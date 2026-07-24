# AI_KEY メッセージ表示(Windowsダイアログ)。手動(START.cmd)と常駐ウォッチャーで共用。
param([string]$Root = (Split-Path $PSScriptRoot -Parent))

# 6秒スロットル(多重起動時の二重表示を防ぐ)
$marker = Join-Path $env:TEMP 'aikey_last_shown.txt'
$now = Get-Date
if (Test-Path $marker) {
    try {
        $last = Get-Content -LiteralPath $marker -TotalCount 1
        if ($last -and (($now - [datetime]$last).TotalSeconds -lt 6)) { return }
    } catch {}
}
$now.ToString('o') | Set-Content -LiteralPath $marker

Add-Type -AssemblyName System.Windows.Forms | Out-Null

$msg = @"
AI_KEY を検出しました。

1) 引き継ぎたいPJのフォルダで AI を開く
2) AI にこう言う:
     このUSBの AI_KEY/10_PROJECTS から引き継ぐPJを選ばせて
3) 終わったら USB と Google Drive を同期

［はい］で手引き(_START_HERE.md)を開きます。
"@

$res = [System.Windows.Forms.MessageBox]::Show(
    $msg, 'AI_KEY',
    [System.Windows.Forms.MessageBoxButtons]::YesNo,
    [System.Windows.Forms.MessageBoxIcon]::Information)

if ($res -eq [System.Windows.Forms.DialogResult]::Yes) {
    $doc = Join-Path $Root '_START_HERE.md'
    if (Test-Path $doc) { Start-Process $doc } else { Start-Process $Root }
}
