@echo off
rem AI_KEY 手引きを実ダイアログで表示(ゼロインストール・ダブルクリック用)
start "" powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "%~dp0tools\show_message.ps1" -Root "%~dp0"
