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
| `docs/STATE.md` | **常に上書き** / Always overwritten | 現在地。目安1画面(50行)。正確さが上限に優先 / Current position. ~50 lines as a guide; accuracy outranks the limit |
| `docs/LOG.md` | **追記のみ** / Append-only | セッション履歴と判断理由 / Session history and rationale |

分離の理由: 「現在地」と「履歴」を1ファイルに混ぜると、本文が陳腐化して
冒頭に「⚠️この下は古い」バナーを貼る羽目になる(実際に起きた失敗)。
Why separate: mixing "current position" and "history" in one file leads to a stale body
with a "⚠️ outdated below" banner on top (a failure we actually experienced).

## 原則 / Principles

1. **1 Step = 1 コミット**。仕様があればメッセージに節番号、無ければ目的を1行。
   未コミットで引き継がない。
   One step = one commit — cite the spec section if there is one, otherwise one line of
   intent. Never hand off uncommitted work.
2. **散文より検証可能な根拠**。受け入れ条件は可能な限りテストに落とす。テストがある領域では
   緑が必要条件(緑=十分ではない)。テストを持てない領域(ドキュメント・UI・調査)は、
   「何をどう確かめたか」を手順ごと STATE に書くことが根拠になる。
   Verifiable evidence over prose. Turn acceptance criteria into tests wherever possible;
   where tests exist, green is necessary but not sufficient. Where tests cannot exist
   (docs, UI, investigation), the evidence is the verification procedure written into STATE.
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
