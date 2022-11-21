travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(visited_country, num_of_visits, visited_cities):
    travel_log.append({
        "country": visited_country,
        "visits": num_of_visits,
        "cities": visited_cities
    })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
