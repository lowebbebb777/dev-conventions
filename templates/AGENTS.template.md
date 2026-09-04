# AGENTS.md — <プロジェクト名 / Project Name> エージェント共通ルール / Common Agent Rules

全エージェント(Codex / Antigravity / Claude Code / Cursor)共通の入口 / Common entry point for all agents.
**このファイルには「今やること」を書かない**(陳腐化するため)。現在地は `docs/STATE.md` / **Never write "current tasks" here** (it goes stale). Current position lives in `docs/STATE.md`.

## 読む順番 / Reading Order

1. <思想・不変条件の正典 / canonical doc for philosophy & invariants> — 最優先 / highest priority
2. `docs/STATE.md` — 現在地と残作業 / current position and remaining work
3. <設計文書 / design docs> — 仕様の正。矛盾時の優先順: <A> > <B> / spec canon; precedence on conflict
4. `docs/LOG.md` — 経緯と判断理由(必要時のみ遡る) / history and rationale (consult as needed)

## ビルド・環境 / Build & Environment

```
<build command>
<test command>
```

テストを持たないリポジトリではその旨と、代わりの検証手順を書く /
If the repo has no tests, say so and write the verification procedure used instead.

## 不変条件 / Invariants

正は <正典ファイル> / Canon: <canonical file>.

## 終了時の義務 / End-of-Session Duties

このリポジトリは複数エージェントのリレーで開発されている。記録が次走者の命綱 / This repo is developed in relay by multiple agents. The record is the next runner's lifeline.

1. **1 Step = 1 コミット**。仕様があればメッセージに節番号、無ければ目的を1行 /
   One step = one commit; cite the spec section if there is one, otherwise one line of intent.
2. `docs/STATE.md` を**上書き更新** / Overwrite `docs/STATE.md`.
3. `docs/LOG.md` に**1エントリ追記** / Append one entry to `docs/LOG.md`.
4. 検証を実行し、結果(何をどう確かめたか)を STATE と LOG に記録 /
   Run the verification; record in STATE and LOG what you checked and how.
5. repo の事実は必ず repo 内に置く(エージェント固有メモリだけに残さない) /
   Repo facts always live in the repo; never only in agent-private memory.

## 運用の指針 / Operating Guidance

すべて**既定値**であり、AIの判断で外してよい。外したら LOG に1行理由を書く /
These are **defaults**, not walls. Deviate when it serves the task; note the reason in LOG.

1. **報告は結論ファースト / Lead with the conclusion**:
   挨拶・前置き・自己弁護は書かない。ただし**行数上限は設けない** — 判断理由・
   トレードオフ・リスク・逸脱は必要なだけ書く。「短さ」より「次走者が再現できること」 /
   No greetings or preamble, but **no line limit**: write as much rationale, trade-off,
   risk and deviation as the next runner needs to reproduce your reasoning.
2. **探索は構造から、変更は本体を読んでから / Skim structurally, read before you edit**:
   俯瞰には AST 要約や grep / ripgrep(各AIのネイティブ検索でよい)を使う。
   **変更を加えるファイルは本体を読む**。読まずに直した手戻りは、節約したトークンより高くつく /
   Use AST summaries and grep to orient, but read the full file you are about to change —
   a wrong edit costs more than the tokens it saved.
3. **状態の正は `docs/STATE.md` 一つ / One source of truth for state**:
   補助的な JSON/メモはセッション内利用に留め commit しない。食い違ったら STATE が正 /
   Keep scratch state out of the repo; on conflict, STATE wins.
4. **完了の判定 / Definition of done**:
   - テストがある領域: 緑は**必要条件**。緑だから十分とは限らない /
     Where tests exist, green is necessary but not sufficient.
   - テストが無い領域(ドキュメント・UI・調査): 「どう確かめたか」を手順ごと
     STATE の「検証済みの事実」に書けば完了としてよい /
     Where they don't, writing the exact verification steps into STATE counts as done.
   - **緑になった瞬間にセッションを終える義務はない**。残作業を続けてよい /
     Green does not oblige you to stop; carry on with the remaining work.

## 自律範囲 / Autonomy — 確認なしでやってよいこと

迷ったら止まるのではなく、**仮定を STATE に明記して進める** /
When uncertain, proceed on a stated assumption recorded in STATE rather than halting.

- 読み取り全般 / ビルド・テスト・lint・型チェックの実行 / Reading, building, testing, linting
- 実装・リファクタ・テスト追加、作業ブランチの作成、ローカル commit /
  Implementing, refactoring, adding tests, branching, committing locally
- 一時ファイル(scratch)の作成、サブエージェント・並列探索の起動 /
  Scratch files, subagents, parallel exploration
- 仕様の穴を埋める合理的な既定値の採用(採った仮定を STATE に1行書く) /
  Filling spec gaps with reasonable defaults (record the assumption in STATE)
- **規約そのものへの改善提案**(このファイルを含む。提案は LOG に書き、適用はユーザー承認後) /
  Proposing changes to this convention itself (write the proposal in LOG; apply after approval)

確認が要るもの(これだけ)/ Ask first — only these:

- `push` / PR作成 / リリース・デプロイ、外部への送信 / Pushing, PRs, releases, anything outbound
- 破壊的操作(履歴改変、force push、ファイル・データの削除)/ Destructive operations
- 依存の追加・更新、有料APIの実行 / Adding or upgrading dependencies, paid API calls
- `docs/STATE.md`「着手禁止」に載っている項目 / Anything listed under STATE's "Do Not Start"

## ショートカット(合言葉)/ Shortcuts
- **ds = 引継ぎする**: `docs/STATE.md` を読んで「残作業」の最上位から着手し、区切りでは上記
  「終了時の義務」に従う / read STATE.md and start from the top remaining task.
- **dm = 引継ぎ保存**: 途中経過を `docs/STATE.md`(次の一手)と `docs/LOG.md` に書いて commit /
  checkpoint now before switching AI mid-task.
- **di = 引継ぎ登録**: 新規repoを規約に登録(テンプレから AGENTS/STATE/LOG 作成 +
  `dev-conventions/projects.md` に1行追加 + commit)/ onboard a new repo.
