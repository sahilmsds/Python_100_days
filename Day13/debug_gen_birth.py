# year = int(input("What's your birth year? "))
# if year >1980 and year < 1994:
#     print("You are Millennial")
# elif year > 1994:
#     print("You are GenZ.")

# Below code is the corrected version of above code
year = int(input("What's your birth year? "))
if year > 1980 and year <= 1994:
    print("You are Millennial")
elif year > 1994:
    print("You are GenZ.")