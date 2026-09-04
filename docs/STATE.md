# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-09-04 Claude Code @ 5e07bdb (規約自由化を統合)

## 検証済みの事実

- ドキュメント整備: `README.md`, `global-pointer.md`, `ai_key/` 整備完了 (2026-07-25)
- AI_KEY 連携: `F:\AI_KEY\` との構造・テンプレ共通化完了 (2026-07-25)
- SleepSoundOne: AGENTS/STATE/LOG導入と`projects.md`登録完了 (2026-07-28)
- Ideas: dev-conventions準拠文書とIDEA-001をGitHubへ保存し、`projects.md`登録完了 (2026-08-02)
- **4ファイル構成へ移行** (2026-08-02): `docs/IDEAS.md` 追加。分離基準はアクセス頻度(README §4ファイル構成)
- **`tests/` 新設** (2026-08-02): `tests/test_conventions.py` — 逆検証4件が赤になることを確認済み
- **規約の自由化** (2026-09-04): 「省トークン・TDD規約」を「運用の指針」(既定値・逸脱可)へ置換し
  「自律範囲」節を新設。撤廃= 報告5行上限 / コード丸読みの禁止 / `.state.json` の第二状態源 /
  「完了=PASSのみ・即終了」。逆検証(原則2)と50行上限は**維持**(機械テストが正)。
  検証: `python -m unittest discover -s tests -p "test_*.py"` **7件 緑**

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## 置いた仮定

- 行数上限は緩めず維持 — 根拠: 溢れ先(`IDEAS.md`)と実測(4件中2件超過・最大250行)があり、
  「上限が情報を削らせる」懸念は解消済みと判断

## アイディア棚

`docs/IDEAS.md`(11件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. **`global-pointer.md` の再貼り付け** — `did` / `IDEAS` / 新設「自律範囲」を各AIツールの
   グローバル設定へ反映(`~/.claude/CLAUDE.md` 他)。**ユーザー作業**
2. **Runova への規約適用** — `docs/IDEAS.md` 新設 + STATE 250行→50行 + テストテンプレ導入
3. **SleepSoundOne の STATE 65行を50行以下へ**
4. **SleepSoundSampler の `AGENTS.md`** に旧「省トークン・TDD規約」が残存。新テンプレへ追従
5. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
6. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- **SmartSleepManager に `docs/STATE.md` が無い**。`projects.md` は指すが実体が無く `ds` が空振る
- **Ideas repo はローカル未clone**。索引の到達性は remote 有りで通しているが中身は未検証
- 新「自律範囲」が各AIで意図通り効くかは未検証。確認の多寡が出たら境界を調整する

## 着手禁止

- なし
