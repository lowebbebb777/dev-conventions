#!/usr/bin/env python3
"""AST Summary Extractor for Token Minimization.

Extracts class & function signatures with line numbers from Python files,
allowing AI agents to inspect codebase structure using ~90% fewer tokens.
"""

import ast
import sys
import os
from pathlib import Path

def extract_file_structure(filepath: str) -> str:
    path = Path(filepath)
    if not path.exists() or not path.suffix == '.py':
        return f"Error: Invalid Python file '{filepath}'"
        
    try:
        source = path.read_text(encoding='utf-8', errors='replace')
        tree = ast.parse(source, filename=filepath)
    except Exception as exc:
        return f"Error parsing {filepath}: {exc}"

    lines = [f"File: {path.name} ({len(source.splitlines())} lines)"]
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            lines.append(f"  Class {node.name} (L{node.lineno}-L{getattr(node, 'end_lineno', node.lineno)})")
            for item in node.body:
                if isinstance(item, ast.FunctionDef) or isinstance(item, ast.AsyncFunctionDef):
                    args = [a.arg for a in item.args.args]
                    lines.append(f"    def {item.name}({', '.join(args)}) (L{item.lineno})")
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not isinstance(getattr(node, 'parent', None), ast.ClassDef):
            if hasattr(node, 'col_offset') and node.col_offset == 0:
                args = [a.arg for a in node.args.args]
                lines.append(f"  def {node.name}({', '.join(args)}) (L{node.lineno})")

    return "\n".join(lines)

def summarize_directory(dirpath: str) -> str:
    target = Path(dirpath)
    if not target.is_dir():
        return extract_file_structure(dirpath)
        
    out = []
    for root, _, files in os.walk(target):
        if ".venv" in root or ".git" in root or "__pycache__" in root:
            continue
        for f in sorted(files):
            if f.endswith(".py"):
                full_path = os.path.join(root, f)
                out.append(extract_file_structure(full_path))
    return "\n\n".join(out)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(summarize_directory(target))
