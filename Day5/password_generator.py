import random
print("Welcome to PyPassword generator..")
num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "C", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

simple_password= []
for _ in range(num_letters):
    simple_password.append(random.choice(letters))
for _ in range(num_numbers):
    simple_password.append(random.choice(numbers))
for _ in range(num_symbols):
    simple_password.append(random.choice(symbols))

random.shuffle(simple_password)
final_password = ""
for let in simple_password:
    final_password += let

print(final_password)