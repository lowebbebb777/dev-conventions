# ai_key — USB「AI_KEY」の Windows ツール & 引き継ぎ補助(非機密のみ)

このフォルダは USB「AI_KEY」に載せる**非機密の道具**の版管理コピー。
運用上の正本は Google Drive(と物理USB)。ここは新しいPCへ導入するための配布元。

## いちばん簡単な使い方(推奨)
USBを挿すと Explorer がルートを開く。そこの **`_START_HERE.txt`** を読むだけ。
特別な常駐やインストールは要らない。AI↔AIの引き継ぎ本体は各リポジトリの
`docs/STATE.md` / `docs/LOG.md`(git)で回っている。

## 中身
- `_START_HERE.txt` … USBルートに置く人間向けクイックスタート(平文)
- `_START_HERE.md` … 同内容の Markdown 版
- `03_RESUME.md` … AI用の引き継ぎ再開フロー(`AI_KEY/` 直下へ置く)
- `START.cmd` … ダブルクリックで手引きダイアログ(任意・ゼロインストール)
- `tools/` … (任意・実験的)挿入時に自動でメッセージを出す常駐ウォッチャー

## 自動ポップアップ(tools/)について — 既定オフ
挿入時の自動メッセージは**環境依存で不安定**(WindowsのUSB自動実行制限、
プロセスのドライブ可視性)。**基本は「Explorer + `_START_HERE.txt`」で十分**。
どうしても使いたい人向けに残してあるが、既定では入れない:
- `install_watcher.ps1`(スタートアップ登録・管理者不要)/ `uninstall_watcher.ps1`

## 機密は置かない
`ACTIVATION.txt`(物理トークン)・`manifest.sha256`・個人データはここに入れない。
それらは Google Drive / USB のみ。
