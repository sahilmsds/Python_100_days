# travel_log = {
#     "Paris": ["London", "Berlin", "Madrid"],
#     "France": ["Paris", "Lille", "Nice"],
# }
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D", ["E", "F"]], "G"]
# # print D
# print(nested_list[2][1])

travel_log = {
    "France":
        {
            "cities_visited": ["Paris", "Lille", "Nice"],
            "total_visits": 12,
        },
    "Germany":
        {
            "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
            "total_visits": 5,
        }
}
print(travel_log["France"]["cities_visited"])