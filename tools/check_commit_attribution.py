"""Future-commit AI-attribution validator. Never rewrites Git history."""
from __future__ import annotations
import argparse
import re
import subprocess
import sys
from pathlib import Path


def is_agent(name: str) -> bool:
    return bool(re.fullmatch(
        r"claude(?: (?:code|opus|sonnet|haiku|fable)(?: [\w.-]+)*)?|"
        r"codex(?: [\w.-]+)*|chatgpt(?: [\w.-]+)*|openai codex|"
        r"antigravity|gemini(?: cli)?|github copilot|copilot|gpt(?:-[\w.-]+)*",
        name.strip(), flags=re.I))


def identity_issue(name: str, email: str) -> str | None:
    if not name.strip() or not email.strip() or "@" not in email:
        return "氏名・メール未設定"
    if is_agent(name):
        return "AI名義: " + name
    local, domain = email.casefold().rsplit("@", 1)
    if (local in ("noreply", "claude") and domain == "anthropic.com") or (
        domain == "users.noreply.github.com" and re.search(r"(?:^|[+.-])claude$", local)
    ):
        return "AIメール: " + email
    return None


def message_issues(body: str) -> list[str]:
    issues = []
    for line in body.splitlines():
        co = re.match(r"^\s*Co-Authored-By:\s*(.*)$", line, re.I)
        if co:
            m = re.fullmatch(r"(.*?)\s*<([^<>]+)>", co.group(1).strip())
            if m:
                bad = identity_issue(m.group(1), m.group(2))
                if bad:
                    issues.append("AI Co-Authored-By: " + bad)
            elif re.search(r"\b(claude|anthropic|codex|chatgpt|gemini|copilot|antigravity)\b",
                           co.group(1), re.I):
                issues.append("AI Co-Authored-By: " + co.group(1))
        if re.match(r"^\s*Claude-Session:", line, re.I):
            issues.append("Claude-Session URLをコミットせずLOGへ記録")
    return issues


def git(*args: str) -> str:
    p = subprocess.run(["git", *args], encoding="utf-8", text=True, capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or "git error")
    return p.stdout


def current_issues() -> list[str]:
    issues = []
    for role in ("AUTHOR", "COMMITTER"):
        raw = git("var", "GIT_" + role + "_IDENT").strip()
        m = re.fullmatch(r"(.*?)\s*<([^<>]+)>\s+\d+\s+[+-]\d{4}", raw)
        if not m:
            issues.append(role + ": 名義を解釈できません")
        else:
            bad = identity_issue(m.group(1), m.group(2))
            if bad:
                issues.append(role + ": " + bad)
    return issues


def range_issues(spec: str) -> list[str]:
    if ".." not in spec or spec.startswith("-"):
        raise ValueError("BASE..HEAD を指定してください")
    issues = []
    for sha in git("rev-list", "--reverse", spec).splitlines():
        raw = git("show", "-s", "--format=%an%x1f%ae%x1f%cn%x1f%ce%x1f%B", sha)
        fields = raw.split("\x1f", 4)
        if len(fields) != 5:
            raise RuntimeError("commit parse failed: " + sha)
        an, ae, cn, ce, body = fields
        for role, name, email in (("AUTHOR", an, ae), ("COMMITTER", cn, ce)):
            bad = identity_issue(name, email)
            if bad:
                issues.append(sha[:12] + " " + role + ": " + bad)
        issues.extend(sha[:12] + " message: " + x for x in message_issues(body))
    return issues


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    modes = ap.add_mutually_exclusive_group(required=True)
    modes.add_argument("--current", action="store_true")
    modes.add_argument("--message", type=Path)
    modes.add_argument("--range", dest="revision_range")
    args = ap.parse_args(argv)
    try:
        if args.current:
            issues = current_issues()
        elif args.message is not None:
            issues = message_issues(args.message.read_text(encoding="utf-8-sig"))
        else:
            issues = range_issues(args.revision_range)
    except (RuntimeError, ValueError, OSError) as e:
        print("ERROR:", e, file=sys.stderr)
        return 2
    if issues:
        for item in issues:
            print("BLOCKED:", item, file=sys.stderr)
        return 1
    print("OK: AI名義の問題を検出しませんでした")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
