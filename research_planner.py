def create_research_plan(company_name, research_goal):
    """Create a focused and efficient research plan."""

    goal = research_goal.lower()

    # Career / jobs research
    if "job" in goal or "career" in goal or "hiring" in goal:
        return [
            f"{company_name} {research_goal}",
            f"{company_name} careers skills requirements"
        ]

    # News research
    if "news" in goal or "recent" in goal or "latest" in goal:
        return [
            f"{company_name} latest news",
            f"{company_name} recent developments"
        ]

    # AI research
    if "ai" in goal or "artificial intelligence" in goal:
        return [
            f"{company_name} AI products",
            f"{company_name} AI technologies",
            f"{company_name} AI latest news",
            f"{company_name} AI competitors"
        ]

    # Product research
    if "product" in goal or "technology" in goal or "technologies" in goal:
        return [
            f"{company_name} products",
            f"{company_name} technologies",
            f"{company_name} latest products"
        ]

    # Competitor research
    if "competitor" in goal or "competition" in goal:
        return [
            f"{company_name} competitors",
            f"{company_name} competitors latest"
        ]

    # Financial research
    if "financial" in goal or "revenue" in goal or "earnings" in goal:
        return [
            f"{company_name} financial results",
            f"{company_name} revenue earnings",
            f"{company_name} financial news"
        ]

    # Full company research
    if (
        "research" in goal
        or "full" in goal
        or "intelligence" in goal
        or "general" in goal
    ):
        return [
            f"{company_name} company overview",
            f"{company_name} latest news",
            f"{company_name} competitors",
            f"{company_name} products",
            f"{company_name} jobs careers"
        ]

    return [f"{company_name} company overview"]