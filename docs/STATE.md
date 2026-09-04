# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-09-04 Antigravity (全現存リポジトリへの最新規約適用完了)

## 検証済みの事実

- 文書整備 + AI_KEY (`F:\AI_KEY\`) 構造・テンプレ共通化 完了 (2026-07-25)
- 4ファイル構成 + 機械テスト + 規約自由化 + IDEAS棚grepタグ必須化 (2026-09-04)
- **全現存リポジトリへの最新規約適用完了** (2026-09-04):
  - `SleepSoundSampler`: 最新Remote pull、規約更新、テスト5件全緑
  - `sleepsm` (SmartSleepManager): 最新Remote pull、規約更新、テスト5件全緑
  - `Runova`: AGENTS更新、IDEAS棚タグ付与、テスト7件全緑
  - `Facefusionkai`: AGENTS更新、IDEAS棚タグ整形、テスト5件全緑
  - `SleepSoundOne`: 4ファイル構成新設、AGENTS更新、テスト5件全緑
  - `RanovaCLI`: 4ファイル構成新設、AGENTS更新、テスト5件全緑
  - `LLLM`: 4ファイル構成新設(`di`)、AGENTS更新、テスト5件全緑
  - 各repoで `test_conventions.py` による機械チェック全緑を確認済み
- `projects.md` 索引適正化 (sleepsmパス修正、新規登録完了、到達性テスト緑・逆検証確認)

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## アイディア棚

`docs/IDEAS.md`(12件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. **`global-pointer.md` の再貼り付け** — `did` / `IDEAS` / 「自律範囲」を各AIのグローバル設定へ
   反映(`~/.claude/CLAUDE.md` 他)。**ユーザー作業**
2. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
3. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- **Ideas repo はローカル未clone**。到達性は remote 有りで通しているが中身は未検証
- 新「自律範囲」が各AIで意図通り効くかは未検証。確認の多寡が出たら境界を調整する

## 着手禁止

- なし

