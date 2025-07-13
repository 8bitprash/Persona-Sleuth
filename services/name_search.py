import os, httpx
from typing import List, Dict

SERP_KEY = os.getenv("SERPAPI_KEY")

async def search_name_google(name: str) -> List[Dict]:
    params = {
        "q": f'"{name}" site:linkedin.com OR site:twitter.com',
        "api_key": SERP_KEY,
        "num": 10,
    }
    async with httpx.AsyncClient() as client:
        r = await client.get("https://serpapi.com/search.json", params=params, timeout=10)
    r.raise_for_status()
    results = r.json().get("organic_results", [])
    return [
        {"name": item.get("title", ""), "link": item.get("link", ""),
         "snippet": item.get("snippet", ""), "source": "google"}
        for item in results
    ]
