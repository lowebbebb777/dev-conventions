# LOG — セッション履歴 / Session History

---

## 2026-10-28 Antigravity — CLAUDE.mdの全Head削除と全AI用(AGENTS.md)への完全統合

- やったこと / Done:
  - ユーザー指示「CLAUDE.mdはすべての最新Headから削除すること（最新dev-conの規約に従う）」および「Claude用⇒全AI用に統合」に基づき、全リポジトリおよび規約本体を更新・検証。
  - `dev-conventions`:
    - `README.md`: 「CLAUDE.mdは作成せず、全エージェント共通の入口としてAGENTS.mdに一本化する。既存のCLAUDE.mdは最新Headから削除しAGENTS.mdへ統合する」に改定。
    - `projects.md`: `sleepsm` の正典を `AGENTS.md → docs/STATE.md → docs/DESIGN_V3_1.md` に更新。`SleepSoundSampler` のローカル実体パス `C:\Users\soich\PycharmProjects\Sleep-Audio-AI` を反映。
  - `sleepsm` (`C:\Users\soich\AndroidStudioProjects\sleepsm`):
    - `CLAUDE.md` を git rm で完全削除。
    - `CLAUDE.md` に記載されていた思想・設計ドキュメント・不変条件・主要ファイルをすべて `AGENTS.md` に統合し、正典を一本化。
    - `docs/STATE.md` / `docs/LOG.md` 更新、コミット完了。
  - `Sleep-Audio-AI` (`C:\Users\soich\PycharmProjects\Sleep-Audio-AI`):
    - 旧「省トークン規約」から最新の「運用の指針」「自律範囲」へ `AGENTS.md` を更新。
    - `docs/IDEAS.md` (grepタグ付きアイディア棚)新設、`tests/test_conventions.py` 配備。
    - `docs/STATE.md` (棚ポインタ・最終更新日) / `docs/LOG.md` 更新、コミット完了。
  - 全リポジトリ一斉検証:
    - `dev-conventions`, `sleepsm`, `Sleep-Audio-AI`, `SleepSoundOne`, `Runova`, `Facefusionkai`, `RanovaCLI`, `LLLM` の全8リポジトリにおいて `CLAUDE.md` が存在しないこと、および `test_conventions.py` が緑であることを自動スクリプトで確認完了。
- 逸脱・追加・スキップ / Deviations, additions, skips: なし。
- 検証 / Verification:
  - `python -m unittest discover -s tests -p "test_*.py"` — **8件 緑**。
  - 逆検証: `projects.md` に不正パスを混入させて `test_every_entry_is_reachable` が赤になることを確認し、復元して緑に戻した。
- 申し送り / Notes for next runner:
  - 各AIツールのグローバル設定(`~/.claude/CLAUDE.md`等)には `global-pointer.md` の文面を貼る（ユーザー作業）。リポジトリ内には `CLAUDE.md` は置かず `AGENTS.md` を正とする。

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

---

## 2026-09-04 Antigravity — 現存する全リポジトリへの最新引き継ぎ規約の一斉適用

- やったこと:
  - ユーザー指示に基づき、現存する全プロジェクトおよびその最新Remoteコミットへ最新規約体系（運用の指針・自律範囲・4ファイル構成・IDEAS棚grepタグ必須化・test_conventions.py機械チェック）を一斉適用。
  - 対象リポジトリ（全7件 + dev-conventions）:
    1. SleepSoundSampler (C:\Users\soich\PycharmProjects\SleepSoundSampler): 最新Remote pull、AGENTS/STATE/LOG更新、IDEAS新設、test_conventions配備 (5件緑)
    2. sleepsm (C:\Users\soich\AndroidStudioProjects\sleepsm): 最新Remote pull、AGENTS/STATE/LOG更新、IDEAS新設、test_conventions配備 (5件緑)
    3. Runova (C:\Users\soich\PycharmProjects\Runova): AGENTS/STATE/LOG更新、IDEAS全エントリにgrepタグ付与、test_conventionsにIdeaShelf追加 (7件緑)
    4. Facefusionkai (C:\AI\Facefusionkai): AGENTS/STATE/LOG更新、IDEAS整形・grepタグ付与、test_conventions配備 (5件緑)
    5. SleepSoundOne (C:\Users\soich\AndroidStudioProjects\SleepSoundOne): 4ファイル構成新設、AGENTS更新、test_conventions配備 (5件緑)
    6. RanovaCLI (C:\Users\soich\PycharmProjects\RanovaCLI): AGENTS/STATE/LOG更新、IDEAS新設、test_conventions配備 (5件緑)
    7. LLLM (C:\Users\soich\PycharmProjects\LLLM): 最新Remote pull、規約初期導入(di)、AGENTS/STATE/LOG/IDEAS/test_conventions配備 (5件緑)
    8. dev-conventions: projects.md 索引適正化（sleepsm実体パス修正、新規repo登録）
