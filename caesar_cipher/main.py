from alphabet_list import alphabet
from art import logo

def caesar_cipher(start_text, shift_amount, cipher_direction):
    #encode or decode 선택
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        #letter외에 심볼이나 숫자가 있을경우
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here is the {cipher_direction}d result: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" ).lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar_cipher(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if restart =="no":
        should_continue = False
        print("Goodbye!")

        
        