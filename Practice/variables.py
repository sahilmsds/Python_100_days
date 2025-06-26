# Write a program that takes a user's name and age, then prints: "Hello [name], you are [age] years old."
user_name = input("What's your name? ")
user_age = int(input("What's your age? "))
print(f"Hello {user_name}, you are {user_age} years old")
# Convert a temperature from Celsius to Fahrenheit.
celsius = 23
fahrenheit = celsius * (9/5) + 32 
print("Fahrenheit: ",fahrenheit)
celcius = fahrenheit - 32 * (5/9)
print("Celsius: ", celsius)

# Ask the user for 2 numbers and print their sum, difference, product, and quotient.
first_num = int(input("Enter first number: "))
second_num = int(input("Now enter second number: "))

def calculate(first_num, second_num):
    print(f"Sum: {first_num + second_num}")
    print(f"Difference: {first_num - second_num}")
    print(f"Product: {first_num * second_num}")
    print(f"Quotient: {first_num / second_num}")

calculate(first_num, second_num)

# Convert a user's height from centimeters to feet and inches.
user_height_cm = float(input("Enter height in cm to convert in Feet and inces: "))
user_height_f = round(user_height_cm / 30.48, 2)
feet = int(user_height_f)
inches = round((user_height_f - feet) * 12)
print(f"Your height is {feet} feet and {inches} inches.")
# Ask the user for a 3-digit number and reverse it (e.g. 123 -> 321).
number = int(input("Enter a number to reverse: "))
hundred = number // 100
tens = number % 100 // 10
ones = number % 10
reversed_num = ones * 100 + tens * 10 + hundred
print("Your reversed number = ", reversed_num)