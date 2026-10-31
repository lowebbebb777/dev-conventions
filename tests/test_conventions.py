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
    "docs/DEVELOPMENT_PHILOSOPHY.md",
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


class DevelopmentAuthority(unittest.TestCase):
    """文字列・リンクの静的保証のみ。委任や人間の承認の実在は証明しない。"""

    def test_philosophy_has_required_sections(self):
        philosophy = _read("docs/DEVELOPMENT_PHILOSOPHY.md")
        required = [
            "目的と適用範囲", "役割ベースの権限体系", "企画・設計権限と実装裁量",
            "フロントローディング", "リスクと不確実性の優先順位", "最短反証実験",
            "実装契約の必須事項", "証拠に基づく完了判定", "独立レビューとユーザー受入",
            "失敗時の差戻し・再設計", "役割交代と引継ぎ",
            "プロジェクト固有規約との関係",
        ]
        for title in required:
            with self.subTest(section=title):
                self.assertRegex(philosophy, rf"(?m)^## \d+\. {re.escape(title)}$")

    def test_readme_and_agents_reference_existing_canon(self):
        canon = "docs/DEVELOPMENT_PHILOSOPHY.md"
        self.assertTrue((ROOT / canon).is_file())
        for file in ("README.md", "AGENTS.md"):
            with self.subTest(file=file):
                self.assertIn(canon, _read(file))

    def test_authority_markers_in_all_entries(self):
        """共通入口と配布テンプレが役割と承認ゲートを落とさない。"""
        for file in ("AGENTS.md", "templates/AGENTS.template.md"):
            text = _read(file)
            with self.subTest(file=file):
                for marker in ("ユーザー", "設計担当AI", "実装担当AI",
                               "独立レビュー担当", "事前承認", "受入基準"):
                    self.assertIn(marker, text, f"{file} lacks {marker}")
                self.assertNotIn("仕様の穴を埋める合理的な既定値", text)
                self.assertNotIn("確認が要るもの(これだけ)", text)

    def test_single_common_ai_entry(self):
        prohibited = [
            str(path.relative_to(ROOT)) for path in ROOT.rglob("CLAUDE.md")
            if ".git" not in path.parts
        ]
        prohibited += [
            str(path.relative_to(ROOT)) for path in ROOT.rglob("CLAUDE.template.md")
            if ".git" not in path.parts
        ]
        self.assertEqual([], prohibited, "AI共通入口はAGENTS.mdのみ")

    def test_four_file_rules_and_negative_verification_survive(self):
        readme = _read("README.md")
        for path in ("AGENTS.md", "docs/STATE.md", "docs/LOG.md", "docs/IDEAS.md"):
            self.assertTrue((ROOT / path).is_file())
            self.assertIn(f"`{path}`", readme)
        self.assertIn("逆検証", readme)
        self.assertIn("FAIL", _read("templates/AGENTS.template.md"))
        self.assertIn("docs/IDEAS.md", _read("templates/docs/STATE.template.md"))

    def test_template_keeps_shared_philosophy_link(self):
        self.assertIn("dev-conventions/blob/main/docs/DEVELOPMENT_PHILOSOPHY.md",
                      _read("templates/AGENTS.template.md"))


class ValueFirstScopePruning(unittest.TestCase):
    """思想正本§14が全AI入口まで届くことの静的テスト。"""

    def test_scope_gate_is_reachable(self):
        philosophy = _read("docs/DEVELOPMENT_PHILOSOPHY.md")
        for marker in ("## 14. ユーザー価値", "既存との重複", "捨てる仕事",
                       "リリース", "忠告", "ユーザーの明示委任"):
            self.assertIn(marker, philosophy)
        for file in ("AGENTS.md", "templates/AGENTS.template.md", "global-pointer.md"):
            with self.subTest(file=file):
                self.assertIn("ユーザー", _read(file))
                self.assertIn("捨てる", _read(file))

    def test_did_original_and_poem(self):
        ideas = _read("docs/IDEAS.md")
        self.assertIn("「捨てるべき仕事」を決めるのは近年の日本人がやれてない最重要任務だ（これdid）", ideas)
        self.assertIn("ユーザーのためにならない仕事は全て捨てていく。", ideas)
        self.assertIn("原文（ユーザー・逐語）", ideas)
        self.assertIn("詩文（AI解釈）", ideas)
        pointer = _read("global-pointer.md")
        self.assertIn("逐語原文＋別記の詩文", pointer)
        self.assertIn("逐語原文＋詩文", ideas)


