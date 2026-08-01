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

## 省トークン・テスト駆動運用規約 (Zero-Token-Waste & TDD Rules)

1. **おしゃべり・前置き・丁寧すぎる解説の完全禁止**:
   - 会話や応答における無駄な挨拶や自己解説は行わず、**「変更点」と「テスト結果 (PASS/FAIL)」のみを最大 5 行以内で簡潔に報告**すること。
2. **コード丸読みの禁止と AST / 構造検索ツールの活用**:
   - コードベース構造の探索時は、`tools/ast_summary.py` や `grep_search` を優先利用し、ファイル全体の無用なテキスト流し込みを避けること。
3. **軽量構造化ステートマネージャー**:
   - 現在地や状態管理には `tools/mcp_state.py` (JSON `.state.json`) を活用し、長文テキストの無駄な読み込みを防止すること。
4. **テスト駆動 (TDD) 判定**:
   - タスクの完了判定は自動テストが PASS することのみを基準とする。
   - ただし **PASS だけでは根拠にならない**。新しいテストは**修正前のコードで FAIL する
     ことを確認**してから採用する(README 原則2)。緑のまま通るテストは、何も検証していない。

## 終了時の義務

<!-- 2026-07-30 のコミットで本節が省トークン規約に置き換わり削除されていたが、
     README 原則1〜4 と合言葉 ds が本節を参照しているため復活させた。 -->

1. **1 Step = 1 コミット**。メッセージに仕様の節番号。
2. `docs/STATE.md` を**上書き更新**。
3. `docs/LOG.md` に**1エントリ追記**。
4. `python -m unittest discover -s tests -p "test_*.py"` が緑であること(逆検証込み)。
5. エージェント固有メモリに repo の事実を置かない。
6. 今やらない案は `docs/IDEAS.md` に**詩**(散文でない1〜2文)。STATE には置かない(README 原則7)。

## ショートカット(合言葉)
- **ds = 引継ぎする**: `docs/STATE.md` を読んで「残作業」の最上位から着手。区切りでは上記「終了時の義務」に従う。
- **dm = 引継ぎ保存**: 今の途中経過を `docs/STATE.md`(現在地・次の一手)と `docs/LOG.md` に書いて commit。タスク途中で別AIへ渡す前の強制セーブ。
- **di = 引継ぎ登録**: 新規repoを規約に登録する合言葉。
- **did = アイディアを棚に落とす**: 直前に出た案を、今いる repo の `docs/IDEAS.md` へ
  **詩**(散文でない1〜2文)で追記する。仕様も手順も書かない。STATE には置かない。
  横断的な着想を `lowebbebb777/Ideas` へ集約したい場合は、その旨を明示して指示すること。
