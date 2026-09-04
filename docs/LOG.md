# LOG — セッション履歴 / Session History

---

## 2026-09-04 Claude Code (Opus 5) — IDEAS棚の取り出し口

- やったこと / Done: アイディア棚の retrieval を修正。棚の使い方は「着手前に関連語で grep、
  通読しない」と決まっているが、詩は grep の取っ手になる名詞をわざと削ぎ落とす形式のため、
  両者が噛み合っていなかった(実例: 「索引は、指した先が消えても平気な顔をしている」は
  `projects.md` の話をしながら `projects.md` を含まない)。**詩の外に具体語タグ2語以上**を
  必須化し、既存11件へ付与。`docs/IDEAS.md` / `templates/docs/IDEAS.template.md` の書式を更新し、
  `tests/test_conventions.py` と `templates/tests/test_conventions.template.py` に
  `IdeaShelf.test_every_entry_has_grep_tags` を追加(原則7: 散文の規約は守られない)。
  棚には今回の着想自体を12件目として追加した(`取っ手の無い詩は…`)。
- 逸脱・追加・スキップ / Deviations, additions, skips: 追加2件 —
  (a) テンプレ既存ルール「その分野の名詞を必ず1つ入れる」は既にあったが、詩の**内側**の
      抽象名詞1語では取っ手にならないため、詩の**外側**の具体語タグへ強化した(置換ではなく明確化)。
  (b) 配布テンプレ冒頭の「同じ4項目」を「5項目」に更新(テスト追加に伴う実数のずれ)。
  なお STATE が50行上限を超えたため、原則4に従い 07-25/07-28 の完了済み進捗2組を各1行へ集約した
  (履歴は本 LOG と git にある)。現在ちょうど50行。
- 検証 / Verification: `python -m unittest discover -s tests -p "test_*.py"` — **8件 緑**。
  逆検証: 1件からタグを剥がして `IdeaShelf` が FAILED になることを確認し、復元して緑に戻した。
  配布テンプレも別ディレクトリへコピーして単体で 5件緑 を確認済み。
- 申し送り / Notes for next runner: タグは**説明ではない**ので「説明を足したら作業」の線は
  越えない。詩は詩のまま置くこと。タグ語が「次走者が実際に打つ語」を当てられているかは、
  棚が50件規模になるまで判定できない(STATE 未検証項目)。そこで外していたら、
  タグ語彙のほうを直す — 詩を散文に戻さない。

---

## 2026-09-04 Claude Code (Opus 5)

- やったこと / Done: 規約の自由化。AIの能力を制限していた「省トークン・TDD規約」
  (2026-07-30 Antigravity 追加) を撤廃し「運用の指針」(既定値・逸脱可)へ置換、
  「自律範囲」節を新設。変更: `AGENTS.md` / `templates/AGENTS.template.md` /
  `templates/docs/STATE.template.md` / `README.md` / `~/.claude/commands/di.md`(repo外)。
  撤廃した制限 4件: ①報告5行以内 ②コード丸読みの禁止 ③`.state.json` による第二の状態源
  ④「完了=テストPASSのみ・PASSしたら即終了」。
  緩和: コミットメッセージの節番号必須→仕様がある時のみ、エージェント固有メモリの
  併用禁止→「そこだけに置かない」に限定、`di` の着手前ユーザー確認→推測+仮定明記で前進。
  追加: 自律範囲(確認なしで可/要確認の線引き)、STATE テンプレに「置いた仮定」節、
  「着手禁止」に解除条件欄。
