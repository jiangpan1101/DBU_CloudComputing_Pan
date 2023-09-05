# Full Name: Pan Jiang
# Student ID: 1104986
# Assignment Due Date: 03/05/2023
# MSITM 6341: Spring 2023
# Assignment #5
# Assignment Title: working with if statement



full_name = "Pan Jiang"


full_name_letters = ""
full_name_ascii = ""

print(full_name.title())

print("-" * len(full_name))

for letter in full_name:
   
    if letter.isupper():
        letter = letter.lower()
    else:
        letter = letter.upper()

    full_name_letters += letter + "-"

    full_name_ascii += str(ord(letter)) + "-"

    print(f"ASCII value of {letter} is {ord(letter)}")

print(full_name_letters[:-1])
print(full_name_ascii[:-1])


print("-" * len(full_name))




