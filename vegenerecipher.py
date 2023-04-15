# Style the entire Project
# Repeat the key until it became the same length as the raw_text
# Ask User text and save it to variable, validate it to be uppercase letters with no spaces
while True:
    plain_text = input("Enter your Text: ")
    if plain_text.isupper() and ' ' not in plain_text:
        break
    else:
        print("Invalid input! Please enter text in uppercase and with no spaces.")
# Convert every letters in the text into numbers(0-25)
initial_text = ""
for letter in plain_text:
    initial_letter = ord(letter) - 65
    initial_text += str(initial_letter) + " "
# Ask user for the key
while True:
    key = input("Enter your key: ")
    if key.isupper() and ' ' not in plain_text:
        break
    else:
        print("Invalid input! Please enter text in uppercase and with no spaces.")
# Convert every letters in the text into numbers(0-25)
# Display it in a Row
# Add two columns
# Print the Ciphered Text
# Put the program in loop