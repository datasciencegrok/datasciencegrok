import re
from datetime import datetime
import requests

# Load README.md content
with open("README.md", "r") as file:
    readme_content = file.read()

# Update the date
today = datetime.now().strftime("%B %d, %Y")
readme_content = re.sub(r"<!-- DATE_PLACEHOLDER -->", today, readme_content)

# Fetch a random quote
try:
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote = response.json().get("content")
        author = response.json().get("author")
        quote_text = f'"{quote}" — {author}'
    else:
        quote_text = "Stay curious and keep learning!"
except Exception:
    quote_text = "Stay curious and keep learning!"

# Update the quote
readme_content = re.sub(r"<!-- QUOTE_PLACEHOLDER -->", quote_text, readme_content)

# Save the updated README.md
with open("README.md", "w") as file:
    file.write(readme_content)
