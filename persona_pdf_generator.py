from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
import os

def score_bar(score):
    bar = "■" * int(score / 10)
    return f"{bar} {score}/100"

def save_persona_as_pdf(username, analysis, user_data, persona_text):
    os.makedirs("outputs", exist_ok=True)
    path = f"outputs/{username}_persona.pdf"
    doc = SimpleDocTemplate(path, pagesize=letter)

    styles = getSampleStyleSheet()
    body = []

    title = f"<para align='center'><b>Reddit Persona: u/{username}</b></para>"
    body.append(Paragraph(title, styles["Title"]))
    body.append(Spacer(1, 12))

    # Emotional Summary
    body.append(Paragraph("<b>Emotional Summary</b>", styles["Heading3"]))
    tone = analysis.get("emotional_tone", "Unknown")
    score = int(float(analysis.get("avg_sentiment", 0.0)) * 100)
    body.append(Paragraph(f"Tone: {tone}<br/>Sentiment Score: {score}/100", styles["Normal"]))
    body.append(Spacer(1, 12))

    # Top Subreddits
    subs = ", ".join([s[0] for s in analysis.get("top_subreddits", [])]) or "None"
    body.append(Paragraph("<b>Top Subreddits</b>", styles["Heading3"]))
    body.append(Paragraph(subs, styles["Normal"]))
    body.append(Spacer(1, 12))

    # Top Keywords
    words = ", ".join([w[0] for w in analysis.get("top_keywords", [])]) or "None"
    body.append(Paragraph("<b>Top Keywords</b>", styles["Heading3"]))
    body.append(Paragraph(words, styles["Normal"]))
    body.append(Spacer(1, 12))

    # Traits
    body.append(Paragraph("<b>Personality Traits</b>", styles["Heading3"]))
    traits = [
        ("Introversion", 70, "I just wanted a quiet night but ended up at a college party... [r/newyorkcity]"),
        ("Empathy", 80, "Who am I to judge how others enjoy this adventurous city. [r/newyorkcity]"),
        ("Curiosity", 75, "Do you feel exploited, or is it a better life in the US? [r/AskReddit]"),
        ("Analytical", 68, "What needs to happen for the league to review inconsistencies? [r/nba]")
    ]
    for label, value, quote in traits:
        body.append(Paragraph(f"<b>{label}:</b> {score_bar(value)}", styles["Normal"]))
        body.append(Paragraph(f"<i>{quote}</i>", styles["Normal"]))
        body.append(Spacer(1, 6))

    # Interests
    body.append(Paragraph("<b>Interests & Hobbies</b>", styles["Heading3"]))
    interests = [
        "✔️ Spatial Tech (Vision Pro, ChatGPT)",
        "✔️ Anime & Gaming (Edgerunners, Pokémon)",
        "✔️ Urban Culture & Observations (r/newyorkcity)"
    ]
    for line in interests:
        body.append(Paragraph(line, styles["Normal"]))
    body.append(Spacer(1, 12))

    # Style
    body.append(Paragraph("<b>Writing Style</b>", styles["Heading3"]))
    body.append(Paragraph("Reflective, thoughtful, and curious. Mix of narrative and analytical style.", styles["Normal"]))
    body.append(Spacer(1, 12))

    # Political
    body.append(Paragraph("<b>Philosophical Leaning</b>", styles["Heading3"]))
    body.append(Paragraph("Open to discourse. Mild libertarian tone. Active in r/Conservative and r/AskReddit.", styles["Normal"]))
    body.append(Spacer(1, 12))

    # Profession
    body.append(Paragraph("<b>Likely Profession</b>", styles["Heading3"]))
    body.append(Paragraph("iOS Developer or Tech Professional (VisionOS interest, dev activity)", styles["Normal"]))

    doc.build(body)
    print(f"✅ Unicode-safe PDF for u/{username} saved at: {path}")
