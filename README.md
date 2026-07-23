# dev-conventions — マルチエージェント引き継ぎ規約 / Multi-Agent Handoff Convention

複数のAIエージェント(Claude Code / Codex / Antigravity / Cursor 等)と人間がリレーで
開発するリポジトリのための共通規約。
A shared convention for repositories developed in relay by multiple AI agents
(Claude Code / Codex / Antigravity / Cursor, etc.) and humans.

## 目的 / Purpose

次走者が**「読む」のでなく「検証」で現在地を把握できる**状態を保つこと。
黙った逸脱と文書の陳腐化による事故をなくすこと。
Keep the repo in a state where the next runner can locate the current position by
**verifying, not reading**. Eliminate accidents caused by silent deviations and stale docs.

## 3ファイル構成 / The Three Files

| ファイル / File | 性質 / Nature | 役割 / Role |
|---|---|---|
| `AGENTS.md` | ほぼ不変 / Rarely changes | 全エージェント共通の入口。環境・規則・ポインタのみ / Common entry point: environment, rules, pointers only |
| `docs/STATE.md` | **常に上書き** / Always overwritten | 現在地。1画面(50行)以内 / Current position. One screen (≤50 lines) |
| `docs/LOG.md` | **追記のみ** / Append-only | セッション履歴と判断理由 / Session history and rationale |

分離の理由: 「現在地」と「履歴」を1ファイルに混ぜると、本文が陳腐化して
冒頭に「⚠️この下は古い」バナーを貼る羽目になる(実際に起きた失敗)。
Why separate: mixing "current position" and "history" in one file leads to a stale body
with a "⚠️ outdated below" banner on top (a failure we actually experienced).

## 原則 / Principles

1. **1 Step = 1 コミット**。メッセージに仕様の節番号。未コミットで引き継がない。
   One step = one commit, citing the spec section. Never hand off uncommitted work.
2. **散文よりテスト**。「完了」の根拠はテスト緑。受け入れ条件は可能な限りテストに落とす。
   Tests over prose. "Done" means green tests. Turn acceptance criteria into tests wherever possible.
3. **黙った逸脱の禁止**。仕様に無いことをやったら LOG の「逸脱」欄に理由つきで申告。
   No silent deviations. Anything beyond spec goes in the LOG's "Deviations" field with a reason.
4. **古い進捗記述は消す**。履歴は LOG と git にある。STATE に歴史を溜めない。
   Delete stale progress notes. History lives in LOG and git; STATE hoards no past.
5. **エージェント固有メモリに repo の事実を置かない**。`~/.claude` 等は他エージェントから
   見えない。次走者が必要とする情報は必ず repo 内に置く。
   No repo facts in agent-private memory (`~/.claude` etc. is invisible to other agents).
   Anything the next runner needs lives in the repo.
6. **矛盾の仲裁ルールを文書側に持たせる**。エージェント同士は会話できない。
   優先順位(どの文書が正か)を AGENTS.md / STATE.md に明記する。
   Encode conflict arbitration in the docs. Agents cannot talk to each other;
   the precedence order (which doc wins) must be written down.

## 新規プロジェクトへの導入 / Adopting in a New Project

1. `templates/AGENTS.template.md` → リポジトリ直下に `AGENTS.md` としてコピーし、穴埋め
   Copy to repo root as `AGENTS.md` and fill in the blanks
2. `templates/docs/STATE.template.md` → `docs/STATE.md` / `templates/docs/LOG.template.md` → `docs/LOG.md`
3. `CLAUDE.md` は薄いラッパにする: 「まず `AGENTS.md` を読むこと」+ Claude 固有事項のみ
   Make `CLAUDE.md` a thin wrapper: "Read `AGENTS.md` first" + Claude-specific notes only
   (Codex/Antigravity は `AGENTS.md` を、Claude Code は `CLAUDE.md` をネイティブに読むため、
   正典は1つにし他方をポインタにする /
   Codex/Antigravity natively read `AGENTS.md`, Claude Code reads `CLAUDE.md`;
   keep one canonical file and make the other a pointer)

既存プロジェクトでは、確立済みの正典(例: `CLAUDE.md` が正)を無理に入れ替えない。
ポインタの向きを逆にするだけでよい。
In existing projects, don't force-swap an established canon (e.g., `CLAUDE.md` as source of
truth); just reverse the direction of the pointer.
