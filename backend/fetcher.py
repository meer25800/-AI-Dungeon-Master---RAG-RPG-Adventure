import requests
import json
from pathlib import Path

BASE_DIR = Path("data/fetched/")
BASE_DIR.mkdir(parents=True, exist_ok=True)

def fetch_open5e(endpoint: str, name: str):
    url = f"https://api.open5e.com/{endpoint}/"
    all_results = []
    while url:
        res = requests.get(url)
        data = res.json()
        all_results.extend(data["results"])
        url = data["next"]
    with open(BASE_DIR / f"{name}.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)

if __name__ == "__main__":
    fetch_open5e("spells", "spells")
    fetch_open5e("monsters", "monsters")
    fetch_open5e("magicitems", "magicitems")