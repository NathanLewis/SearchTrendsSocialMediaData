#!/usr/bin/env python

from bs4 import BeautifulSoup
from pathlib import Path
html_content = Path('trending_2025-02-24T21_37_04.html').read_text()

# Parse your HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Get all divs with class 'my-class'
divs = soup.select('div.mZ3RIc')

# Access individual divs
for div in divs:
    print(div.text.strip())
