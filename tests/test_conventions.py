"""規約自身の機械チェック (README 原則7)。

散文で書かれた規則は必ず風化する。行数上限・索引の実在・必須ファイルのように
機械的に判定できるものは、心がけでなくここで落とす。
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_MAX_LINES = 50


MIN_TAGS = 2


def parse_shelf(ideas_md: str) -> list[tuple[str, list[str]]]:
    """IDEAS.md の棚から (行, タグ列) を取り出す。

    行の形: - <詩> — `YYYY-MM-DD` <状態> — `タグ` `タグ`
    `## 棚` より前の説明文と、コメント内の例は拾わない。
    """
    entries: list[tuple[str, list[str]]] = []
    in_shelf = False
    in_comment = False
    for line in ideas_md.splitlines():
        if line.startswith("## "):
            in_shelf = line.startswith("## 棚")
            continue
        if "<!--" in line:
            in_comment = True
        if "-->" in line:
            in_comment = False
            continue
        if not in_shelf or in_comment or not line.startswith("- "):
            continue
        ticks = re.findall(r"`([^`]+)`", line)
        if not ticks or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ticks[0]):
            continue
        entries.append((line, ticks[1:]))
    return entries

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "global-pointer.md",
    "projects.md",
    "docs/STATE.md",
    "docs/LOG.md",
    "docs/IDEAS.md",
    "templates/AGENTS.template.md",
    "templates/docs/STATE.template.md",
    "templates/docs/LOG.template.md",
    "templates/docs/IDEAS.template.md",
]


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def parse_projects(projects_md: str) -> list[tuple[str, str, str]]:
    """projects.md の表から (プロジェクト名, ローカルパス, remote) を取り出す。

    行の形: | 名前 | `C:\\...\\path` | remote | 正典 |
    ヘッダ・区切り行・コメントは自然に弾かれる(バッククォート付きパスが無いため)。
    """
    found: list[tuple[str, str, str]] = []
    for line in projects_md.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        m = re.fullmatch(r"`([^`]+)`", cells[1])
        if m:
            found.append((cells[0], m.group(1), cells[2]))
    return found


class RequiredFiles(unittest.TestCase):
    def test_all_present(self):
        missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
        self.assertEqual([], missing, f"規約の必須ファイルが欠けている: {missing}")


class StateFile(unittest.TestCase):
    """STATE は「現在地」であって履歴ではない (README 原則4)。"""

    def setUp(self):
        self.text = _read("docs/STATE.md")

    def test_within_line_cap(self):
        n = len(self.text.splitlines())
        self.assertLessEqual(
            n, STATE_MAX_LINES,
            f"STATE.md が {n} 行 (上限 {STATE_MAX_LINES})。"
            "履歴は docs/LOG.md、アイディアは docs/IDEAS.md へ移すこと",
        )

    def test_has_last_updated(self):
        self.assertRegex(
            self.text, r"最終更新.*\d{4}-\d{2}-\d{2}",
            "STATE.md に『最終更新: YYYY-MM-DD』が無い。鮮度が判定できない",
        )

    def test_points_at_idea_shelf(self):
        """棚は毎回読まれないので、STATE の1行だけが発見経路になる。"""
        self.assertIn(
            "docs/IDEAS.md", self.text,
            "STATE.md にアイディア棚へのポインタが無い。棚は忘れられる",
        )


class ProjectIndex(unittest.TestCase):
    """索引は、指した先が消えても平気な顔をしている。

    各行は「ローカルに実在する」か「remote から clone できる」のどちらかで
    必ず辿れなければならない。どちらでもない行は、次走者を空振りさせる。
    """

    def test_every_entry_is_reachable(self):
        entries = parse_projects(_read("projects.md"))
        self.assertTrue(entries, "projects.md からプロジェクト行を1件も抽出できなかった")
        unreachable = []
        for name, path, remote in entries:
            if Path(path).is_dir():
                continue                      # ローカルにある
            if "github.com/" in remote:
                continue                      # clone できる(ローカル未固定でよい)
            unreachable.append((name, path, remote))
        self.assertEqual(
            [], unreachable,
            "projects.md にローカルにも remote にも辿れない行がある: "
            f"{unreachable}",
        )


class IdeaShelf(unittest.TestCase):
    """詩は grep の取っ手になる名詞を削ぎ落とす形式。

    タグの無い詩は、棚に載っていても見つからない = 捨てたのと同じ。
    """

    def test_every_entry_has_grep_tags(self):
        entries = parse_shelf(_read("docs/IDEAS.md"))
        self.assertTrue(entries, "docs/IDEAS.md の棚から1件も抽出できなかった")
        untagged = [line[:40] for line, tags in entries if len(tags) < MIN_TAGS]
        self.assertEqual(
            [], untagged,
            f"タグが {MIN_TAGS} 語未満の詩がある(grep で見つからない): {untagged}",
        )


class Templates(unittest.TestCase):
    def test_state_template_carries_shelf_pointer(self):
        """テンプレ側に無いと、新規repoは棚を持たないまま生まれる。"""
        self.assertIn("docs/IDEAS.md", _read("templates/docs/STATE.template.md"))

    def test_agents_template_mentions_negative_verification(self):
        """緑だけを根拠にさせない (README 原則2)。"""
        self.assertIn("FAIL", _read("templates/AGENTS.template.md"))


if __name__ == "__main__":
    unittest.main()
