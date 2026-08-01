# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-08-02 Claude Code @ 810895a

## 検証済みの事実

- ドキュメント整備: `README.md`, `global-pointer.md`, `ai_key/` 整備完了 (2026-07-25)
- AI_KEY 連携: `F:\AI_KEY\` との構造・テンプレ共通化完了 (2026-07-25)
- SleepSoundOne: AGENTS/STATE/LOG導入と`projects.md`登録完了 (2026-07-28)
- **4ファイル構成へ移行** (2026-08-02): `docs/IDEAS.md` を追加。1件＝詩的な1文。
  分離基準は重要度でなく**アクセス頻度**(README §4ファイル構成)
- **規約の機械チェック新設** (2026-08-02): `tests/test_conventions.py` — **7件 緑**。
  `python -m unittest discover -s tests -p "test_*.py"`。
  逆検証4件(棚ポインタ削除 / 不在パス / 51行 / テンプレの逆検証記述削除)が全て赤になることを確認済み
- **合言葉に `did` 追加** (2026-08-02): 案を `docs/IDEAS.md` へ詩1文で落とす

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## アイディア棚

`docs/IDEAS.md`(10件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. **`global-pointer.md` の再貼り付け** — `did` と `IDEAS` を各AIツールのグローバル設定へ反映
   (`~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md` / Antigravity・Cursor の UI)。**ユーザー作業**
2. **Runova への規約適用** — `docs/IDEAS.md` 新設 + STATE を 250行→50行 へ削減 +
   `templates/tests/test_conventions.template.py` を導入。GPT の自己修復完了後に着手
3. **SleepSoundOne の STATE 65行を50行以下へ** — 同テンプレのテストを導入して機械的に維持
4. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
5. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- **SmartSleepManager に `docs/STATE.md` が存在しない**。`projects.md` の正典欄は
  `CLAUDE.md` → `docs/STATE.md` を指しているが実体が無く、`ds` が空振りする

## 着手禁止

- なし
