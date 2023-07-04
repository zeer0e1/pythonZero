import requests
import re
from bs4 import BeautifulSoup

url = 'http://localhost:7777/'
response = requests.get(url)
raw_html = response.content
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    ariticle = top_jobs_heading.parent
    if ariticle is not None:
        for p in ariticle.select('p'):
            print(re.sub(r'\s{1,}', '', p.text).strip())
