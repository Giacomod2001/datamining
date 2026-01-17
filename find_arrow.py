import sys

# Force UTF-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

with open('app.py', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if '←' in line or '&larr;' in line or 'transferable' in line.lower():
            try:
                print(f"{i}: {line.strip()}")
            except:
                pass
