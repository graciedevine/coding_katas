from city_functions import get_city_name

print("Enter q at any time to quit")
while True:
    city = input("Type a city name: ")
    if city == "q":
        break
    country = input("Type a country name: ")
    if country == "q":
        break

    formatted_name = get_city_name(city, country)
    print(f"\tNeatly formatted name: {formatted_name}.")
