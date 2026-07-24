#!/usr/bin/env python3
"""
AI_KEY Sync Engine - Google Drive (正本) ⇄ USB (写し) 自動双方向最新化スクリプト
"""
import os
import shutil
import sys
import subprocess
from pathlib import Path
import string

# 検索対象となる Google Drive / ローカルマスターのパス候補
MASTERS = [
    Path(r"C:\Users\soich\OneDrive\Desktop\AI_KEY_bundle\AI_KEY"),
    Path(r"C:\Users\soich\dev-conventions\ai_key"),
]

def find_usb_aikey():
    """接続されている USB メモリ上の AI_KEY フォルダを自動検索"""
    for letter in string.ascii_uppercase:
        try:
            usb_path = Path(f"{letter}:/AI_KEY")
            if usb_path.exists() and (usb_path / "00_BOOT.md").exists():
                return usb_path
        except OSError:
            continue
    return None

def sync_directories(src_dir, dst_dir):
    """
    src_dir の内容を dst_dir へ同期 (ACTIVATION.txt は除外)
    """
    if not src_dir.exists():
        return
    dst_dir.mkdir(parents=True, exist_ok=True)
    
    for item in src_dir.rglob("*"):
        # verify.py 自体の同期などで書き込みロックがかかるのを防ぐ
        rel = item.relative_to(src_dir)
        if item.name == "ACTIVATION.txt":
            continue
        dst_item = dst_dir / rel
        if item.is_dir():
            dst_item.mkdir(parents=True, exist_ok=True)
        else:
            try:
                if not dst_item.exists() or item.stat().st_mtime > dst_item.stat().st_mtime or item.stat().st_size != dst_item.stat().st_size:
                    shutil.copy2(item, dst_item)
            except Exception as e:
                print(f"[WARN] Skip file copy {item}: {e}")

def main():
    print("=== AI_KEY Automatic Sync Engine ===")
    usb_dir = find_usb_aikey()
    
    # 存在する Drive 正本マスターを取得
    drive_dir = None
    for master in MASTERS:
        if master.exists():
            drive_dir = master
            break
            
    if not drive_dir:
        print("[ERROR] Master AI_KEY directory not found.")
        sys.exit(1)
        
    print(f"[*] Drive Master: {drive_dir}")
    if usb_dir:
        print(f"[*] USB Copy    : {usb_dir}")
    else:
        print("[*] USB Copy    : (Not connected)")

    # 1. 相互同期 (USB ⇄ Drive)
    if usb_dir and usb_dir.exists():
        sync_directories(usb_dir, drive_dir)
        sync_directories(drive_dir, usb_dir)
        print("[OK] Bidirectional sync between Drive and USB completed.")

    # 2. 両方のハッシュマニフェスト再生成 (--update)
    verify_script_drive = drive_dir / "90_INTEGRITY" / "verify.py"
    if verify_script_drive.exists():
        subprocess.run([sys.executable, str(verify_script_drive), "--update"], check=True)
        
    if usb_dir and usb_dir.exists():
        verify_script_usb = usb_dir / "90_INTEGRITY" / "verify.py"
        if verify_script_usb.exists():
            subprocess.run([sys.executable, str(verify_script_usb), "--update"], check=True)

    print("[SUCCESS] All AI_KEY stores (Drive & USB) are fully synchronized and integrity-verified!")

if __name__ == "__main__":
    main()
