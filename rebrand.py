import os
import sys

root_dir = r"d:\Antigravity\genetinddoc\OpenClaw-Medical-Skills"

replacements = [
    ("OpenClaw-Medical-Skills", "GeneTind-Life-Skills"),
    ("OpenClaw Medical Skills", "GeneTind Life Skills"),
    ("openclaw-medical-skills", "genetind-life-skills"),
    ("OpenClaw", "GeneTind"),
    ("openclaw", "genetind"),
    ("OPENCLAW", "GENETIND"),
    ("NanoClaw", "NanoTind"),
    ("nanoclaw", "nanotind"),
    ("MedClaw-Org", "GeneTind-Org"),
    ("Medical-Skills", "Life-Skills"),
]

def process_readme(content):
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if '[![GitHub' in line or '[![License' in line or '[![Platform' in line or '[![Skills Count' in line or '[![技能数量' in line:
            continue
        if 'WangRongsheng/awesome-LLM-resources' in line:
            continue
        new_lines.append(line)
    return '\n'.join(new_lines)

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return # Skip binary or non-utf8 files
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    original_content = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    content = content.replace("https://github.com/GeneTind-Org", "https://git.internal.genetind.com/GeneTind-Org")
    content = content.replace("https://github.com/genetind/genetind", "https://git.internal.genetind.com/GeneTind-Org/genetind")

    if os.path.basename(filepath).startswith('README'):
        content = process_readme(content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Starting rebranding on {root_dir}")

# First pass: replace content
for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.git' in dirnames:
        dirnames.remove('.git')
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        replace_in_file(filepath)

# Second pass: rename files and directories bottom-up
for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
    if '.git' in dirnames:
        dirnames.remove('.git')
        
    for filename in filenames:
        new_filename = filename
        for old, new in replacements:
            new_filename = new_filename.replace(old, new)
        if new_filename != filename:
            old_path = os.path.join(dirpath, filename)
            new_path = os.path.join(dirpath, new_filename)
            os.rename(old_path, new_path)
            
    for dirname in dirnames:
        new_dirname = dirname
        for old, new in replacements:
            new_dirname = new_dirname.replace(old, new)
        if new_dirname != dirname:
            old_path = os.path.join(dirpath, dirname)
            new_path = os.path.join(dirpath, new_dirname)
            os.rename(old_path, new_path)

print("Done with contents and internal renaming.")
