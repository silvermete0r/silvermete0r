import json
import random

README_FILE = "README.md"
QUOTES_FILE = "quotes.json"
START_MARKER = "<!-- QUOTES_START -->"
END_MARKER = "<!-- QUOTES_END -->"

# Load quotes from JSON
with open(QUOTES_FILE, "r", encoding="utf-8") as file:
    quotes = json.load(file)["quotes"]

# Select a random quote
random_entry = random.choice(quotes)
random_quote = random_entry["quote"]
random_author = random_entry["author"]

# Read README content
with open(README_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Find section and update it
with open(README_FILE, "w", encoding="utf-8") as file:
    inside_quote_section = False
    for line in lines:
        if line.strip() == START_MARKER:
            inside_quote_section = True
            file.write(line)
            file.write(f"\n> \"{random_quote}\"\n>\n> — *{random_author}*\n\n")  # Markdown formatted
        elif line.strip() == END_MARKER:
            inside_quote_section = False
            file.write(line)
        elif not inside_quote_section:
            file.write(line)

print(f"✅ Updated README with a new quote by {random_author}.")
