alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
direction = input("Type 'encode' to encrypt, and 'decode' to decrypt").lower()
text = input("Enter the message:\n")
shift_number = int(input("Enter the shift number"))


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabets:
            char_num = alphabets.index(char)
            if direction == "decode":
                letter = alphabets[(char_num - shift) % len(alphabets)]
            elif direction == "encode":
                letter = alphabets[(char_num + shift) % len(alphabets)]
            else:
                print("Invalid direction. Please enter 'encode' or 'decode'.")
                return ""
            encrypted_text += letter
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text


print(caesar_cipher(text,shift_number))