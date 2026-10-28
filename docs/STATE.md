# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-10-28 Antigravity (CLAUDE.md全削除・全AI用AGENTS.md一本化完了)

## 検証済みの事実

- 4ファイル構成 + 機械テスト + 規約自由化 + IDEAS棚grepタグ必須化 (2026-09-04)
- **全現存リポジトリの最新Headから CLAUDE.md を完全削除 & AGENTS.mdへ一本化** (2026-10-28):
  - `sleepsm`: `CLAUDE.md` 削除、思想・不変条件等を `AGENTS.md` へ完全統合 (テスト22件全緑)
  - `Sleep-Audio-AI`: 旧規約から最新規約へ更新、IDEAS棚新設、test_conventions配備 (テスト5件全緑)
  - `dev-conventions`, `SleepSoundOne`, `Runova`, `Facefusionkai`, `RanovaCLI`, `LLLM`: CLAUDE.md不在 & 機械チェック全緑を確認済み
  - 全8リポジトリで `CLAUDE.md` 削除・不在および `test_conventions.py` 全緑を一斉検証スクリプトで確認
- `dev-conventions`: `README.md` (CLAUDE.md削除・AGENTS.md一本化)、`projects.md` (sleepsm正典更新、Sleep-Audio-AI実体パス反映) を更新完了 (テスト8件全緑)

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## アイディア棚

`docs/IDEAS.md`(12件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. **`global-pointer.md` の再貼り付け** — 各AIのグローバル設定へ反映。**ユーザー作業**
2. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
3. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- Ideas repo はローカル未clone。到達性は remote 有りで通しているが中身は未検証

## 着手禁止

- なし
