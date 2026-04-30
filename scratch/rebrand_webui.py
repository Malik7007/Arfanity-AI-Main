"""
Comprehensive rebranding script: replace all remaining 'webui' / 'Open WebUI' 
references in the chat components folder with Arfanity AI equivalents.
"""
import os
import re

# Ordered from most-specific to least-specific to avoid partial replacements
REPLACEMENTS = [
    # URLs — point to Arfanity / Malik7007 GitHub
    ('https://openwebui.com/m/', 'https://github.com/Malik7007/'),
    ('https://openwebui.com/models', 'https://github.com/Malik7007/Arfanity-AI-Main'),
    ('https://openwebui.com', 'https://github.com/Malik7007/Arfanity-AI-Main'),
    ('https://github.com/open-webui/openapi-servers', 'https://github.com/Malik7007/Arfanity-AI-Main'),
    ('https://github.com/open-webui/open-terminal', 'https://github.com/Malik7007/Arfanity-AI-Main'),
    ('https://github.com/open-webui/open-webui/releases/tag/', 'https://github.com/Malik7007/Arfanity-AI-Main/releases/tag/'),
    ('https://github.com/open-webui/open-webui/blob/main/LICENSE', 'https://github.com/Malik7007/Arfanity-AI-Main/blob/main/LICENSE'),
    ('https://github.com/open-webui/open-webui/blob/main/docs/CONTRIBUTING.md#-translations-and-internationalization', 'https://github.com/Malik7007/Arfanity-AI-Main/blob/main/docs/CONTRIBUTING.md'),
    ('https://github.com/open-webui/open-webui', 'https://github.com/Malik7007/Arfanity-AI-Main'),
    ('https://twitter.com/OpenWebUI', 'https://github.com/Malik7007'),
    
    # Badge image URLs — replace with Arfanity branding
    ('https://img.shields.io/badge/Discord-Open_WebUI-blue?logo=discord&logoColor=white', 'https://img.shields.io/badge/Discord-Arfanity_AI-blue?logo=discord&logoColor=white'),
    ('https://img.shields.io/twitter/follow/OpenWebUI', 'https://img.shields.io/badge/Follow-Arfanity_AI-blue'),
    ('https://img.shields.io/github/stars/open-webui/open-webui?style=social&label=Star us on Github', 'https://img.shields.io/github/stars/Malik7007/Arfanity-AI-Main?style=social&label=Star us on Github'),

    # Visible text strings
    ('Open WebUI Inc.', 'Arfanity AI'),
    ('Open WebUI Community', 'Arfanity AI Community'),
    ('Open WebUI version', 'Arfanity AI version'),
    ("Open WebUI can use tools provided by any OpenAPI server.", "Arfanity AI can use tools provided by any OpenAPI server."),
    ('Help us translate Open WebUI!', 'Help us translate Arfanity AI!'),
    ('open-webui-stats', 'arfanity-ai-stats'),
    ("requests from Open WebUI.", "requests from Arfanity AI."),
    ("improvements to Open WebUI.", "improvements to Arfanity AI."),
    ("sync your usage stats with Open WebUI Community", "sync your usage stats with Arfanity AI Community"),
    ("Share to Open WebUI Community", "Share to Arfanity AI Community"),
    ("Redirecting you to Open WebUI Community", "Redirecting you to Arfanity AI Community"),
    ("Open WebUI", "Arfanity AI"),  # catch-all for remaining visible text
    
    # Comments in code
    ('Open WebUI backend proxy', 'Arfanity AI backend proxy'),
    ('proxy through Open WebUI backend', 'proxy through Arfanity AI backend'),
    
    # Identifiers / search keywords in code (lowercase)
    ("'about open webui'", "'about arfanity ai'"),
    ("'aboutopenwebui'", "'aboutarfanityai'"),
    ("'webuisettings'", "'aisettings'"),
    ("'webui settings'", "'ai settings'"),
    
    # UI labels
    ('WebUI Settings', 'AI Settings'),
    ('WebUI will make requests', 'Arfanity AI will make requests'),
    
    # Any remaining case-insensitive "webui" in visible text
    # (These are intentionally at the end as last resort)
]

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in REPLACEMENTS:
        new_content = new_content.replace(old, new)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

src_dir = r'd:\Arfanity-AI-main\src'
count = 0
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith(('.svelte', '.ts', '.js')):
            filepath = os.path.join(root, file)
            if replace_in_file(filepath):
                count += 1
                print(f"Updated: {filepath}")

print(f"\nTotal files updated: {count}")
