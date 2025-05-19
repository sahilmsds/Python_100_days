# def greet():
#     print("Hello guys")
#     print("Wish you a very happy returns of the Day.")
#     print("May God bless you")


# greet()

# def life_in_weeks(age):
#     years = 90 - age
#     weeks = years * 52
#     return weeks

# weeks_remaining = life_in_weeks(56)
# print(f"You have {weeks_remaining} weeks left.")

def calculate_love_score(name1, name2):
    name = name1 + name2
    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")
    true = t + r + u + e
    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    e = name.count("e")
    love = l + o + v + e
    score = str(true) + str(love)
    print(score)
    
calculate_love_score(name1 = "Kanye West", name2 = "Kim Kardashian")