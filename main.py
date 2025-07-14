# main.py

import sys
import os
from reddit_scraper import scrape_user_data
from persona_builder import generate_persona
from utils import extract_username_from_url, save_persona_to_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <reddit_profile_url>")
        return

    reddit_url = sys.argv[1]
    username = extract_username_from_url(reddit_url)

    if not username:
        print("Invalid Reddit profile URL.")
        return

    print(f"🔍 Scraping Reddit activity for u/{username}...")
    user_data = scrape_user_data(username)

    if not user_data:
        print("❌ No user data found or scraping failed.")
        return

    print("🤖 Generating user persona using LLM...")
    persona_text = generate_persona(username, user_data)

    print("📄 Saving persona to text file...")
    output_path = os.path.join("outputs", f"{username}_persona.txt")
    save_persona_to_file(output_path, persona_text)

    print(f"✅ Persona for u/{username} saved at: {output_path}")


if __name__ == "__main__":
    main()
