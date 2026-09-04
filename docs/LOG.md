# LOG — セッション履歴 / Session History

---

## 2026-09-04 Claude Code (Opus 5)

- やったこと / Done: 規約の自由化。AIの能力を制限していた「省トークン・TDD規約」
  (2026-07-30 Antigravity 追加) を撤廃し「運用の指針」へ置換、「自律範囲」節を新設。
  変更 5ファイル: `AGENTS.md` / `templates/AGENTS.template.md` /
  `templates/docs/STATE.template.md` / `README.md` / `~/.claude/commands/di.md`。
  撤廃した制限: ①報告5行以内 ②コード丸読みの禁止 ③`.state.json` による第二の状態源
  ④「完了=テストPASSのみ・PASSしたら即終了」。緩和: STATE 50行上限→目安、コミットメッセージの
  節番号必須→仕様がある時のみ、エージェント固有メモリの併用禁止→「そこだけに置かない」に限定、
  `di` の着手前ユーザー確認→推測+仮定明記で前進。追加: 自律範囲(確認なしで可/要確認の線引き)、
  STATE テンプレに「置いた仮定」節、「着手禁止」に解除条件欄。
- 逸脱・追加・スキップ / Deviations, additions, skips: 追加2件 —
  (a) `AGENTS.md` に欠落していた「終了時の義務」節を新設(`ds`/`dm` が「上記『終了時の義務』」を
      参照するのに本文に存在しないバグ。テンプレ側にしかなかった)。
  (b) ビルド・環境の記載を、存在しない `tests/` を指す `python -m unittest discover` から
      実在の検証手順へ差替え。理由: 旧規約「完了判定はテストPASSのみ」が本repo自身で
      満たせない状態だった。いずれもユーザー合意済み。
  スキップ1件 — SleepSoundSampler の旧規約追従は別repoへの変更のため本コミットに含めず、
  STATE の残作業#2に登録。
  なお ChatGPT による Runova 分の未コミット変更 (`docs/STATE.md` / `docs/LOG.md`) が
  作業開始時に残っていたため、内容を保持したまま本コミットに同梱した。
- 検証 / Verification: 自動テストなし(本repoは文書と小ツールのみ)。手順4点を実施し全てOK —
  ①`python tools/ast_summary.py tools` 実行成功 ②`python tools/mcp_state.py get` 実行成功・
  `.state.json` の副作用生成なし ③本体とテンプレの `##` 節構成が `diff` で一致
  ④旧規約文言の残骸 grep が LOG 以外0件。
- 申し送り / Notes for next runner: 「運用の指針」は既定値であって壁ではない。外してよいが、
  外したらこの LOG に1行理由を書くこと。既に登録済みの他repoは旧テンプレのコピーを持つため、
  規約を変えたら追従が要る(現状 SleepSoundSampler のみ該当、STATE 残作業#2)。

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

## 2026-08-05 ChatGPT

- やったこと / Done: Runova の「詳細設定」UIを追加し、config.yaml の重要度Sランク設定をGUIから編集可能にする実装を進行。`/api/config` の返却項目を拡張し、詳細設定のライト/ダークテーマ不一致を修正。
- 検証 / Verification: `tests/test_settings_dialog.py` 2件PASS。Runovaコミット: `acac1c1`（詳細設定のテーマと重要設定UIを整える）。
- 申し送り / Notes for next runner: `tests/run_tests.py` による全体回帰確認を実施し、詳細設定で未適用スタイルが残っていないか最終確認する。

---

## 2026-07-28 Codex

- やったこと / Done: README「新規プロジェクトへの導入」に従い、SleepSoundOneを`projects.md`へ登録
- 逸脱・追加・スキップ / Deviations, additions, skips: なし
- 検証 / Verification: SleepSoundOne側の`AGENTS.md`、`docs/STATE.md`、`docs/LOG.md`存在確認、STATE 35行、Android tests 8/8・build成功
- 申し送り / Notes for next runner: SleepSoundOneの正典は`docs/android_audio_pipeline.md`、残作業の正は同repoの`docs/STATE.md`
