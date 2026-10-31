# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-11-01 GPT（DR1 Investment Gate v1.0設計PR作成）

## 検証済みの事実
- §16.4/§17を正本とするDR1専用投資審査の詳細設計案を作成。
- 配点8軸・100点、証拠等級E0-E4、独立した証拠強度、必須ゲートG0-G9を定義。
- DR1はCONDITIONAL GOなし。必須ゲート未達・証拠不足はGO不可。
- 専用記録テンプレートと静的テスト案を追加。
- 作業ブランチ: feature/dr1-investment-gate-v1-20261101。
- 本変更は設計案のみ。採点スクリプト、CI、rulesetは未実装。

## 文書の優先順位
思想: docs/DEVELOPMENT_PHILOSOPHY.md。詳細設計: docs/DR1_INVESTMENT_GATE_V1.md（未発効）。

## アイディア棚
docs/IDEAS.md — 着手前に関連語でgrep。通読しない。

## 残作業（優先順）
1. PR差分の独立レビュー・ユーザー確認・閾値の校正。
2. 設計承認後、採点スクリプト/JSON schema/負例テストを実装。
3. GitHub required check・ruleset・独立承認者を設定。
4. RevoAim DR1を新制度で再審査。現在の判定はPENDING。

## 未検証項目
- Python全回帰・新規テストの旧版FAIL逆検証はNOT_RUN。
- Claude独立レビュー・CI強制力・GitHub rulesetはNOT_RUN。
- 80点/証拠強度70点/一次証拠カバレッジ70%は設計初期値で、正式採用前の校正が必要。

## 着手禁止
- DR1 Investment Gate v1.0の正式運用・RevoAimへの採点適用（設計承認前）。
- 採点スクリプト/CIの実装（Phase Aの設計承認後）。
