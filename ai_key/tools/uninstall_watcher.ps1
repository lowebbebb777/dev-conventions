# AI_KEY 常駐ウォッチャーを削除する(スタートアップ登録・ローカル写し・起動中プロセス)。
$startup = [Environment]::GetFolderPath('Startup')
Remove-Item (Join-Path $startup 'AI_KEY Watcher.vbs') -Force -ErrorAction SilentlyContinue
# 起動中のウォッチャーを停止
Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
    Where-Object { $_.CommandLine -like '*watch_aikey.ps1*' } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
Remove-Item (Join-Path $env:LOCALAPPDATA 'AI_KEY') -Recurse -Force -ErrorAction SilentlyContinue
Write-Host '削除完了: スタートアップ登録・ローカル写し・起動中プロセスを除去しました。'
