# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-10-29 dev-conventions v2 実装GPT (GitHub main反映・独立レビュー待ち)

## 検証済みの事実

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

`docs/IDEAS.md`(12件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. v2 の実clone環境で全件回帰と独立レビューを実施（未実施、ユーザーまたは指定レビュー担当）。
2. v2 の継続改良はユーザーの指示に従い、他repoへ自動展開しない。

3. **`global-pointer.md` の再貼り付け** — 各AIのグローバル設定へ反映。**ユーザー作業**
4. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
5. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- Ideas repo はローカル未clone。到達性は remote 有りで通しているが中身は未検証。
- 実GitHub mainの完全なローカルcloneによる回帰、独立レビュー、実機受入、他repo適用は NOT_RUN。

## 着手禁止

- なし
