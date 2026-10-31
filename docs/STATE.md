# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-10-31 GPT (オーナー呼称の明文化)

## 検証済みの事実
- 2026-10-31: ユーザー指示により呼称を「SoZOKさん／岡さん／師匠」に統一する修正を作業ブランチに記録。global-pointer.mdの差分を静的確認。main統合・各AIグローバル設定への貼付け・実clone全回帰はNOT_RUN。
- 2026-10-31: ユーザー承認で思想§15/COMMIT_ATTRIBUTION/全AI入口と名義検査・安全hook導入ツール/正負テスト追加。過去履歴無変更。他repo/PCへの適用と実cloneテストはNOT_RUN。
- 2026-10-31: オーナー承認で思想正本§14・AGENTS/テンプレ/グローバルポインタに「ユーザー価値・重複・捨てる仕事・忠告」ゲートを追加、did原文＋詩文2件。静的マーカー点検実施。実cloneのPython全回帰・独立レビューは NOT_RUN。
- 2026-10-30: didを発言者付き原文（逐語）＋詩文＋タグへ明示改定。静的整合確認済み、実clone回帰・独立レビューは NOT_RUN。

- 2026-10-29: ユーザー承認の Dynamic Role Assignment 8原則を思想正本第13節と AGENTS 実行規則へ追加。対象節の静的整合確認済み。実clone回帰・独立レビューは NOT_RUN。
- 4ファイル構成 + 機械テスト + 規約自由化 + IDEAS棚grepタグ必須化 (2026-09-04)
- **全現存リポジトリの最新Headから CLAUDE.md を完全削除 & AGENTS.mdへ一本化** (2026-10-28):
  - `sleepsm`: `CLAUDE.md` 削除、思想・不変条件等を `AGENTS.md` へ完全統合 (テスト22件全緑)
  - `Sleep-Audio-AI`: 旧規約から最新規約へ更新、IDEAS棚新設、test_conventions配備 (テスト5件全緑)
  - `dev-conventions`, `SleepSoundOne`, `Runova`, `Facefusionkai`, `RanovaCLI`, `LLLM`: CLAUDE.md不在 & 機械チェック全緑を確認済み
  - 全8リポジトリで `CLAUDE.md` 削除・不在および `test_conventions.py` 全緑を一斉検証スクリプトで確認
- `dev-conventions`: `README.md` (CLAUDE.md削除・AGENTS.md一本化)、`projects.md` (sleepsm正典更新、Sleep-Audio-AI実体パス反映) を更新完了 (テスト8件全緑)

- v2 の思想正本 `docs/DEVELOPMENT_PHILOSOPHY.md` を新設、README/AGENTS/配布テンプレ/機械テストを整合。
- 2026-10-29: 最新 main の主要6ファイルのblob SHAを照合した再構成環境で既存8件+追加6件=14件PASS。
- 修正前ソースに戻した逆検証と禁止ファイル混入の逆検証を実施。リモート全体の実cloneでの回帰は未実施。
- 2026-10-29: ユーザーの明示承認によりv2をGitHub mainへ直接反映（基準 `916943d`）。既存LOGと他ファイルを維持、force更新なし。

## ドキュメントの優先順位

権限・思想: `docs/DEVELOPMENT_PHILOSOPHY.md`。引継ぎ: `README.md` > `global-pointer.md` > `docs/STATE.md`

## アイディア棚

`docs/IDEAS.md`(14件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. v2 の実clone環境で全件回帰と独立レビューを実施（未実施、ユーザーまたは指定レビュー担当）。
2. Dynamic Role Assignmentを実開発で試行し、担当再割当・独立再検証・競合回避の事例と結果をLOGへ記録（実運用受入は未判定）。
3. v2 の継続改良はユーザーの指示に従い、他repoへ自動展開しない。

4. **`global-pointer.md` の再貼り付け** — 各AIのグローバル設定へ反映。**ユーザー作業**
5. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
6. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- Ideas repo はローカル未clone。到達性は remote 有りで通しているが中身は未検証。
- 実GitHub mainの完全なローカルcloneによる回帰、独立レビュー、実機受入、他repo適用は NOT_RUN。

## 着手禁止

- なし