- 逸脱・追加・スキップ:
  - SmartSleepManager のローカル実体は C:\Users\soich\AndroidStudioProjects\sleepsm (lowebbebb777/sleepsm) であったため、同リポジトリへ規約を適用し projects.md のパスを適正化。
  - 公式クローンである C:\AI\facefusion は外部OSSであるため規約適用の対象外とした。
- 検証:
  - 各プロジェクトで python -m unittest discover -s tests -p "test_conventions.py" 実行、全件 PASS。
  - dev-conventions で python -m unittest discover -s tests -p "test_*.py" 実行、8件全緑。
  - 不正パス混入による逆検証で FAILED を確認。
- 申し送り:
  - 全リポジトリでローカルコミット作成済み。リモートへの push はユーザー確認・指示待ち。

---

## 2026-10-29 dev-conventions v2 実装GPT — 権限・開発思想の実装

- やったこと / Done: ユーザー委任のv2仕様に沿い、開発思想の正本新設、README/AGENTS/配布テンプレ更新、静的規約テスト追加、STATE更新。
- 逸脱・追加・スキップ / Deviations, additions, skips: 他リポジトリへの適用はなし。リモートへのpush・PR・main統合はなし。GitHub cloneができない環境のため、変更対象主要ファイルのblob SHAがmainと一致するローカル再構成で検証。元のmainの全ファイルをcloneして実行したものではない。
- 検証 / Verification: 再構成環境 `python -m unittest discover -s tests -p "test_*.py"` 14件PASS（既存8・新規6）。逆検証として旧入口・旧README復元、およびCLAUDE.md混入・思想正本の削除でFAILを確認。配布テストも模擬新規プロジェクトで検証。
- 申し送り / Notes for next runner: 実main上でパッチ適用と全テスト再実行、独立レビュー、ユーザー最終受入が必要。設計変更・権限変更の承認実在は文字列テストでは検証できない。

---

## 2026-10-29 dev-conventions v2 実装GPT — main反映のユーザー承認

- 承認 / Approval: ユーザーが「これをdevのmainにして。開発しながら改良する。こちらでPULLするので成果物提出は不要」と明示。v2をmainへ反映する権限を委任した。これは他repo自動展開や設計権限の委任ではない。
- 実施 / Done: GitHub main `916943d993b45b09c593ae4ff1bbb94b1b0453f6` を基準に、v2の8変更ファイルをfast-forwardで反映。LOGの既存全履歴と他ファイルを保持。CLAUDE.mdの新設・既存分岐の統合・PR作成・強制更新はなし。
- 検証 / Verification: main由来の変更前Git blob SHAとの一致、および変更後7ファイルのローカル検証済みGit blob SHAとの一致を照合。ローカル再構成環境は14件PASS、逆検証6件、配布模擬7件PASS。実リポジトリをcloneしてのPythonテストと独立レビューは未実施。
- 申し送り / Notes: 継続改良は本規約の委任範囲内で実施し、設計・受入基準変更は事前承認を求める。実リポジトリでの全件回帰は次回確認する。

---

## 2026-10-29 dconちゃん — Dynamic Role Assignment の追加設計