- 逸脱・追加・スキップ / Deviations, additions, skips: **撤回1件・スキップ1件**。
  (a) 撤回: 当初 STATE の50行上限を「目安・超過可」へ緩める予定だったが、統合先(08-02)が
      溢れ先 `docs/IDEAS.md` を新設し、実測(登録4件中2件が超過・最大250行)を根拠に
      上限を機械テスト化していた。緩和の前提だった「削る動機になる」が解消済みのため撤回し、
      上限を維持。テンプレの文言も「溢れたら削るのでなく LOG/IDEAS へ移す」に変更した。
  (b) スキップ: SleepSoundSampler の旧規約追従は別repoへの変更のため本コミットに含めず、
      STATE 残作業#4に登録。
  また作業開始時のローカルは origin/main より8コミット遅れており、当初「バグ」として直した
  2件(「終了時の義務」の欠落 / 存在しない `tests/` を指すテストコマンド)は、いずれも
  08-02 に上流で独立に修正済みだった。上流版を採用し、自分の修正は破棄した。
  上流の原則2「緑より逆検証」は能力制限ではなく実失敗(中核がダミーのまま全緑)からの
  学習のため、維持した上で「テストを持てない領域は検証手順を書く」を重ねた。
  なお ChatGPT による Runova 分の未コミット変更が作業開始時に残っていたため同梱した。
- 検証 / Verification: `python -m unittest discover -s tests -p "test_*.py"` — **7件 緑**。
  逆検証: STATE.md に11行追加して上限テストが FAILED になることを確認し、復元して緑に戻した。
  併せて本体とテンプレの `##` 節構成が `diff` で一致することを確認。
- 申し送り / Notes for next runner: 「運用の指針」は既定値であって壁ではない — 外してよいが、
  外したらこの LOG に1行理由を書くこと。一方 `tests/` に落ちているもの(50行上限・索引の実在・
  必須ファイル)は既定値ではなく規則で、緩めるならテストごと変えること。
  既に登録済みの他repoは旧テンプレのコピーを持つため追従が要る(現状 SleepSoundSampler のみ、
  STATE 残作業#4)。

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

---

## 2026-08-02 Claude Code — origin/main とのマージ

- やったこと / Done: `origin/main`(Antigravity 07-30 の省トークン/TDD規約 + `tools/`、
  Codex 08-02 の Ideas登録 + `did`)と、ローカル5コミットをマージ。5ファイルの衝突を解決。
- 逸脱・追加・スキップ / Deviations, additions, skips:
  - **逸脱**: ユーザーの当初指示は「強制 push」だったが実行しなかった。リモートに
    他エージェントの未取得作業(規約2種・共通ツール2本・Ideas連携)があり、上書きすると
    消えるため中断して確認を取った。結果、マージ方針をユーザーが選択。
  - **判断(ユーザー裁定)**: `did` の定義が二重化していた。Codex版(`lowebbebb777/Ideas`
    へ登録)と本セッション版(repo内 `docs/IDEAS.md` へ詩)。**repo内版を正**とし、
    Ideas repo への集約は「明示指示があるとき」に限る、と各入口へ書き分けた。
  - **復元**: `AGENTS.md`「終了時の義務」を復活。07-30 のコミットで省トークン規約に
    置き換わって消えていたが、README 原則1〜4 と合言葉 `ds` が本節を参照しており、
    参照先が存在しない状態だった。
  - **統合**: TDD規約4「PASSのみを基準」に、README 原則2 の逆検証を但し書きとして追加。
    両者は排他ではなく、PASS が本物であることの担保が逆検証。
  - **変更**: 索引テストを「ローカル実在」から「**ローカルか remote のどちらかで辿れる**」
    へ緩和。Ideas は `(clone先未固定)` でローカル不在だが remote があり、正当な登録のため。
- 検証 / Verification: `python -m unittest discover -s tests -p "test_*.py"` — 7件 緑。
  Codex が残作業に挙げた「AGENTS のテストコマンドと `tests/` 不在の不整合」は本作業で解消。
- 申し送り / Notes for next runner:
  - `did` は**今いる repo の `docs/IDEAS.md`** へ詩で落とす。Ideas repo は明示指示時のみ。
  - `global-pointer.md` の再貼り付けはユーザー作業。未反映だと他エージェントに伝わらない。
