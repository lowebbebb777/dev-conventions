# ai_key — USB「AI_KEY」の Windows ツール & 引き継ぎ補助(非機密のみ)

このフォルダは USB「AI_KEY」に載せる**非機密の道具**の版管理コピー。
運用上の正本は Google Drive(と物理USB)。ここは新しいPCへ導入するための配布元。

## 中身
- `_START_HERE.md` … USBルートに置く人間向けクイックスタート
- `START.cmd` … ダブルクリックで手引きダイアログ(ゼロインストール)
- `03_RESUME.md` … AI用の引き継ぎ再開フロー(`AI_KEY/` 直下へ置く)
- `tools/`
  - `show_message.ps1` … Windowsメッセージ(MessageBox)表示
  - `watch_aikey.ps1` … ラベル `AI-KEY` のUSB到着を監視する常駐スクリプト
  - `install_watcher.ps1` … スタートアップ登録(**管理者不要**)+即起動
  - `uninstall_watcher.ps1` … 上記の削除

## 新しいPCで「挿したら自動メッセージ」を有効化
```powershell
powershell -ExecutionPolicy Bypass -File tools\install_watcher.ps1
```
ラベル `AI-KEY` のUSBを挿すとメッセージが出る。無効化は `uninstall_watcher.ps1`。

## 手動だけで使う(常駐なし)
USBルートの `START.cmd` をダブルクリック → 同じダイアログが出る。

## 機密は置かない
`ACTIVATION.txt`(物理トークン)・`manifest.sha256`・個人データはここに入れない
(AI_KEY `02_RULES` 恒久禁止)。それらは Google Drive / USB のみ。
