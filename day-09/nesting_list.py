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

def add_new_country(country, visits, cities):
    travel_log.append(
        {
            "country": country,
            "visits": visits,
            "cities": cities,
        }
    )

    # print(f"You've visited {country} {visits} times.")
    # print(f"You've been to {cities[0]} and {cities[1]}")




add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# add_new_country("Brazil", 2, ["São Paulo", "Rio de janeiro"])
print(travel_log)