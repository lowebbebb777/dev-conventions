#!/usr/bin/env python3
"""Lightweight JSON State Manager for Token Minimization.

Replaces heavy text file reading with structured JSON status operations.
"""

import json
import sys
from pathlib import Path

STATE_FILE = Path(".state.json")

def load_state() -> dict:
    if not STATE_FILE.exists():
        return {
            "current_position": "Initial State",
            "active_task": None,
            "last_verified_tests": "PASS",
        }
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}

def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    if len(sys.argv) < 2:
        print(json.dumps(load_state(), ensure_ascii=False, indent=2))
        return
        
    cmd = sys.argv[1]
    if cmd == "get":
        print(json.dumps(load_state(), ensure_ascii=False, indent=2))
    elif cmd == "set" and len(sys.argv) >= 4:
        key, val = sys.argv[2], sys.argv[3]
        st = load_state()
        st[key] = val
        save_state(st)
        print(f"Updated {key} = {val}")

if __name__ == "__main__":
    main()
