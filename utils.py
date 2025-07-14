# utils.py

import os

def extract_username_from_url(url):
    """Extract the Reddit username from the profile URL."""
    if url.endswith("/"):
        url = url[:-1]
    return url.split("/")[-1]

def save_persona_to_file(filepath, content):
    """Save the generated persona text to a file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
