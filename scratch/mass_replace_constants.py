import os
import re

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacements = {
        'WEBUI_BASE_URL': 'AI_BASE_URL',
        'WEBUI_API_BASE_URL': 'AI_API_BASE_URL',
        'WEBUI_NAME': 'AI_NAME',
        'WEBUI_VERSION': 'AI_VERSION',
        'WEBUI_BUILD_HASH': 'AI_BUILD_HASH',
    }
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

src_dir = 'd:\\Arfanity-AI-main\\src'
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith(('.svelte', '.ts', '.js')):
            filepath = os.path.join(root, file)
            if replace_in_file(filepath):
                print(f"Updated: {filepath}")
