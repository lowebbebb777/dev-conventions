# STATE — 現在地 / Current Position

<!-- 常に上書き。1画面(50行)以内(tests が落とす)。溢れたら削るのではなく移す:
     歴史は LOG.md、今やらない案は IDEAS.md。毎回読まれるファイルに、たまにしか
     要らないものを置くと全エージェントが毎セッション運搬費を払う。
     Always overwritten; ≤50 lines (enforced by tests). On overflow, move rather than
     delete: history to LOG.md, not-now ideas to IDEAS.md. -->

最終更新 / Last updated: YYYY-MM-DD <エージェント名 / agent> @ <git HEAD 短縮ハッシュ / short hash>

## 検証済みの事実 / Verified Facts

<!-- テストが無い領域は「何をどう確かめたか」を手順ごと書く。それが完了の根拠になる。
     Where there are no tests, write the exact verification steps — that is the evidence of done. -->

- ビルド / Build: `<command>` ✅/❌ (YYYY-MM-DD)
- テスト / Tests: `<command>` — N件 / N tests, 緑/赤 green/red (YYYY-MM-DD)
- <テスト以外の検証 / non-test verification: 手順と結果 steps and result>
- <バージョン事実 / version facts: DBスキーマ、API版数など schema versions, API levels, ...>

## 置いた仮定 / Assumptions Made

<!-- 仕様の穴を既定値で埋めたら1行書く。次走者が覆せるように。
     One line per gap filled with a default, so the next runner can overturn it. -->

- <仮定 / assumption> — 根拠 / basis: <...>

## 文書の優先順位 / Doc Precedence

矛盾時 / On conflict: <A> > <B> > <C>。残作業一覧の正は本ファイル。
Canonical list of remaining work: this file.

## 残作業(優先順)/ Remaining Work (by priority)

1. <作業 / task> — 仕様: <文書 §節 / doc §section>
2. ...

## アイディア棚 / Idea Shelf

<!-- この1行は消さない。棚の存在を次走者に必ず気づかせるための唯一の仕掛け。
     Never delete this line: it is the only mechanism that makes the shelf discoverable. -->

`docs/IDEAS.md`(N件 / N entries)— **着手前に関連語で grep**。通読しない /
grep by keyword before starting; do not read it through.

## 未検証項目 / Unverified Items

<!-- 「完了と誤認すると事故る」ものだけ。Only items where mistaking them as done causes accidents. -->

- <項目と、何が検証されていないか / item and what exactly is unverified>

## 着手禁止 / Do Not Start

<!-- ユーザー指示待ちのものだけ。**解除条件を必ず書く**(書かないと永久凍結になる)。
     Only items awaiting explicit user instruction. **Always write the unblocking condition** —
     without one this list silently becomes a permanent freeze. -->

- <項目 / item> — 理由 / reason: <...> — 解除条件 / unblocked when: <...>
