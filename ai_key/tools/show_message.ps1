# AI_KEY メッセージ表示(Windowsダイアログ)。手動(START.cmd)と常駐ウォッチャーで共用。
param([string]$Root = (Split-Path $PSScriptRoot -Parent))

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
