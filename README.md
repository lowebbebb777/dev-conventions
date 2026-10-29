# dev-conventions — マルチエージェント引き継ぎ規約 / Multi-Agent Handoff Convention

複数のAIエージェント(Claude Code / Codex / Antigravity / Cursor 等)と人間がリレーで
開発するリポジトリのための共通規約。
A shared convention for repositories developed in relay by multiple AI agents
(Claude Code / Codex / Antigravity / Cursor, etc.) and humans.

## 目的 / Purpose

次走者が**「読む」のでなく「検証」で現在地を把握できる**状態を保つこと。
黙った逸脱と文書の陳腐化による事故をなくすこと。
さらに、開発思想と役割ごとの権限を共有し、仕様を勝手に変えずに要求達成を検証すること。
Keep the repo in a state where the next runner can locate the current position by
**verifying, not reading**. Eliminate accidents caused by silent deviations and stale docs.

## 開発思想・権限の正本 / Canonical Development Philosophy

**[docs/DEVELOPMENT_PHILOSOPHY.md](docs/DEVELOPMENT_PHILOSOPHY.md)** は全プロジェクト共通の
開発思想と権限境界の正本。AI の権限はモデル名・性能・製品名ではなく、**ユーザーによる明示的な役割委任**で決まる。
ユーザーが最終承認を行い、企画・設計はユーザーと明示的に任命された設計担当 AI のみが担う。
実装担当は承認済み契約内の技術的裁量を持つが、要求、設計、受入基準、作業範囲、権限は変えない。
独立レビュー・必要な実機評価・ユーザー受入をテスト PASS と区別する。

規約の層: `docs/DEVELOPMENT_PHILOSOPHY.md`（権限・思想）→ `README.md`（構成・原則）→
`AGENTS.md`（全 AI の実行入口）→ `docs/STATE.md`（現在地）/ `docs/LOG.md`（承認・履歴）/
`docs/IDEAS.md`（棚）。引継ぎの既存優先順位は README > global-pointer > STATE。
明示されたユーザー指示と承認済みの実装契約を、一般規約で上書きしない。

## 4ファイル構成 / The Four Files

| ファイル / File | 性質 / Nature | 読む頻度 / Read | 役割 / Role |
|---|---|---|---|
| `AGENTS.md` | ほぼ不変 / Rarely changes | 毎回 / always | 全エージェント共通の入口。環境・規則・ポインタのみ / Common entry point: environment, rules, pointers only |
| `docs/STATE.md` | **常に上書き** / Always overwritten | 毎回 / always | 現在地。1画面(50行)以内 / Current position. One screen (≤50 lines) |
| `docs/LOG.md` | **追記のみ** / Append-only | 事故調査時 / on incident | セッション履歴と判断理由 / Session history and rationale |
| `docs/IDEAS.md` | **追記のみ** / Append-only | **grep時のみ** / on grep | アイディア棚。1件＝詩(散文でない1〜2文) / Idea shelf: one entry = a poetic line or two, never prose |

分離の理由: 「現在地」と「履歴」を1ファイルに混ぜると、本文が陳腐化して
冒頭に「⚠️この下は古い」バナーを貼る羽目になる(実際に起きた失敗)。
Why separate: mixing "current position" and "history" in one file leads to a stale body
with a "⚠️ outdated below" banner on top (a failure we actually experienced).

`IDEAS.md` を分ける理由: 置き場が無いと、惜しい案が STATE に居座って肥大する。
実測(2026-08-02): 登録4プロジェクト中2つが50行上限超過、最大は **250行**(規則の5倍)。
分ける基準は**重要度ではなくアクセス頻度**。毎回読まれる STATE に、たまにしか要らない
ものを置くと、全エージェントが毎セッション運搬費を払い続ける。
Why `IDEAS.md`: without a home, good-but-not-now ideas squat in STATE and bloat it
(measured 2026-08-02: 2 of 4 registered projects exceed the 50-line cap; worst is **250 lines**).
Split by **access frequency, not importance** — anything parked in STATE is carried by
every agent, every session.

## 原則 / Principles

1. **1 Step = 1 コミット**。仕様があればメッセージに節番号、無ければ目的を1行。
   未コミットで引き継がない。
   One step = one commit — cite the spec section if there is one, otherwise one line of
   intent. Never hand off uncommitted work.
