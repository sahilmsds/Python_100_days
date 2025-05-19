# students = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# max_score = 0
# for score in students:
#     if score > max_score:
#         max_score = score

# print(max_score)
# sum_total = 0
# for i in range(1,101):
#     sum_total += i

# print(sum_total)
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)