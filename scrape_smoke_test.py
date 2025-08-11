import requests
from bs4 import BeautifulSoup

url = "https://example.com"
r = requests.get(url, timeout=10)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
h1 = soup.find("h1")
print("Status:", r.status_code)
print("Título H1:", h1.get_text(strip=True) if h1 else "No encontrado")
