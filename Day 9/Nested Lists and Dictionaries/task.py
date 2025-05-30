capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested List in Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Stuttgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C","D"]]
#print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visitors": 12
    },
    "Germany":{
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visitors": 5
    },
}