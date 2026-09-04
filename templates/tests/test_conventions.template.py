"""引き継ぎ規約の機械チェック (dev-conventions README 原則7)。

新規repoへ導入するときは `tests/test_conventions.py` としてコピーするだけでよい。
ROOT はこのファイルから2階層上を repo ルートと見なす(`<repo>/tests/` 配置が前提)。

言語やビルド系に依存しないので、Android / Python / Node いずれのrepoでも動く。
Python が無いrepoでは、同じ4項目を各repoのテスト系で書き直すこと。
"""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_MAX_LINES = 50


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class HandoffConvention(unittest.TestCase):
    def test_required_files_present(self):
        required = ["AGENTS.md", "docs/STATE.md", "docs/LOG.md", "docs/IDEAS.md"]
        missing = [p for p in required if not (ROOT / p).is_file()]
        self.assertEqual([], missing, f"引き継ぎ規約の必須ファイルが欠けている: {missing}")

    def test_state_within_line_cap(self):
        """STATE は現在地であって履歴ではない (原則4)。"""
        n = len(_read("docs/STATE.md").splitlines())
        self.assertLessEqual(
            n, STATE_MAX_LINES,
            f"docs/STATE.md が {n} 行 (上限 {STATE_MAX_LINES})。"
            "履歴は docs/LOG.md へ、今やらない案は docs/IDEAS.md へ移すこと",
        )

    def test_state_has_last_updated(self):
        self.assertRegex(
            _read("docs/STATE.md"), r"最終更新.*\d{4}-\d{2}-\d{2}",
            "STATE.md に『最終更新: YYYY-MM-DD』が無い。鮮度が判定できない",
        )

    def test_state_points_at_idea_shelf(self):
        """棚は毎回読まれない。STATE の1行だけが唯一の発見経路。"""
        self.assertIn(
            "docs/IDEAS.md", _read("docs/STATE.md"),
            "STATE.md にアイディア棚へのポインタが無い。棚は忘れられる",
        )


if __name__ == "__main__":
    unittest.main()
