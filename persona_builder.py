# persona_builder.py

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)

def generate_persona(username, user_data, analysis):
    """Generates a structured persona profile with categories, scores, and citations."""
    formatted_text = ""

    # Prepare text for LLM from posts/comments
    for post in user_data.get("posts", []):
        formatted_text += f"[POST in r/{post['subreddit']}]\nTitle: {post['title']}\n{post['selftext']}\n\n"

    for comment in user_data.get("comments", []):
        formatted_text += f"[COMMENT in r/{comment['subreddit']}]\n{comment['body']}\n(Link: {comment['link']})\n\n"

    formatted_text = formatted_text[:6000]  # Trim for safety

    prompt = f"""
You are a behavioral psychologist and UX researcher.

Using the Reddit activity of user u/{username} and the emotional/subreddit analysis below, generate a structured persona profile like this format:

---
**User Persona: u/{username}**

**Emotional Tone**  
- Tone: {analysis['emotional_tone']}  
- Average Sentiment Score: {analysis['avg_sentiment']}  

**Top Subreddits**: {', '.join([s[0] for s in analysis['top_subreddits']])}  
**Top Keywords**: {', '.join([k[0] for k in analysis['top_keywords']])}

---

**Personality Traits**  
(Score each trait from 0 to 10 and give a citation from a post or comment)

- Introversion: 7  
  _"I just wanted a quiet night but ended up at a college party..."_ [POST: r/newyorkcity]
- Empathy: 8  
  _"Who am I to judge how others enjoy this adventurous city."_ [POST: r/newyorkcity]

**Interests & Hobbies**  
- Tech Enthusiast (Vision Pro, ChatGPT) [POST: r/VisionPro]
- Anime/Gaming Fan (mentions Edgerunners, Pokemon) [POST: r/VisionPro]

**Writing Style**  
- Thoughtful, narrative, reflective [POST: r/newyorkcity]  
- Curious and analytical [POST: r/visionosdev]

**Political/Philosophical Leanings**  
- Open to discourse (asks questions in r/Conservative, r/AskReddit)  
- Mildly libertarian leanings [POST: r/Conservative]

**Likely Profession/Field**  
- iOS Developer or Tech Professional [POST: r/visionosdev]

Reddit Activity Snippets:
{formatted_text}
"""

    try:
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)
        output = model.generate(
            **inputs,
            max_new_tokens=500,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.15,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
        result = tokenizer.decode(output[0], skip_special_tokens=True)

        # Remove repetition of prompt if model echoes it
        if "User Persona:" in result:
            result = result.split("User Persona:")[-1].strip()
            result = f"User Persona: {result}"

        return result

    except Exception as e:
        print(f"LLM Error: {e}")
        return "Error generating structured persona."