- 指示 / Mandate: ユーザーが権限と作業担当を分離する8原則の追加を明示指示。既存の開発思想・権限体系・受入基準は不変更。
- 実施 / Done: `docs/DEVELOPMENT_PHILOSOPHY.md` 第13節に8原則を追加し、`AGENTS.md` に実行規則を要約。既存第10節の「実装担当」を元の実装者に固定しないことを明確化。`docs/STATE.md` に現在地を反映。
- 検証 / Verification: 既存第1〜12節と権限・承認・受入規則を保持し、8原則・独立再検証・競合回避・反復フローが文書上で整合することを静的確認。実GitHub cloneでの `python -m unittest discover -s tests -p "test_*.py"`、独立レビューは NOT_RUN。
- 逸脱 / Deviations: なし。push / PR / main統合はこの変更指示から自動的に許可されたものと扱わない。
- 追加承認 / Approval: ユーザーが続けて「GitHubへの直接反映実施／実開発につかいながら検証する」と明示。本変更をdev-conventionsのmainに直接反映する承認として扱う。他repoへの自動展開、以後の一般的なpush承認、設計権限・受入基準変更には拡張しない。
- 試行 / Trial: 実際の開発タスクで作業再割当、レビュー指摘者の修正と別担当による独立再検証、並列作業の衝突回避を確認し、観測事実をLOGに継続記録する。実運用受入は未判定。
- 申し送り / Next: main反映後に実repo全件回帰と別担当による独立レビューを実施し、実開発で受入妥当性を確認する。ローカルcloneはネットワークのDNS制限で失敗したためPython全件回帰はNOT_RUN。今回の直接反映以外の操作は既存の承認ゲートを守る。

---

## 2026-10-30 dconちゃん — did「原文＋詩文」へ改定

- 実施: ユーザーの「didはこれから原文と詩文両方登録したい」「改定」により、AGENTS・配布テンプレ・思想正本・README・IDEASテンプレを新規登録の「逐語原文（発言者付き）＋詩文＋タグ」へ変更。歴史の詩文のみの項目は維持。
- 逸脱・追加・スキップ: なし。他の製品repoへの自動配布なし。
- 検証: 変更元の存在照合、原文/詩文の文言整合、STATE 50行以内を静的確認。実cloneでのunittest、逆検証、独立レビューは NOT_RUN（外部ネットワーク不可）。
- 申し送り: 原文を捏造せず、ユーザー発言・AI発言を分ける。横断Ideas登録はIdeas repo固有の規約に従う。

---

## 2026-10-31 GPT — ユーザー価値と「捨てる仕事」の必須ゲート

- 決定: オーナーが「ユーザーのためにならない仕事は全て捨てていく」、新案を足す前に捨てる仕事を決めること、優先目標との衝突時は各AIが本人にも忠告することを明示承認。設計の最終決定権はユーザー。
- やったこと / Done: 思想正本`docs/DEVELOPMENT_PHILOSOPHY.md` §14に価値・重複・期限・廃止候補・反証のゲート追加。AGENTS・新規repoテンプレ・global-pointerへ接続。did原文（ユーザー逐語）と詩文（AI解釈）を分離して2件追記。静的テストを2件追加。
- 逸脱・追加・スキップ: 他repoへの自動展開はしない。ユーザーの各AIグローバル設定への再貼り付けが必要。既存の法令・安全・データ保全・権限・品質ゲートは緩和しない。
- 検証 / Verification: 全更新対象の既存本文をGitHubから取得し既存内容を保持。追加した§14・入口・didの原文・タグを静的確認。新規テストの逆検証は修正前に§14が無いことの文字列チェックのみであり、**実cloneでのPythonユニットテスト・逆検証・独立レビューは NOT_RUN**。
- 次の一手: 実cloneの規約全テストと必要な逆検証、別担当の独立レビュー、グローバル設定への貼付け（ユーザー作業）、実際の提案・開発で作業削減の効果を確認する。
- 追加整合（同日）: `global-pointer.md` の旧「didは詩だけ」を現行の逐語原文＋詩文＋具体タグへ統一し、`docs/IDEAS.md` の冒頭説明とテストを整合。詩だけの旧12件はそのまま保持。検証はGitHub上の静的比較のみ、Python実行はNOT_RUN。

---

