# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-09-04 Claude Code @ 9038ebe (この更新のcommitは本行の次)

## 検証済みの事実

- ドキュメント整備: `README.md`, `global-pointer.md`, `ai_key/` 整備完了 (2026-07-25)
- AI_KEY 連携: `F:\AI_KEY\` との構造・テンプレ共通化完了 (2026-07-25)
- SleepSoundOne: AGENTS/STATE/LOG導入と`projects.md`登録完了 (2026-07-28)
- 規約の自由化 (2026-09-04): 「省トークン・TDD規約」(2026-07-30版)を「運用の指針」へ置換し、
  「自律範囲」節を新設。検証手順 = ① `python tools/ast_summary.py tools` 実行OK
  ② `python tools/mcp_state.py get` 実行OK・`.state.json` 生成なし
  ③ `diff <(grep -o '^## [^ /(]*' AGENTS.md) <(... templates/AGENTS.template.md)` で節構成一致
  ④ `grep -rn "省トークン|丸読み|5 行以内|即座にコミットして終了" --include=*.md .` が LOG 以外0件
- 既存バグ2件の是正 (2026-09-04): AGENTS.md に欠落していた「終了時の義務」節を追加
  (`ds`/`dm` の参照先が復旧)。存在しない `tests/` を指していたテストコマンドを実在の検証手順に差替え。
- Runova: 「詳細設定」UIを追加し、config.yaml重要度Sランク項目のGUI編集対応を進行中。`/api/config`返却項目を拡張済み。ライト/ダークテーマの統一を修正し、`tests/test_settings_dialog.py` は2件PASS、Runovaコミット `acac1c1`。残作業は `tests/run_tests.py` による全体回帰確認と未適用テーマの最終確認。

## 置いた仮定

- dev-conventions 自身の「検証」は自動テストではなく上記の手順4点とする — 根拠: 本repoは
  文書と小ツールのみでテスト対象のロジックを持たないため。テストを足すならこの節を差し替える。

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## 残作業(優先順)

1. Runova: 「設定」に「詳細設定」を設け、config.yaml の重要度Sランク項目をすべてGUIから設定可能にする。テーマ（ライト/ダーク）と完全に統一し、未適用スタイルを解消する。server.py の /api/config も対応項目を漏れなく返すことを維持する。最後に tests/run_tests.py で回帰確認する。
2. SleepSoundSampler の `AGENTS.md` を新テンプレへ追従(旧「省トークン・TDD規約」が残存。
   `C:\Users\soich\PycharmProjects\SleepSoundSampler\AGENTS.md`)。他3repo(SmartSleepManager /
   SleepSoundOne / CloudCodeEX)には旧規約なし=対応不要。CloudCodeEX はローカルパス自体が要確認。
3. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
4. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- 新「自律範囲」節が各AI(Codex / Antigravity / Cursor)で意図通り効くかは未検証。
  実運用で「確認が多すぎる/少なすぎる」が出たら境界を STATE 経由で調整する。

## 着手禁止

- なし
