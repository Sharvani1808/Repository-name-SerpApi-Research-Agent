import os
import time
import serpapi
from dotenv import load_dotenv
from research_planner import create_research_plan

load_dotenv()

api_key = os.getenv("SERPAPI_API_KEY")
client = serpapi.Client(api_key=api_key)


def search_web(query):
    results = client.search({
        "engine": "google",
        "q": query
    })

    organic_results = results.get("organic_results", [])

    cleaned_results = []

    for result in organic_results[:5]:
        cleaned_results.append({
            "title": result.get("title"),
            "source": result.get("source"),
            "link": result.get("link"),
            "snippet": result.get("snippet")
        })

    return cleaned_results


def search_jobs(query):
    last_error = None

    for attempt in range(3):
        try:
            results = client.search({
                "engine": "google_jobs",
                "q": query
            })

            jobs = results.get("jobs_results", [])

            cleaned_jobs = []

            for job in jobs[:5]:
                cleaned_jobs.append({
                    "title": job.get("title"),
                    "company": job.get("company_name"),
                    "location": job.get("location"),
                    "via": job.get("via"),
                    "link": (
                        job.get("apply_options", [{}])[0].get("link")
                        if job.get("apply_options")
                        else None
                    )
                })

            return cleaned_jobs

        except Exception as error:
            last_error = str(error)

            if attempt < 2:
                time.sleep(2)

    return [{
        "error": "Google Jobs search is temporarily unavailable.",
        "details": last_error
    }]


def research_company(company_name, research_goal):
    queries = create_research_plan(company_name, research_goal)

    research = {}

    for query in queries:
        if "job" in query.lower() or "career" in query.lower():
            research[query] = search_jobs(query)
        else:
            try:
                research[query] = search_web(query)
            except Exception as error:
                research[query] = [{
                    "error": "Web search temporarily failed.",
                    "details": str(error)
                }]

    return research