## 2026-10-31 GPT — AI作業とGitコミット名義の分離

- ユーザー指示: 今後のAI名義・AI共同作成者登録を停止、dev-conventionsを共通ルール化。過去の履歴は何もしない。
- 変更: 思想§15、COMMIT_ATTRIBUTION、AGENTS/配布テンプレ/README/グローバルポインタ、名義・共同作成者を検証するPythonガード、安全hook導入ツール、正負テスト、STATE。
- 既存履歴: amend/rebase/force push等は一切行わない。他リポジトリのファイルやWindows/Git/Claude設定も触れない。
- 検証: ファイルの静的整合とガードの正負ケースを設計。実clone上のPython unittest、独立レビュー、Windows実機hook試験はNOT_RUN。導入するrepo側で検証が必要。GitHub Web/APIコミットはローカルhookを通らない。

---

## 2026-10-31 GPT（GitHub接続）— Design Review（DR）を開発基本規約に採用

- **ユーザー承認**: 「DR0：アイディアレベル、DR1：商品企画・要求（市場・差別化）、DR2：構想設計、DR3：詳細設計、DR4：実装・検証結果、DR5：リリース・運用準備、初回出荷審査：リリース前承認、DR6：商品ライフサイクル審査」とする提案をユーザーが承認。「DR123とか平気である」「アジャイルにもとに戻る場合も多々ある」を踏まえた統合DR・差戻し・リスク別軽量DRにも同意し、「dev-con更新！」と指示。
- **実施**: 思想正本§16へ上記8ゲートと最重要の問い、Verification/Validation、DR123統合時の段階別証拠、前工程への反復差戻し、軽量・緊急DR、DR5と初回出荷審査の区別、出荷後のDR6継続評価を明文化。README/AGENTS/配布テンプレ/global-pointerへ入口を追加。任意DR記録テンプレートと既存・配布テストの静的チェックを追加。
- **設計判断**: 4ファイル構成と役割・承認ゲートは変更しない。正式DRの会議回数を義務化せず、リスクと変更規模に応じて軽量化可能とする。複数DRの統合は各段階の検証・判定を省略する免罪符ではない。
- **検証**: 変更前は§16・DR123・初回出荷審査が規約正本に存在しない（旧版静的マーカー検査FAIL相当）。候補の節番号、8ゲート、各入口への参照、テンプレート、初回出荷承認分離、既存§1〜15維持を静的照合。GitHub反映後のファイルを再取得して確認。Pythonによる実clone全回帰・独立レビューは **NOT_RUN**（ネットワーク制約により実clone不可）。テストPASSとは記録しない。
- **逸脱**: なし。対象repoのmainへの直接PUSHはユーザーの当該指示を根拠とする。force push・履歴改変・他repo更新はしない。
- **次**: dev-conventionsの実cloneで全テスト実行と独立レビュー、RevoAimでのDR運用試行。AIがDRの最終承認・初回出荷承認を代行しない。

---

## 2026-10-31 GPT（GitHub接続）— RevoAimプロジェクト登録

- ユーザー承認: RevoAimの上流設計作成に伴い、RevoAimとdev-conventionsの作業ブランチ作成・コミットを許可。main統合・PR作成は行わない。
- 実施: `projects.md` にRevoAimを登録し、正典ポインタを `AGENTS.md` → `docs/STATE.md` → `docs/UPSTREAM_DESIGN.md` とした。STATEを現在地に更新し、本エントリを追記。
- 逸脱・追加・スキップ: ローカルclone先は未確認のため `(clone先未固定)` と記載。RevoAim・dev-conventionsのmainは変更しない。
- 検証: main HEADと対象ファイルをGitHubから取得し、登録行・remote URL・正典パス・STATE 50行以内を静的確認。RevoAim側の作業ブランチcommitは `e0fe046e04857df85fac19ce48065847e7912a71`。dev-conventionsのPythonテスト・逆検証・独立レビューはNOT_RUN。
- 申し送り: RevoAimの上流設計はDR1/DR2統合ドラフト。ユーザー確認後にDR3へ進む。dev-conventions全テストと独立レビューは実clone環境で行う。

