# AI_KEY 常駐ウォッチャーをこのユーザーへ登録(管理者不要・スタートアップ方式・削除可)。
# USBから実行してよい。監視スクリプトはローカルへ写し、USB非挿入時も待機できるようにする。
$Dest = Join-Path $env:LOCALAPPDATA 'AI_KEY'
New-Item -ItemType Directory -Force $Dest | Out-Null
Copy-Item (Join-Path $PSScriptRoot 'watch_aikey.ps1')  $Dest -Force
Copy-Item (Join-Path $PSScriptRoot 'show_message.ps1') $Dest -Force
$Watch = Join-Path $Dest 'watch_aikey.ps1'

# 隠し起動用 VBS(コンソールを一切出さない)
$vbs = Join-Path $Dest 'aikey_watch.vbs'
@"
' AI_KEY watcher launcher (hidden)
CreateObject("WScript.Shell").Run "powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File ""$Watch""", 0, False
"@ | Set-Content -Path $vbs -Encoding ASCII

# スタートアップへ登録(ログオン時に自動起動・管理者不要)
$startup = [Environment]::GetFolderPath('Startup')
Copy-Item $vbs (Join-Path $startup 'AI_KEY Watcher.vbs') -Force

# 今すぐ起動
Start-Process wscript.exe -ArgumentList "`"$vbs`""
Write-Host 'インストール完了: スタートアップに登録し、今すぐ起動しました(管理者不要)。'
Write-Host '削除するには uninstall_watcher.ps1 を実行してください。'
