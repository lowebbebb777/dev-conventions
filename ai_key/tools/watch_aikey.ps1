# AI_KEY 常駐ウォッチャー(ポーリング方式・ログ付き)
# ラベル 'AI-KEY' のUSBが新しく挿入されたら、Drive正本と自動同期しメッセージを表示する
$Label   = 'AI-KEY'
$Self    = $PSScriptRoot
$Log     = Join-Path $env:TEMP 'aikey_watch.log'
$PidFile = Join-Path $env:TEMP 'aikey_watch.pid'

function Log($m) { try { "$(Get-Date -Format o)  $m" | Add-Content -LiteralPath $Log } catch {} }

$PID | Set-Content -LiteralPath $PidFile
Log "watcher start (pid $PID) self=$Self"

function Get-AiKeyRoot {
    try {
        $d = [System.IO.DriveInfo]::GetDrives() | Where-Object {
            $_.DriveType -eq 'Removable' -and $_.IsReady -and $_.VolumeLabel -eq $Label
        } | Select-Object -First 1
        if ($d) { return $d.Name }
    } catch { Log "query error: $_" }
    return $null
}

function Show-AiKey($root) {
    $show = Join-Path $root 'tools\show_message.ps1'
    if (-not (Test-Path $show)) { $show = Join-Path $Self 'show_message.ps1' }
    Log "show for $root using $show"
    Start-Process powershell -ArgumentList @(
        '-NoProfile','-WindowStyle','Hidden','-ExecutionPolicy','Bypass',
        '-File', "`"$show`"", '-Root', "`"$root`"")
}

$prev = [bool](Get-AiKeyRoot)
Log "initial present=$prev"

while ($true) {
    Start-Sleep -Seconds 2
    $root = Get-AiKeyRoot
    $now  = [bool]$root
    if ($now -and -not $prev) { 
        Log "ARRIVED $root"
        # 挿入時に Google Drive (正本) ⇄ USB (写し) の自動同期を実行
        try {
            $syncScript = Join-Path $root 'AI_KEY\90_INTEGRITY\sync_aikey.py'
            if (Test-Path $syncScript) {
                Log "executing auto-sync: $syncScript"
                Start-Process python -ArgumentList "`"$syncScript`"" -NoNewWindow -Wait
            }
        } catch {
            Log "auto-sync error: $_"
        }
        Show-AiKey $root 
    }
    elseif (-not $now -and $prev) { Log "removed" }
    $prev = $now
}