2. **散文よりテスト、緑より逆検証**。「完了」の根拠はテスト緑。ただし**そのテストが修正前の
   コードで FAIL することを必ず確認する**。緑だけでは「本物のテスト」と「何も検証していない
   テスト」を区別できない(実例: 中核が両端ダミーのまま全テスト緑だった)。
   テストを持てない領域(ドキュメント・調査)は、「何をどう確かめたか」を手順ごと STATE に
   書くことが根拠になる。手順を書けないものは完了ではない。
   Tests over prose; negative verification over green. "Done" means green tests — but always
   confirm the test FAILS against the pre-fix code. Green alone cannot tell a real test from
   one that verifies nothing (real case: all green while the core was a dummy at both ends).
   Where tests cannot exist (docs, investigation), the evidence is the verification procedure
   written into STATE; if you cannot write the steps, it is not done.
3. **黙った逸脱の禁止**。仕様に無いことをやったら LOG の「逸脱」欄に理由つきで申告。
   No silent deviations. Anything beyond spec goes in the LOG's "Deviations" field with a reason.
4. **古い進捗記述は消す**。履歴は LOG と git にある。STATE に歴史を溜めない。
   Delete stale progress notes. History lives in LOG and git; STATE hoards no past.
5. **repo の事実は repo 内に置く**。`~/.claude` 等のエージェント固有メモリは他エージェントから
   見えないため、そこ**だけ**に置かない。併用は自由 — 次走者が必要とする情報が repo 内に
   あることだけを担保する。
   Repo facts live in the repo. Agent-private memory (`~/.claude` etc.) is invisible to other
   agents, so never let it be the *only* copy; using it alongside the repo is fine.
6. **矛盾の仲裁ルールを文書側に持たせる**。エージェント同士は会話できない。
   優先順位(どの文書が正か)を AGENTS.md / STATE.md に明記する。
   Encode conflict arbitration in the docs. Agents cannot talk to each other;
   the precedence order (which doc wins) must be written down.
7. **規約自身にも原則2を適用する**。心がけは必ず風化するので、機械的に落とせるものは
   `tests/` に落とす(行数上限・索引の実在・必須ファイル)。散文の規約は守られない。
   Apply Principle 2 to the convention itself. Good intentions decay; whatever can be
   checked mechanically belongs in `tests/` (line caps, index validity, required files).

## 実装契約から受入まで / Working Procedure

1. **委任を確認**: ユーザーが定めた設計・実装・独立レビューの担当と権限範囲を記録する。モデル名では代用しない。
2. **上流で確定**: 要求・不変条件・対象外・受入基準・必要な実機試験を確かめ、最も安価な反証実験を先に行う。
3. **契約内で実装**: 軽微・可逆な実装選択は進めるが、仕様の穴を設計判断で埋めない。影響・選択肢・推奨案を返す。
4. **証拠を残す**: 既存／追加テスト、変更前 FAIL の逆検証、回帰、実機評価の有無を区別して記録する。
5. **独立レビュー・ユーザー受入**: 実装者の自己申告やテスト PASS だけで最終完了を宣言しない。
   変更・承認履歴は `docs/LOG.md`、現在地は `docs/STATE.md` に残す。

## 新規プロジェクトへの導入 / Adopting in a New Project

1. `templates/AGENTS.template.md` → リポジトリ直下に `AGENTS.md` としてコピーし、穴埋め
   Copy to repo root as `AGENTS.md` and fill in the blanks
2. `templates/docs/STATE.template.md` → `docs/STATE.md` / `templates/docs/LOG.template.md` → `docs/LOG.md`
   / `templates/docs/IDEAS.template.md` → `docs/IDEAS.md`
3. 全エージェント共通の入口として `AGENTS.md` に一本化する。個別ツール用の `CLAUDE.md` 等は作成せず、
   既存の `CLAUDE.md` は最新Headから削除して内容を `AGENTS.md` に統合する /
   Unify on `AGENTS.md` as the common entry point for all agents. Do not create tool-specific
   files like `CLAUDE.md`; delete existing `CLAUDE.md` files from latest Head and integrate their contents into `AGENTS.md`.

4. `docs/DEVELOPMENT_PHILOSOPHY.md` を共通原則として参照し、ユーザーの明示委任と
   プロジェクト固有の承認済み実装契約を `AGENTS.md` から辿れるようにする。
5. `templates/tests/test_conventions.template.py` を `tests/test_conventions.py` に配備し、
   既存の4ファイルと権限規則、禁止された `CLAUDE.md` の不在を検証する。
   他リポジトリへ自動展開しない（対象と適用はユーザー承認を要する）。
