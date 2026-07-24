# AI_KEY 常駐ウォッチャー(ポーリング方式・ログ付き)。
# ラベル 'AI-KEY' のUSBが新しく挿入されたらメッセージを表示する。
# ドライブ検出は WMI ではなく .NET DriveInfo を使う(WMIはこの環境でハングすることがあるため)。
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
        if ($d) { return $d.Name }   # 例: "F:\"
    } catch { Log "query error: $_" }
    return $null
}

function Show-AiKey($root) {
    $show = Join-Path $root 'tools\show_message.ps1'          # USB上の本体を優先
    if (-not (Test-Path $show)) { $show = Join-Path $Self 'show_message.ps1' }  # 無ければローカル写し
    Log "show for $root using $show"
    Start-Process powershell -ArgumentList @(
        '-NoProfile','-WindowStyle','Hidden','-ExecutionPolicy','Bypass',
        '-File', "`"$show`"", '-Root', "`"$root`"")
}

# 起動時点で挿さっていても、その状態は「既知」として扱う(新規挿入のみ通知)
$prev = [bool](Get-AiKeyRoot)
Log "initial present=$prev"

while ($true) {
    Start-Sleep -Seconds 2
    $root = Get-AiKeyRoot
    $now  = [bool]$root
    if ($now -and -not $prev) { Log "ARRIVED $root"; Show-AiKey $root }
    elseif (-not $now -and $prev) { Log "removed" }
    $prev = $now
}
