"""Non-destructive local Git hook installer for the current repository."""
from __future__ import annotations
import os
import subprocess
import sys
from pathlib import Path


def git(*args: str) -> str:
    p = subprocess.run(["git", *args], capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(p.stderr.strip())
    return p.stdout.strip()


def main() -> int:
    try:
        root = Path(git("rev-parse", "--show-toplevel")).resolve()
        if not (root / "tools" / "check_commit_attribution.py").is_file():
            raise RuntimeError("tools/check_commit_attribution.py が見つかりません")
        configured = subprocess.run(["git", "config", "--get", "core.hooksPath"],
                                    capture_output=True, text=True)
        if configured.returncode == 0 and configured.stdout.strip():
            raise RuntimeError("既存core.hooksPathは保護します。手動で統合してください")
        folder = Path(git("rev-parse", "--git-path", "hooks")).resolve()
        hooks = {
            folder / "pre-commit": '#!/bin/sh\npython "tools/check_commit_attribution.py" --current\n',
            folder / "commit-msg": '#!/bin/sh\npython "tools/check_commit_attribution.py" --message "$1"\n',
        }
        for path, content in hooks.items():
            if path.exists() and path.read_text(encoding="utf-8") != content:
                raise RuntimeError("既存hookを上書きしません: " + str(path))
        folder.mkdir(parents=True, exist_ok=True)
        for path, content in hooks.items():
            if not path.exists():
                path.write_text(content, encoding="utf-8", newline="\n")
                if os.name != "nt":
                    path.chmod(path.stat().st_mode | 0o111)
        print("OK: pre-commit / commit-msg hookを導入")
        return 0
    except (RuntimeError, OSError) as e:
        print("ERROR:", e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
