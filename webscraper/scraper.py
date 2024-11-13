import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# URL til den side, du vil scrape
url = "https://www.cokogames.com/simon-says-online-game/play/"

# Laver en mappe til at gemme billederne
os.makedirs("freesimon_images", exist_ok=True)

# Henter HTML-indholdet fra siden
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Finder alle billedfiler (img tags)
images = soup.find_all("img")

# Download billederne
for img in images:
    img_url = img.get("src")
    img_url = urljoin(url, img_url)  # Sikrer, at URL'en er fuld

    # Filnavn til at gemme billedet
    filename = os.path.join("freesimon_images", os.path.basename(img_url))

    # Downloader billedet
    with open(filename, "wb") as f:
        img_data = requests.get(img_url).content
        f.write(img_data)
        print(f"Downloaded {filename}")

print("Alle billeder er nu downloadet.")
