# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?

import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted = ""
    for letter in original_text:
        if letter.isalpha():
            base=ord('a')
            shifted=(ord(letter)-base+shift_amount)%26+base
            encrypted+=chr(shifted)
        else:
            encrypted+=letter
    print(f"Here is the encoded result: {encrypted}")
def decrypt(original_text,shift_amount):
    decrypted = ""
    for letter in original_text:
        if letter.isalpha():
            base = ord('a')
            shifted = (ord(letter)-base-shift_amount)%26+base
            decrypted += chr(shifted)
        else:
            decrypted+=letter
    print(f"Here is the decoded result: {decrypted}")
def caesar_cipher():
    k=True
    while k:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))%26
        if direction=='encode':
            encrypt(text,shift)
        elif direction=='decode':
            decrypt(text,shift)
        choice=input("Type yes if you want to go again, Otherwise, type 'no'.").lower()
        if choice=='yes':
            k=True
        else:
            k=False

caesar_cipher()



