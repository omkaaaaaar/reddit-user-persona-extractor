# Reddit User Persona Extractor 🧠

This project generates a detailed user persona based on a Reddit profile. It scrapes the user’s posts and comments, analyzes emotional tone, identifies interests, and builds a personality profile — complete with citations from their activity.

> ✅ Built for the BeyondChats AI/LLM Engineer Internship Assignment.

---

## 🚀 Features

- 🔗 Accepts a Reddit user profile URL
- 🧹 Scrapes posts and comments
- 🤖 Generates a personality using LLM (GPT-based)
- 📊 Analyzes sentiment, subreddits, and writing style
- 🧠 Assigns trait scores (0–100) with visual bars
- 📄 Outputs both `.txt` and styled `.pdf` reports
- 🧾 All insights are **cited** using the source comment or post

---

## 🧩 Tech Stack

- `Python 3.8+`
- `PRAW` – Reddit API wrapper
- `HuggingFace Transformers` – Local GPT model for persona generation
- `ReportLab` – Unicode-safe PDF generation
- `NLTK` – Sentiment analysis and keyword extraction

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/reddit-user-persona-extractor.git
cd reddit-user-persona-extractor


Install dependencies:

pip install -r requirements.txt

Set up Reddit API credentials via .env:

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_app_name


🛠 Usage
Run the main script with any Reddit profile URL:

python main.py https://www.reddit.com/user/kojied/


📂 Output
All results are saved to the /outputs/ directory:

kojied_persona.txt → Raw LLM output with insights
kojied_persona.pdf → Styled 2-page persona profile with:
Emotional Tone
Top Subreddits & Keywords
Personality Traits (0–100)
Interests, Style, Political Leaning, and Profession
Cited Reddit posts/comments



📄 Files Included
All results are saved to the /outputs/ directory:

kojied_persona.txt → Raw LLM output with insights
kojied_persona.pdf → Styled 2-page persona profile with:
Emotional Tone
Top Subreddits & Keywords
Personality Traits (0–100)
Interests, Style, Political Leaning, and Profession
Cited Reddit posts/comments