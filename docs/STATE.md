# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-10-28 ChatGPT (共通規約の単一正本化・作業ブランチ)

## 検証済みの事実
- 2026-09-04時点: 4ファイル構成(AGENTS/STATE/LOG/IDEAS)、IDEAS grepタグ2件以上、STATE 50行上限のテストが既存。過去の詳細はLOG。
- 2026-10-28: `AGENTS.md` を全AI共通の唯一の作業規約とし、`CLAUDE.md` を参照だけの互換入口とする文書・テンプレ・テストを作業ブランチへ記録。
- `README.md` に既存repo向け安全な移行順、`global-pointer.md` に全AI共通の同一案内文を記載。
- GitHubから変更ファイルを読み戻して内容・参照関係を確認（Windows上の実行テストではない）。

## ドキュメントの優先順位
- 全AI共通の作業規約: `AGENTS.md`。背景・導入方針: `README.md`。
- 現在地・残作業: **本 `docs/STATE.md` が唯一の正**。履歴: `docs/LOG.md`。
- `CLAUDE.md` / `global-pointer.md` は案内用。独立した規約を置かない。

## 置いた仮定
- AIごとの自動読込ファイル名は互換のため残すが、行動規則は一本化する。各ツールのグローバル設定は勝手に変えない。

## アイディア棚
`docs/IDEAS.md`（12件、既存）— 着手前に関連語でgrep。通読しない。

## 残作業(優先順)
1. このブランチで `python -m unittest discover -s tests -p "test_*.py"` を実行し、元の8件と追加3件、テンプレの回帰を確認する（現会話のGitHub接続では実行不可）。
2. 規約統一の内容をユーザーがレビュー後、mainへの取り込みを判断する（未マージ）。
3. 既存repoの `CLAUDE.md` 独自記載を棚卸し、AGENTSへ統合してからポインターにする。SleepSM等への変更は個別に実施し、勝手に上書きしない。
4. 各AIのグローバル設定を新しい `global-pointer.md` へ必要に応じ更新（ユーザー操作が必要）。
5. 既存残件: Runova規約適用、SleepSoundOne STATE行数、SleepSoundSampler旧規約、新規repo導入補助、AI_KEYドングル強化。

## 未検証項目
- Python unittestの実行結果と既存repoにおけるAIの読み込み挙動。
- 旧来の未検証: SmartSleepManagerのSTATE不在、Ideas未clone、一部規約の実際の遵守、IDEASタグの有効性。

## 着手禁止
- 既存プロジェクトのAGENTS/CLAUDEを、内容移管・安全確認なしに一括置換しない。
