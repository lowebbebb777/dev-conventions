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
python -m unittest discover -s tests -p "test_*.py"
```

規約の機械チェック(行数上限・索引の実在・必須ファイル)は `tests/test_conventions.py`。

## 不変条件

正は `README.md` および `global-pointer.md`。

## 終了時の義務

1. **1 Step = 1 コミット**。メッセージに仕様の節番号。
2. `docs/STATE.md` を**上書き更新**。
3. `docs/LOG.md` に**1エントリ追記**。
4. `python -m unittest discover -s tests -p "test_*.py"` が緑であること。
   新テストは**修正前コードで FAIL することを確認**してから緑にする(README 原則2)。
5. エージェント固有メモリに repo の事実を置かない。
6. 今やらない案は `docs/IDEAS.md` に**語＋手がかり1行**。STATE には置かない(README 原則7)。
