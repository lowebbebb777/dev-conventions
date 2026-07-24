# AGENTS.md — dev-conventions エージェント共通ルール

全エージェント(Codex / Antigravity / Claude Code / Cursor)共通の入口。
**このファイルには「今やること」を書かない**(陳腐化するため)。現在地は `docs/STATE.md`。

## 読む順番

1. `README.md` — dev-conventions 思想・全体構造(最優先)
2. `docs/STATE.md` — 現在地と残作業
3. `global-pointer.md` / `templates/` — ポインター・テンプレート正典
4. `docs/LOG.md` — 経緯と判断理由

## ビルド・環境(Windows)

```powershell
python -m unittest discover -s tests -p "*.py"
```

## 不変条件

正は `README.md` および `global-pointer.md`。

## 終了時の義務

1. **1 Step = 1 コミット**。メッセージに仕様の節番号。
2. `docs/STATE.md` を**上書き更新**。
3. `docs/LOG.md` に**1エントリ追記**。
4. **`python F:\AI_KEY\90_INTEGRITY\sync_aikey.py` を実行**し、Google Drive (正本) ⇄ USB (写し) の自動同期とハッシュマニフェスト再生成を行う。
5. エージェント固有メモリに repo の事実を置かない。
