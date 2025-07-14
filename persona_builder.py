# persona_builder.py

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "distilgpt2"  # optimized for 8GB RAM
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_persona(username, user_data, analysis):
    """Generate a user persona from scraped Reddit data and tone analysis."""
    text_blocks = []

    for p in user_data.get("posts", []):
        text_blocks.append(f"[POST in r/{p['subreddit']}]\n{p['title']}\n{p['selftext']}\n")

    for c in user_data.get("comments", []):
        text_blocks.append(f"[COMMENT in r/{c['subreddit']}]\n{c['body']}\n")

    sample_text = "\n".join(text_blocks[:10])[:1500]

    prompt = f"""
You are an AI sociologist. Analyze the Reddit activity of u/{username} to generate a detailed persona.

Insights:
- Frequent Subreddits: {', '.join([s[0] for s in analysis['top_subreddits']])}
- Emotional Tone: {analysis['emotional_tone']} (Score: {analysis['avg_sentiment']})
- Top Keywords: {', '.join([w[0] for w in analysis['top_keywords']])}

Reddit Sample:
{sample_text}

Persona:
"""

    try:
        result = generator(prompt, max_new_tokens=300, temperature=0.7, do_sample=True)[0]["generated_text"]
        return result[len(prompt):].strip()
    except Exception as e:
        print(f"Error generating persona: {e}")
        return "Error generating persona."
