import os
from dotenv import load_dotenv

# Explicitly load the .env file from the current directory
load_dotenv(dotenv_path=".env")

# Fetch variables
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
openai_key = os.getenv("OPENAI_API_KEY")

# Print the values to verify
print("🔐 Reddit Client ID:", client_id)
print("🔐 Reddit Client Secret:", client_secret)
print("🧠 OpenAI API Key:", openai_key)
