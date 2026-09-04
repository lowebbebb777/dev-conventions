# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-09-04 Claude Code @ a566051 (IDEAS棚に grep タグを導入)

## 検証済みの事実

- 文書整備 + AI_KEY (`F:\AI_KEY\`) 構造・テンプレ共通化 完了 (2026-07-25)
- `projects.md` 登録完了: SleepSoundOne (2026-07-28) / Ideas + IDEA-001 (2026-08-02)
- **4ファイル構成へ移行** (2026-08-02): `docs/IDEAS.md` 追加。分離基準はアクセス頻度(README §4ファイル構成)
- **`tests/` 新設** (2026-08-02): `tests/test_conventions.py` — 逆検証4件が赤になることを確認済み
- **規約の自由化** (2026-09-04): 「省トークン・TDD規約」→「運用の指針」(既定値・逸脱可)、
  「自律範囲」節を新設。撤廃= 報告5行上限 / 丸読み禁止 / `.state.json` / 「完了=PASSのみ・即終了」。
  逆検証(原則2)と50行上限は**維持**(機械テストが正)
- **IDEAS棚に grep タグを導入** (2026-09-04): 詩は grep 語を削ぎ落とすため棚の取り出し口と
  噛み合っていなかった。具体語タグ2語以上を必須化・既存11件へ付与し `IdeaShelf` で機械強制。
  検証: `python -m unittest discover -s tests -p "test_*.py"` **8件 緑**、タグ剥がしで FAILED 確認

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## 置いた仮定

- 行数上限は緩めず維持 — 根拠: 溢れ先(`IDEAS.md`)と実測(4件中2件超過・最大250行)があり、
  「上限が情報を削らせる」懸念は解消済みと判断

## アイディア棚

`docs/IDEAS.md`(12件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. **`global-pointer.md` の再貼り付け** — `did` / `IDEAS` / 「自律範囲」を各AIのグローバル設定へ
   反映(`~/.claude/CLAUDE.md` 他)。**ユーザー作業**
2. **Runova への規約適用** — `docs/IDEAS.md` 新設 + STATE 250行→50行 + テストテンプレ導入
3. **SleepSoundOne の STATE 65行を50行以下へ**
4. **SleepSoundSampler の `AGENTS.md`** に旧「省トークン・TDD規約」が残存。新テンプレへ追従
5. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
6. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- **SmartSleepManager に `docs/STATE.md` が無い**。`projects.md` は指すが実体が無く `ds` が空振る
- **Ideas repo はローカル未clone**。到達性は remote 有りで通しているが中身は未検証
- 新「自律範囲」が各AIで意図通り効くかは未検証。確認の多寡が出たら境界を調整する
- タグ語が「次走者が打つ語」を当てているかは、棚が50件規模になるまで判定できない

## 着手禁止

- なし