class CommitAttributionPolicy(unittest.TestCase):
    def test_attribution_policy_links(self):
        self.assertIn("## 15. Gitコミット名義とAI作業実績の分離",
                      _read("docs/DEVELOPMENT_PHILOSOPHY.md"))
        for path in ("AGENTS.md", "README.md", "templates/AGENTS.template.md", "global-pointer.md"):
            self.assertIn("COMMIT_ATTRIBUTION.md", _read(path))
        for path in ("docs/COMMIT_ATTRIBUTION.md", "tools/check_commit_attribution.py",
                     "tools/install_commit_hooks.py"):
            self.assertTrue((ROOT / path).is_file())



class DesignReviewGates(unittest.TestCase):
    """DR段階と入口・任意テンプレの整合だけを静的検証。審査の実在や承認は保証しない。"""

    def test_canonical_stages_and_separate_shipment(self):
        philosophy = _read("docs/DEVELOPMENT_PHILOSOPHY.md")
        self.assertIn("## 16. Design Review", philosophy)
        for stage in ("DR0", "DR1", "DR2", "DR3", "DR4", "DR5", "DR6"):
            with self.subTest(stage=stage):
                self.assertIn(f"**{stage}**", philosophy)
        for rule in ("初回出荷審査", "DR123", "CONDITIONAL GO", "REWORK",
                     "Verification", "Validation", "前工程への差戻し", "軽量DR",
                     "最終ゲート通過"):
            with self.subTest(rule=rule):
                self.assertIn(rule, philosophy)


    def test_market_viability_is_a_mandatory_investment_gate(self):
        """市場性の証拠不足をGOにせず、DR1で投資判断する入口が届くこと。"""
        philosophy = _read("docs/DEVELOPMENT_PHILOSOPHY.md")
        for marker in ("## 16.4 市場性・事業継続性", "市場に勝てる余地があるから作る",
                       "PENDING", "機会費用", "悲観・標準・楽観", "DR2"):
            with self.subTest(marker=marker):
                self.assertIn(marker, philosophy)
        for file in ("AGENTS.md", "templates/AGENTS.template.md", "README.md", "global-pointer.md"):
            with self.subTest(file=file):
                body = _read(file)
                self.assertIn("§16.4", body)
                self.assertIn("PENDING", body)
        record = _read("templates/docs/DR_RECORD.template.md")
        for marker in ("市場性・事業性", "機会費用", "悲観", "標準", "楽観", "PENDING"):
            with self.subTest(record_field=marker):
                self.assertIn(marker, record)

    def test_dr_reachable_from_entries_and_record_template(self):
        for file in ("AGENTS.md", "templates/AGENTS.template.md", "README.md", "global-pointer.md"):
            with self.subTest(file=file):
                body = _read(file)
                self.assertIn("DR123", body)
                self.assertIn("初回出荷審査", body)
        path = "templates/docs/DR_RECORD.template.md"
        self.assertTrue((ROOT / path).is_file())
        record = _read(path)
        for field in ("DR0", "DR6", "初回出荷審査", "段階別判断",
                      "判定根拠", "独立レビュー", "未解決課題", "docs/LOG.md"):
            self.assertIn(field, record)


if __name__ == "__main__":
    unittest.main()
