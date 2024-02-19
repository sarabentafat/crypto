import string
import random 

# Generate all possible characters
all_chars = string.ascii_letters + string.digits + string.punctuation

# Count the number of characters
key_length = len(all_chars)
key=list(all_chars)
random.shuffle(key) # Shuffles key in place

print("#" * 30)
# print("All Characters:", all_chars)
# print("Key Length:", key_length)
# print(key)
plain_text=input("enter your plain text")
ciphered_text=""
for letter in plain_text:
    index=all_chars.index(letter)
    ciphered_text += key[index]
   
print(ciphered_text)
plain=""
# decryption 
for letter in ciphered_text:
    index=key.index(letter)
    plain += all_chars[index]

print(plain)

