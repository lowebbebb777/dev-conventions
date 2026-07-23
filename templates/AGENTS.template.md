# AGENTS.md — <プロジェクト名 / Project Name> エージェント共通ルール / Common Agent Rules

全エージェント(Codex / Antigravity / Claude Code / Cursor)共通の入口。
Common entry point for all agents.
**このファイルには「今やること」を書かない**(陳腐化するため)。現在地は `docs/STATE.md`。
**Never write "current tasks" here** (it goes stale). Current position lives in `docs/STATE.md`.

## 読む順番 / Reading Order

1. <思想・不変条件の正典 / canonical doc for philosophy & invariants> — 最優先 / highest priority
2. `docs/STATE.md` — 現在地と残作業 / current position and remaining work
3. <設計文書 / design docs> — 仕様の正。矛盾時の優先順位: <A> > <B> / spec canon; precedence on conflict
4. `docs/LOG.md` — 経緯と判断理由(必要時のみ遡る)/ history and rationale (consult as needed)

## ビルド・環境 / Build & Environment

<!-- OS、シェル、環境変数、ビルド・テストコマンドをコピペ可能な形で。落とし穴も。
     OS, shell, env vars, build/test commands in copy-pastable form. Include gotchas. -->

```
<build command>
<test command>
```

## 不変条件 / Invariants

<!-- 要約+正典へのポインタ。正典と二重管理になるなら要約は箇条書き見出しのみに留める。
     Summary + pointer to canon. If duplication risks drift, keep only one-line headings. -->

正は <正典ファイル>。/ Canon: <canonical file>.

## 終了時の義務 / End-of-Session Duties

このリポジトリは複数エージェントのリレーで開発されている。記録が次走者の命綱。
This repo is developed in relay by multiple agents. The record is the next runner's lifeline.

1. **1 Step = 1 コミット**。メッセージに仕様の節番号(例: `SPEC §5-①`)。
   未コミットの変更を残して終わらない。
   One step = one commit citing the spec section. Never end with uncommitted changes.
2. `docs/STATE.md` を**上書き更新**(古い進捗記述は消す。履歴は LOG と git にある)。
   Overwrite `docs/STATE.md` (delete stale progress; history lives in LOG and git).
3. `docs/LOG.md` に**1エントリ追記**(テンプレートは LOG.md 冒頭。「逸脱」欄は必須)。
   Append one entry to `docs/LOG.md` (template at top of LOG.md; "Deviations" field is mandatory).
4. ビルドとテストを実行し、結果(件数・緑/赤)を STATE と LOG に記録。
   赤のまま終わる場合はその旨を STATE の先頭に明記。
   Run build and tests; record results (counts, green/red) in STATE and LOG.
   If ending red, say so at the top of STATE.
5. エージェント固有メモリ(`~/.claude` 等)だけに repo の事実を置かない。
   次走者が必要とする情報は必ず repo 内へ。
   Never keep repo facts only in agent-private memory; the next runner's info goes in the repo.
