# STATE — 現在地 / Current Position

最終更新 / Last updated: 2026-08-02 Claude Code @ 4d9231a (origin/main 9038ebe 系列とマージ)

## 検証済みの事実

- ドキュメント整備: `README.md`, `global-pointer.md`, `ai_key/` 整備完了 (2026-07-25)
- AI_KEY 連携: `F:\AI_KEY\` との構造・テンプレ共通化完了 (2026-07-25)
- SleepSoundOne: AGENTS/STATE/LOG導入と`projects.md`登録完了 (2026-07-28)
- 省トークン・TDDエコシステム: `tools/ast_summary.py` / `tools/mcp_state.py` 追加 (2026-07-30)
- Ideas: dev-conventions準拠文書とIDEA-001をGitHubへ保存し、`projects.md`登録完了 (2026-08-02)
- **4ファイル構成へ移行** (2026-08-02): `docs/IDEAS.md` を追加。1件＝**詩**(散文でない1〜2文)。
  分離基準は重要度でなく**アクセス頻度**(README §4ファイル構成)
- **`tests/` 新設で AGENTS のテストコマンド不整合を解消** (2026-08-02):
  `tests/test_conventions.py` — **7件 緑**。逆検証4件が全て赤になることを確認済み
- **`AGENTS.md`「終了時の義務」を復活** (2026-08-02): 07-30 のコミットで省トークン規約に
  置き換わり消えていたが、README 原則1〜4 と合言葉 `ds` が参照しているため復元

## ドキュメントの優先順位

矛盾時: `README.md` > `global-pointer.md` > `docs/STATE.md`

## アイディア棚

`docs/IDEAS.md`(11件)— **着手前に関連語で grep**。通読しない

## 残作業(優先順)

1. **`global-pointer.md` の再貼り付け** — `did`(= repo内 `docs/IDEAS.md` へ詩)と `IDEAS` を
   各AIツールのグローバル設定へ反映(`~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md` /
   Antigravity・Cursor の UI)。**ユーザー作業**
2. **Runova への規約適用** — `docs/IDEAS.md` 新設 + STATE を 250行→50行 へ削減 +
   `templates/tests/test_conventions.template.py` を導入。GPT の自己修復完了後に着手
3. **SleepSoundOne の STATE 65行を50行以下へ** — 同テンプレのテストを導入して機械的に維持
4. 新規プロジェクト作成時のプロンプト・CLI自動生成ツールの検討
5. AI_KEY ドングル自動同期スクリプトの強化

## 未検証項目

- **SmartSleepManager に `docs/STATE.md` が存在しない**。`projects.md` の正典欄は
  `CLAUDE.md` → `docs/STATE.md` を指しているが実体が無く、`ds` が空振りする
- **Ideas repo はローカル未clone**。索引の到達性テストは remote 有りで通しているが、
  中身(IDEA-001)は未検証

## 着手禁止

- なし
