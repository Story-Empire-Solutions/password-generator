#Programme to generate passwords using the combination of letters, numbers and special characters.

import random

print("\nWELCOME TO THE PASSWORD GENERATOR PROGRAMME!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '', ']', '^', '_', '{', '|', '}', '~']

#Accept inputs from the user.
letter_characters = int(input("\nEnter the number of letters you want in your password: "))
number_characters = int(input("Enter the number of numbers you want in your password: "))
symbol_characters = int(input("Enter the number of symbols you want in your password: "))

characters_total = letter_characters + number_characters + symbol_characters
print(f"\nThe total number of characters you want is: '{characters_total}'  characters.")

#Create an empty string variable that will hold the characters
password = ""

#Set up the for loop that will generate the password.
for character in range(letter_characters):
    password = password + random.choice(letters)

for character in range(number_characters):
    password = password + random.choice(numbers)

for character in range(symbol_characters):
    password = password + random.choice(symbols)