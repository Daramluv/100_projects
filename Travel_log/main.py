#dictionary_in_list
from travel_log import travel_log as t_log
country = input("Type the country you visited:\n ")
visits = int(input("Type number of visits:\n "))
list_of_cities = input("create list of cities you visited:\n")
list_cities = list_of_cities.split(",")

def new_log(name, times, city_list):
    n_log = {}
    n_log["country"] = name
    n_log["visits"] = times
    n_log["list_cities"] = city_list
    t_log.append(n_log)
    

new_log(country, visits, list_cities)

print(f"I've been to {t_log[2]['country']} {t_log[2]['visits']} times.")
print(f"My favourite city was {t_log[2]['list_cities'][0]}")


    