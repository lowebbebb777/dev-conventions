@echo off
rem AI_KEY 挿入監視を「今の」セッションで開始する(再ログオン後はスタートアップが自動起動)。
rem 自分の Explorer からダブルクリックで実行すること(そうすれば実セッションでUSBイベントを受け取れる)。
start "" wscript "%LOCALAPPDATA%\AI_KEY\aikey_watch.vbs"
echo AI_KEY の挿入監視を開始しました。
echo USB(AI-KEY)を抜いて挿し直すと、手引きのメッセージが表示されます。
echo （停止したいときは tools\uninstall_watcher.ps1）
timeout /t 5 >nul
