def format_city(city: str, country: str, population: int = 0) -> str:
    formatted_city = f"{city.title()}, {country.title()}"
    if population > 0:
        formatted_city += f" - population {population}"
    return formatted_city
