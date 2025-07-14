# main.py

import sys
import os
from reddit_scraper import scrape_user_data
from scraped_analyzer import analyze_scraped_data
from persona_builder import generate_persona
from persona_pdf_generator import save_persona_as_pdf  # ✅ 1. IMPORT HERE

def extract_username_from_url(url):
    return url.strip("/").split("/")[-1]

def save_persona_to_file(username, content):
    os.makedirs("outputs", exist_ok=True)
    path = f"outputs/{username}_persona.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Persona for u/{username} saved at: {path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <reddit_profile_url>")
        return

    profile_url = sys.argv[1]
    username = extract_username_from_url(profile_url)

    print(f"\n🔍 Scraping Reddit activity for u/{username}...")
    user_data = scrape_user_data(username)

    print(f"📊 Analyzing emotional tone and subreddit trends...")
    analysis = analyze_scraped_data(user_data)

    print(f"\n🧠 Emotional Tone: {analysis['emotional_tone']} (Sentiment Score: {analysis['avg_sentiment']})")
    print(f"🔥 Top Subreddits: {[s[0] for s in analysis['top_subreddits']]}")
    print(f"💬 Top Keywords: {[w[0] for w in analysis['top_keywords']]}\n")

    print(f"🤖 Generating user persona using local LLM...")
    persona_text = generate_persona(username, user_data, analysis)

    print(f"📄 Saving persona to text file...")
    save_persona_to_file(username, persona_text)

    # ✅ 2. Generate PDF
    save_persona_as_pdf(username, analysis, user_data, persona_text)

if __name__ == "__main__":
    main()
