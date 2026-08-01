# STATE — 現在地 / Current Position

**⚠️ テスト制約:** `python -m unittest discover -s tests -p "*.py"` は、リポジトリに `tests/` が存在せず失敗。今回の文書構造検証は成功。

最終更新 / Last updated: 2026-08-02 Codex @ 本コミット

## 検証済みの事実

- ドキュメント整備: `README.md`, `global-pointer.md`, `ai_key/` 整備完了 (2026-07-25)
- AI_KEY 連携: `F:\AI_KEY\` との構造・テンプレ共通化完了 (2026-07-25)
- SleepSoundOne: AGENTS/STATE/LOG導入と`projects.md`登録完了 (2026-07-28)
- 省トークン・TDDエコシステム: `tools/ast_summary.py` / `tools/mcp_state.py` 追加、AGENTS規約更新完了 (2026-07-30)
- Ideas: dev-conventions準拠文書とIDEA-001をGitHubへ保存し、`projects.md`登録完了 (2026-08-02)

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## 残作業(優先順)

1. AGENTS記載のテストコマンドと、存在しない`tests/`の不整合を解消
2. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
3. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- なし

## 着手禁止

- なし
