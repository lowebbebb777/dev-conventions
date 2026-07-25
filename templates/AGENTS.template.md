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

## 不変条件 / Invariants

正は <正典ファイル> / Canon: <canonical file>.

## 終了時の義務 / End-of-Session Duties

このリポジトリは複数エージェントのリレーで開発されている。記録が次走者の命綱 / This repo is developed in relay by multiple agents. The record is the next runner's lifeline.

1. **1 Step = 1 コミット**。メッセージに仕様の節番号 / One step = one commit citing the spec section.
2. `docs/STATE.md` を**上書き更新** / Overwrite `docs/STATE.md`.
3. `docs/LOG.md` に**1エントリ追記** / Append one entry to `docs/LOG.md`.
4. ビルドとテストを実行し、結果(件数・緑/赤)を STATE と LOG に記録 / Run build and tests; record results.
5. エージェント固有メモリ(`~/.claude` 等)だけに repo の事実を置かない / Never keep repo facts only in agent-private memory.

## ショートカット / Shortcut: 「Do State」
ユーザーが「Do State」「ds」「続き」等と言ったら、`docs/STATE.md` を読んで「残作業」の最上位から
着手し、区切りでは上記「終了時の義務」に従う / When the user says "Do State"/"ds", read
`docs/STATE.md`, start from the top remaining task, and follow the End-of-Session Duties.
