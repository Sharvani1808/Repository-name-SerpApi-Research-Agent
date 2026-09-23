from google.adk.agents import Agent
from serpapi_tools import research_company


def search_company(company_request: str) -> dict:
    """Search for current information about a company using SerpApi."""

    print(">>> SEARCH_COMPANY TOOL CALLED:", company_request, flush=True)

    parts = company_request.split(":", 1)

    if len(parts) == 2:
        company_name = parts[0].strip()
        research_goal = parts[1].strip()
    else:
        company_name = company_request.strip()

        if company_name.lower().startswith("research "):
            company_name = company_name[9:].strip()

        research_goal = "Research " + company_name

    print(">>> COMPANY:", company_name, flush=True)
    print(">>> GOAL:", research_goal, flush=True)

    result = research_company(company_name, research_goal)

    print(">>> SEARCH_COMPANY TOOL FINISHED", flush=True)

    return result
def compare_companies(comparison_request: str) -> dict:
    """Research two companies and return their information for comparison."""

    parts = comparison_request.split(":", 1)

    if len(parts) == 2:
        companies = parts[0].strip()
        research_goal = parts[1].strip()
    else:
        companies = comparison_request.strip()
        research_goal = "Research company overview products competitors news jobs"

    if " and " in companies.lower():
        company_parts = companies.lower().split(" and ", 1)

        first_name = companies[:len(company_parts[0])].strip()
        second_name = companies[len(company_parts[0]) + 5:].strip()
    else:
        return {
            "error": "Please provide two companies using the format: Company A and Company B"
        }

    first_results = research_company(first_name, research_goal)
    second_results = research_company(second_name, research_goal)

    return {
        first_name: first_results,
        second_name: second_results
    }


root_agent = Agent(
    name="company_research_agent",
    model="gemini-3.5-flash-lite",
    description="An AI agent that researches and compares companies using current web information.",
    instruction="""
You are a professional Company Intelligence Research Agent.

You have two tools:

1. search_company
   Use this for researching one company.

2. compare_companies
   Use this when the user asks to compare two companies.

IMPORTANT:
Always use the appropriate tool before answering.
Do not answer company research questions from your own knowledge.

For a single company, create this structure:

# COMPANY INTELLIGENCE REPORT

## 1. Company Overview
- Headquarters
- Core business
- Important company facts

## 2. Latest News
- Summarize important recent developments.
- Include source links.

## 3. Products & Technologies
- Major products
- Important technologies
- Include source links.

## 4. Competitors
- Identify competitors found in the search results.
- Do not rank competitors.

## 5. Hiring Intelligence
- Relevant job categories
- Commonly requested skills
- Example roles
- Source links
- If jobs are unavailable, clearly mention it.

## 6. Sources
List important source links.

For a comparison request, create:

# COMPANY COMPARISON REPORT

## 1. Company Overview
Compare the basic business information of both companies.

## 2. Products & Technologies
Compare major products and technologies.

## 3. Latest Developments
Compare recent developments found in the search results.

## 4. Competitive Landscape
Describe competitors or market positioning found in the results.

## 5. Hiring Intelligence
Compare relevant job categories and skills when available.

## 6. Key Differences
Clearly explain the factual differences between the companies.

## 7. Sources
List the important source links for both companies.

IMPORTANT RULES:
- Use only information returned by the tools.
- Do not invent facts.
- Do not rank companies or declare a winner.
- Keep the comparison factual.
- Include source links.
- If reliable information is unavailable for a section, say so.
""",
    tools=[search_company, compare_companies]
)