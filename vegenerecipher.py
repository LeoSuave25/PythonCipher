# Style the entire Project
# Repeat the key until it became the same length as the raw_text
def repeat_word(key, raw_text):
    target_length = len(raw_text)
    repeated_word = key * target_length
    if len(raw_text)==len(key):
        return key
    elif len(raw_text)<len(key):
        return key[0:len(raw_text)]
    else:
        return repeated_word[0:len(raw_text)]
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
initial_key = ""
repeated_key = repeat_word(key,plain_text)
for letter in repeated_key:
    initial_letter = ord(letter) - 65
    initial_key += str(initial_letter) + " "
# Display it in a Row
# Add two columns
# Print the Ciphered Text
# Put the program in loop