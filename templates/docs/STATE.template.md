# STATE — 現在地 / Current Position

<!-- 常に上書き。1画面(50行)以内。歴史を書かない(→ LOG.md)。
     Always overwritten. One screen (≤50 lines). No history here (→ LOG.md). -->

最終更新 / Last updated: YYYY-MM-DD <エージェント名 / agent> @ <git HEAD 短縮ハッシュ / short hash>

## 検証済みの事実 / Verified Facts

- ビルド / Build: `<command>` ✅/❌ (YYYY-MM-DD)
- テスト / Tests: `<command>` — N件 / N tests, 緑/赤 green/red (YYYY-MM-DD)
- <バージョン事実 / version facts: DBスキーマ、API版数など schema versions, API levels, ...>

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

<!-- ユーザー指示待ちのもの。Items awaiting explicit user instruction. -->

- <項目 / item> — 理由 / reason
