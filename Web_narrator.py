import requests
from bs4 import BeautifulSoup
import pyttsx3
import time

def get_web_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style"]):
        tag.extract()

    text = soup.get_text(separator=" ", strip=True)
    return text

def narrate_with_pyttsx3(text, speed=175, voice_id=None, chunk_size=500, pause=0.1):
    engine = pyttsx3.init()
    engine.setProperty("rate", speed)

    if voice_id:
        try:
            engine.setProperty("voice", voice_id)
        except Exception as e:
            print(f"[WARN] Could not set voice: {e}")
            
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        engine.say(chunk)
        engine.runAndWait()
        time.sleep(pause)
if __name__ == "__main__":
    url = input("Enter a webpage URL: ").strip()
    print("🔍 Fetching content...")
    try:
        text = get_web_text(url)
    except Exception as e:
        print(f"[ERROR] Failed to fetch webpage: {e}")
        exit(1)
    print("🎙️ Speaking aloud using pyttsx3...")
    narrate_with_pyttsx3(text[:3000])  
    print("✅ Done!")
