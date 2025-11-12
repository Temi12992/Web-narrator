import requests
from bs4 import BeautifulSoup
import subprocess

def get_web_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style"]):
        tag.extract()

    text = soup.get_text(separator=" ", strip=True)
    return text

def narrate_with_espeak(text, speed=175, voice="en"):
    chunk_size = 500
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        subprocess.run(["espeak", f"-s{speed}", f"-v{voice}", chunk])

if __name__ == "__main__":
    url = input("Enter a webpage URL: ").strip()
    print("🔍 Fetching content...")
    text = get_web_text(url)
    print("🎙️ Speaking aloud using eSpeak...")
    narrate_with_espeak(text[:3000]) 
    print("✅ Done!")
