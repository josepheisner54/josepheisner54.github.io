#!/usr/bin/env python3

import os
import json

def is_text_file(filepath, blocksize=512):
    with open(filepath, 'rb') as f:
        chunk = f.read(blocksize)
    return b'\x00' not in chunk

def gather_structure(root):
    def read_text_file(path):
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read()

    def build_tree(dir_path):
        tree = {}
        for entry in os.scandir(dir_path):
            if entry.is_dir():
                tree[entry.name] = build_tree(entry.path)
            else:
                if is_text_file(entry.path):
                    tree[entry.name] = read_text_file(entry.path)
                else:
                    size = entry.stat().st_size
                    tree[entry.name] = f"<Binary file: {size} bytes>"
        return tree

    return build_tree(root)

def main():
    structure = gather_structure(".")
    # Write JSON directly to a file in UTF-8
    with open("website_export.json", "w", encoding="utf-8") as f:
        json.dump(structure, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
