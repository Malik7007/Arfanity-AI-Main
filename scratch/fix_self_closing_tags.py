import os
import re

def fix_self_closing(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # List of common non-void tags that should not be self-closing in Svelte/HTML5
    non_void_tags = [
        'div', 'span', 'i', 'b', 'p', 'a', 'button', 'section', 'article', 
        'header', 'footer', 'nav', 'aside', 'main', 'canvas', 'iframe', 
        'script', 'style', 'textarea', 'select', 'ul', 'ol', 'li', 'h1', 
        'h2', 'h3', 'h4', 'h5', 'h6', 'label', 'svg', 'path'
    ]
    
    new_content = content
    for tag in non_void_tags:
        # Regex to find self-closing tags like <div ... />
        # It handles attributes and spaces.
        # Note: We avoid matching void elements or Svelte components (starting with uppercase)
        pattern = rf'<({tag})(\s+[^>]*?|)\s*/>'
        replacement = rf'<\1\2></\1>'
        new_content = re.sub(pattern, replacement, new_content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

src_dir = 'd:\\Arfanity-AI-main\\src'
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.svelte'):
            filepath = os.path.join(root, file)
            if fix_self_closing(filepath):
                print(f"Fixed self-closing tags in: {filepath}")
