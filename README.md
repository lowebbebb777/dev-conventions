# dev-conventions — マルチエージェント引き継ぎ規約 / Multi-Agent Handoff Convention

複数のAIエージェント(ChatGPT / Claude Code / Codex / Antigravity / Cursor / gbmc 等)と人間がリレーで
開発するリポジトリのための、**AIに依存しない単一正本の共通規約**。
A shared convention for repositories developed in relay by multiple AI agents
(Claude Code / Codex / Antigravity / Cursor, etc.) and humans.

## 目的 / Purpose

次走者が**「読む」のでなく「検証」で現在地を把握できる**状態を保つこと。
黙った逸脱と文書の陳腐化による事故をなくすこと。
Keep the repo in a state where the next runner can locate the current position by
**verifying, not reading**. Eliminate accidents caused by silent deviations and stale docs.

## 唯一の規約正本 / Single Source of Rules

**各repoの `AGENTS.md` が共通規約の唯一の正本。** すべてのAIに同じ目的理解・承認範囲・終了条件を適用する。AIごとに「Claude用の指示」「Codex用の規則」を分けて管理しない。各製品の仕様書は `AGENTS.md` から参照する。

`CLAUDE.md` は読み込み互換のため残してよいが、**中身は `AGENTS.md` への案内のみ**（`templates/CLAUDE.template.md`）。技術的に自動読込するファイル名が異なることは、ルールを分ける理由にはならない。二つの内容を手動で同期・複製する方式も避ける。

- **規約**: `AGENTS.md`（全AI共通）
- **現状**: `docs/STATE.md`（現在地・残作業）
- **履歴**: `docs/LOG.md`（実施・検証・逸脱）
- **アイデア**: `docs/IDEAS.md`（将来案）
- **互換入口**: `CLAUDE.md`（規約ではなく `AGENTS.md` のポインター）

`AGENTS.md` が利用できない実行環境では、利用者に制約を示してからリポジトリ内の同じ規約を読み込む。規約を理解できないまま、異なる「AI向け既定ルール」を勝手に適用しない。

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

## 新規プロジェクトへの導入 / Adopting in a New Project

1. `templates/AGENTS.template.md` → リポジトリ直下に `AGENTS.md` としてコピーし、穴埋め
   Copy to repo root as `AGENTS.md` and fill in the blanks
2. `templates/docs/STATE.template.md` → `docs/STATE.md` / `templates/docs/LOG.template.md` → `docs/LOG.md`
   / `templates/docs/IDEAS.template.md` → `docs/IDEAS.md`
3. `templates/CLAUDE.template.md` をリポジトリ直下の `CLAUDE.md` として配置。
   **追加のClaude固有ルールは禁止。** 参照する `AGENTS.md` が唯一の規約である。
   Copy the neutral compatibility pointer; never put agent-specific directives in it.
4. `templates/tests/test_conventions.template.py` を `tests/test_conventions.py` として配置し、
   STATE行数・必須ファイル・CLAUDEからAGENTSへの参照をテストする（既存のテストは上書きしない）。

### 既存プロジェクトの移行 / Migration (preserve existing instructions)

1. 既存 `AGENTS.md` と `CLAUDE.md` を両方読み、独自の指示・製品仕様・権限・安全条件を一覧化する。自動削除しない。
2. 矛盾する内容は安全な側を暫定維持し、ユーザーの判断を要するものを明記する。合意した全AI共通の運用指示を `AGENTS.md` に統合する。長い製品仕様は別の設計書に置き、AGENTSから参照する。
3. `CLAUDE.md` をポインターのみへ置換する。必要に応じてリネーム前の原文を履歴から追えるようコミットを分離する。**旧CLAUDE内容を移す前に置換しない。**
4. `docs/STATE.md` と `docs/LOG.md` に移行と未確認事項を記載し、検証後にコミットする。対象外repoへの反映は別作業とする。
5. `global-pointer.md` の文面は各AIの設定へ必要な場合に配置するが、それ自体を規約の第二正本にしない。

> 例: SleepSMなど、現在 `CLAUDE.md` を製品思想の正本としている既存repoは、
> 原文を保持して仕様書へ移管し、`AGENTS.md` に正しい参照順を書いてから移行する。
> このdev-conventions変更だけで別repoの規約を上書きしない。
