# AI_KEY 常駐ウォッチャー。ラベル 'AI-KEY' のUSB到着でメッセージを表示する。
# ログオン時にスケジューラから隠しウィンドウで起動される想定。
$Label  = 'AI-KEY'
$Self   = $PSScriptRoot
$Marker = Join-Path $env:TEMP 'aikey_last_shown.txt'

function Show-AiKey($root) {
    # 6秒スロットル(到着イベントの多重発火・起動時スキャンの重複を抑える)
    $now = Get-Date
    if (Test-Path $Marker) {
        $last = Get-Content $Marker -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($last) { try { if (($now - [datetime]$last).TotalSeconds -lt 6) { return } } catch {} }
    }
    $now.ToString('o') | Set-Content $Marker
    $show = Join-Path $root 'tools\show_message.ps1'                  # USB上の本体を優先
    if (-not (Test-Path $show)) { $show = Join-Path $Self 'show_message.ps1' }  # 無ければローカル写し
    Start-Process powershell -ArgumentList @(
        '-NoProfile','-WindowStyle','Hidden','-ExecutionPolicy','Bypass',
        '-File', "`"$show`"", '-Root', "`"$root`"")
}

function Find-AiKey {
    Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=2' |
        Where-Object { $_.VolumeName -eq $Label } |
        ForEach-Object { $_.DeviceID + '\' }
}

# 起動時に既に挿さっていれば一度表示
Find-AiKey | ForEach-Object { Show-AiKey $_ }

# ボリューム到着イベント(EventType=2)を購読
Register-CimIndicationEvent -Query "SELECT * FROM Win32_VolumeChangeEvent WHERE EventType=2" `
    -SourceIdentifier 'AiKeyArrival' -Action {
        Start-Sleep -Milliseconds 800
        Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=2' |
            Where-Object { $_.VolumeName -eq 'AI-KEY' } |
            ForEach-Object { Show-AiKey ($_.DeviceID + '\') }
    } | Out-Null

Wait-Event -SourceIdentifier 'AiKeyIdleForever'   # 常駐(タスク停止/ログオフまで)
