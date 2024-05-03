import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''Way 1'''
# Create an empty list
password = []
# Generate random letters
for n in range(nr_letters):
    password.append(random.choice(letters))
# Generate random symbols
for n in range(nr_symbols):
    password.append(random.choice(symbols))
# Generate random numbers
for n in range(nr_numbers):
    password.append(random.choice(numbers))
# Join the character to form the password string
final_password = ''.join(password)
print(f'Here is your password: {final_password}')

'''Way 2'''
password = ''
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Create an empty list
password = []
# Generate random letters
for n in range(nr_letters):
    password.append(random.choice(letters))
# Generate random symbols
for n in range(nr_symbols):
    password.append(random.choice(symbols))
# Generate random numbers
for n in range(nr_numbers):
    password.append(random.choice(numbers))
# Shuffle the password characters
random.shuffle(password)
# Join the character to form the password string
final_password = ''.join(password)
print(f'Here is your password: {final_password}')



