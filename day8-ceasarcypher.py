alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Encrypt Function
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


# Decrypt Funtion
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


# Single function to decrypt or encrypt
def ceasar(message, shift_amount, method):
    out_text = ""
    if method == "decode":
        shift_amount *= -1

    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            out_text += alphabet[new_position]
        else:
            # If char is not in the alphabet just add it back to the string
            out_text += char

    print(f"The {method}d result: {out_text}\n")


user_repeat = "yes"
while user_repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    ceasar(message=text, shift_amount=shift, method=direction)

    user_repeat = input("Do you want to continue (Yes or No): ").lower()

print("Good Bye!")