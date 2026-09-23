from serpapi_tools import search_web

results = search_web("NVIDIA latest news")

print("\n===== SEARCH RESULTS =====\n")

for i, result in enumerate(results[:5], 1):
    print(f"{i}. {result.get('title')}")
    print(f"   {result.get('link')}")
    print()