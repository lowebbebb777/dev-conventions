# LOG — セッション履歴 / Session History

---

## 2026-07-30 Antigravity (Gemini 3.6 Flash)

- やったこと: 省トークン・テスト駆動運用規約 (Zero-Token-Waste & TDD Rules) の追加、および `tools/ast_summary.py` (AST構造抽出) / `tools/mcp_state.py` (JSON構造化ステート) を共通ツールとして追加。
- 逸脱・追加・スキップ: なし
- 検証: ツールの単体実行およびテンプレ同期確認
- 申し送り: 全プロジェクトへ共通適用可能な最小トークン標準エコシステムとして管理。

---

## 2026-07-25 Antigravity

- やったこと: `AGENTS.md`, `docs/STATE.md`, `docs/LOG.md` の新規作成および dev-conventions のマルチエージェント標準化。
- 逸脱・追加・スキップ: なし
- 検証: ドキュメントおよびAI_KEY連携確認完了
- 申し送り: 今後の全リポジトリ標準テンプレートのマスターとして維持してください。

---

## 2026-07-28 Codex

- やったこと / Done: README「新規プロジェクトへの導入」に従い、SleepSoundOneを`projects.md`へ登録
- 逸脱・追加・スキップ / Deviations, additions, skips: なし
- 検証 / Verification: SleepSoundOne側の`AGENTS.md`、`docs/STATE.md`、`docs/LOG.md`存在確認、STATE 35行、Android tests 8/8・build成功
- 申し送り / Notes for next runner: SleepSoundOneの正典は`docs/android_audio_pipeline.md`、残作業の正は同repoの`docs/STATE.md`

---

## 2026-08-02 Codex

- やったこと / Done: `README.md`「新規プロジェクトへの導入」に従い、Ideasを`projects.md`へ登録。Ideas側はAGENTS/STATE/LOG、テンプレート、IDEA-001をGitHubへ反映済み。
- 逸脱・追加・スキップ / Deviations, additions, skips: ローカルパスは未固定のため`(clone先未固定)`と明記 — 理由: 一時作業ディレクトリを恒久パスとして登録しないため。
- 検証 / Verification: Ideas必須8ファイル・IDEA-001全13節・UTF-8表示 ✅ / `projects.md`のIdeas登録1件 ✅ / STATE 50行以内 ✅ / 指定unittest ❌（既存`tests/`不在）
- 申し送り / Notes for next runner: Ideasの正典は各`ideas/<slug>/IDEA.md`、残作業の正はIdeas側`docs/STATE.md`。dev-conventionsのテストコマンド不整合は残作業へ追加。

---

## 2026-08-02 Codex — `did`共通ショートカット

- やったこと / Done: `did`を「会話中の重要アイデアをIdeasへ登録・共有する」共通ショートカットとして、AGENTS・global-pointer・新規repoテンプレートへ追加。
- 逸脱・追加・スキップ / Deviations, additions, skips: なし。
- 検証 / Verification: 3つの入口で`did`定義一致 ✅ / STATE 50行以内 ✅ / 指定unittest ❌（既存`tests/`不在、既知制約）
- 申し送り / Notes for next runner: `di`は新規repo登録、`did`はIdeas登録。`did`単独指示では適用先プロダクトを実装しない。
