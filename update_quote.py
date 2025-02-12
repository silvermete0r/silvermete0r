import random

README_FILE = "README.md"
START_MARKER = "<!-- QUOTES_START -->"
END_MARKER = "<!-- QUOTES_END -->"

with open(README_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

start_index = lines.index(START_MARKER + "\n") + 1
end_index = lines.index(END_MARKER + "\n")

quotes = [line.strip() for line in lines[start_index:end_index] if line.strip()]
random_quote = random.choice(quotes)

with open(README_FILE, "w", encoding="utf-8") as file:
    inside_quote_section = False
    for line in lines:
        if line.strip() == START_MARKER:
            inside_quote_section = True
            file.write(line)
            file.write("\n> " + random_quote + "\n\n")  # Format as a quote
        elif line.strip() == END_MARKER:
            inside_quote_section = False
            file.write(line)
        elif not inside_quote_section:
            file.write(line)
