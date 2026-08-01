# LOG — セッション履歴 / Session History

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

## 2026-08-02 Claude Code

- やったこと / Done:
  - README §4ファイル構成 — 3ファイル→**4ファイル**。`docs/IDEAS.md`(アイディア棚)を追加。
    1件＝**情報量を含んだ詩的な1文**。分離基準は重要度でなく**アクセス頻度**
  - README §原則2 — 「散文よりテスト」に**逆検証**を追加。緑だけでは「本物のテスト」と
    「何も検証していないテスト」を区別できない(Runova で中核が両端ダミーのまま全緑だった実例)
  - README §原則7(新設) — 規約自身にも原則2を適用する
  - `tests/test_conventions.py`(新設) — 必須ファイル / STATE 50行上限 / 最終更新行 /
    棚へのポインタ / `projects.md` のパス実在 / テンプレの整合、計7件
  - `templates/tests/test_conventions.template.py`(新設) — 各repoへのドロップイン版
  - `templates/docs/IDEAS.template.md`(新設)、STATE テンプレに「アイディア棚」1行を追加
  - 合言葉 **`did` = アイディアを棚に落とす**(詩1文で `docs/IDEAS.md` へ追記)を
    `global-pointer.md` と `templates/AGENTS.template.md` に追加
  - `projects.md` — **Runova を登録**。**CloudCodeEX を削除**(ローカル実体が消滅)
- 逸脱・追加・スキップ / Deviations, additions, skips:
  - **追加**: `global-pointer.md` に「ショートカット」節を新設。従来この節は
    `~/.claude/CLAUDE.md` にだけ存在し、正本であるはずの `global-pointer.md` に無かった
    (二重管理の逆転)。`did` 追加を機に正本側へ寄せた
  - **スキップ**: 他repo(Runova 250行 / SleepSoundOne 65行)の STATE 行数超過は未修正。
    dev-conventions からは強制できないため、各repoへテンプレのテストを導入する形に分割
  - **判断**: 「1件＝語ひとつ」から「1件＝詩的1文」へ設計変更(ユーザー指示)。裸の語は
    記憶を共有しない別エージェントが復元できないが、1文なら関係が入るため両立する
- 検証 / Verification: `python -m unittest discover -s tests -p "test_*.py"` — **7件 緑**。
  **逆検証4件すべて赤を確認**(原則2): 棚ポインタ削除→`test_points_at_idea_shelf`、
  不在パス混入→`test_registered_paths_exist`、STATE を51行超→`test_within_line_cap`、
  テンプレから逆検証記述を削除→`test_agents_template_mentions_negative_verification`。
  破壊は try/finally で必ず復元し、復元後の再走で7件緑に戻ることも確認
- 申し送り / Notes for next runner:
  - **`global-pointer.md` の再貼り付けはユーザー作業**。各AIツールのグローバル設定を
    更新しないと `did` は他エージェントに伝わらない
  - 棚は**種であって記録ではない**。決定・制約・実測値は詩にせず STATE/LOG に置く
    (再構成は生成なので、それらしい別物が返る)
  - Runova への適用は GPT の自己修復完了後。同repoは現在 `tests/test_webui_chat.py` が未コミット
