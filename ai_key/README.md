# ai_key —(非推奨・アーカイブ)USB「AI_KEY」の道具

> **⚠️ 非推奨(2026-07-25)。** USB / AI_KEY 方式は引き継ぎの正本から外しました。
> 現在の引き継ぎは **git だけで完結**します:
> - どのプロジェクトか … `../projects.md`(索引の正本)
> - 各プロジェクトの現在地 … 各repoの `AGENTS.md` → `docs/STATE.md` → `docs/LOG.md`
>
> USBは不要。`sync_aikey.py` の必須実行も撤去済み。以下は歴史的経緯のためのアーカイブです。

このフォルダは USB「AI_KEY」に載せていた**非機密の道具**の版管理コピー(アーカイブ)。

## いちばん簡単な使い方(推奨)
USBを挿すと Explorer がルートを開く。そこの **`_START_HERE.txt`** を読むだけ。
特別な常駐やインストールは要らない。AI↔AIの引き継ぎ本体は各リポジトリの
`docs/STATE.md` / `docs/LOG.md`(git)で回っている。

## 中身
- `_START_HERE.txt` … USBルートに置く人間向けクイックスタート(平文)
- `_START_HERE.md` … 同内容の Markdown 版
- `03_RESUME.md` … AI用の引き継ぎ再開フロー(`AI_KEY/` 直下へ置く)
- `START.cmd` … ダブルクリックで手引きダイアログ(任意・ゼロインストール)
- `tools/` … (任意・実験的)挿入時に自動でメッセージを出す常駐ウォッチャー

## 自動ポップアップ(tools/)について — 既定オフ
挿入時の自動メッセージは**環境依存で不安定**(WindowsのUSB自動実行制限、
プロセスのドライブ可視性)。**基本は「Explorer + `_START_HERE.txt`」で十分**。
どうしても使いたい人向けに残してあるが、既定では入れない:
- `install_watcher.ps1`(スタートアップ登録・管理者不要)/ `uninstall_watcher.ps1`

## 機密は置かない
`ACTIVATION.txt`(物理トークン)・`manifest.sha256`・個人データはここに入れない。
それらは Google Drive / USB のみ。
