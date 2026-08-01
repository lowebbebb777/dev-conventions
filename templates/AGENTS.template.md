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
   **新しいテストは、修正前のコードで FAIL することを確認してから緑にする**(緑だけでは
   何も検証していないテストと区別できない)/ Confirm each new test FAILS against the pre-fix
   code before accepting green.
5. エージェント固有メモリ(`~/.claude` 等)だけに repo の事実を置かない / Never keep repo facts only in agent-private memory.
6. 今やらない案が出たら `docs/IDEAS.md` に**詩**(散文でない1〜2文)を追記する。STATE には置かない /
   Park ideas you won't implement now in `docs/IDEAS.md` as a poetic line or two — never in STATE.

## 省トークン・テスト駆動運用規約 / Zero-Token-Waste & TDD Rules

1. **おしゃべり・前置き・丁寧すぎる解説の完全禁止 / No Chatting & Over-explanation**:
   - 会話や応答における無駄な挨拶や自己解説は行わず、**「変更点」と「テスト結果 (PASS/FAIL)」のみを最大 5 行以内で簡潔に報告**すること。
2. **コード丸読みの禁止と AST / 構造検索ツールの活用 / AST & Structural Search**:
   - コードベース構造の探索時は、`tools/ast_summary.py` や `grep_search` を優先利用し、ファイル全体の無用なテキスト流し込みを避けること。
3. **軽量構造化ステートマネージャー / Lightweight JSON State**:
   - 現在地や状態管理には `tools/mcp_state.py` (JSON `.state.json`) を活用し、長文テキストの無駄な読み込みを防止すること。
4. **テスト駆動 (TDD) 判定 / Test-Driven Judgment**:
   - タスクの完了判定は自動テストが PASS することのみを基準とする。テストが PASS したら即座にコミットして終了すること。
   - ただし **PASS だけでは根拠にならない**。新しいテストは**修正前のコードで FAIL することを
     確認**してから採用する(上記「終了時の義務」4)。緑のまま通るテストは何も検証していない /
     Green alone is not evidence: confirm each new test fails against the pre-fix code.

## ショートカット(合言葉)/ Shortcuts
- **ds = 引継ぎする**: `docs/STATE.md` を読んで「残作業」の最上位から着手し、区切りでは上記
  「終了時の義務」に従う / read STATE.md and start from the top remaining task.
- **dm = 引継ぎ保存**: 途中経過を `docs/STATE.md`(次の一手)と `docs/LOG.md` に書いて commit /
  checkpoint now before switching AI mid-task.
- **di = 引継ぎ登録**: 新規repoを規約に登録(テンプレから AGENTS/STATE/LOG/IDEAS +
  `tests/test_conventions.py` を作成 + `dev-conventions/projects.md` に1行追加 + commit)/
  onboard a new repo.
- **did = アイディアを棚に落とす**: 直前に出た案を、今いる repo の `docs/IDEAS.md` へ
  **詩**(散文でない1〜2文)で追記。仕様も手順も書かない / park the idea just raised as a
  poetic line or two — never prose, never in STATE.
  横断的な着想を `lowebbebb777/Ideas` へ集約する場合は明示的に指示すること /
  To deposit into the shared Ideas repo instead, say so explicitly.
