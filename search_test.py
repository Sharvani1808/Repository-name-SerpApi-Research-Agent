import os
from dotenv import load_dotenv
import serpapi

load_dotenv()

api_key = os.getenv("SERPAPI_API_KEY")
client = serpapi.Client(api_key=api_key)

results = client.search({
    "engine": "google",
    "q": "latest NVIDIA news"
})

print("\n===== NVIDIA NEWS SEARCH =====\n")

for i, result in enumerate(results.get("organic_results", [])[:5], 1):
    print(f"{i}. {result.get('title')}")
    print(f"   Source: {result.get('link')}")
    print(f"   Info: {result.get('snippet')}")
    print()