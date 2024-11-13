def encrypt (plain_text, shift):
    encrypted_text = ""

    for char in plain_text:
# Encrypt uppercase letters
         if char. isupper():
            encrypted_text += chr((ord (char) + shift - 65) & 26 + 65)
# Encrypt lowercase letters
         elif char.islower():
              encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
         else:
# Non-alphabetic characters remain unchanged
              encrypted_text += char
              
    return encrypted_text
def decrypt(encrypted_text, shift):
    decrypted_text = I
    for char in encrypted_text:
# Decrypt uppercase letters
        if char. isupper():
           decrypted_text += chr((ord (char) - shift - 65) % 26 + 65)
# Decrypt lowercase letters
        elif char. islower():
             decrypted_text += chr( (ord (char) - shift - 97) % 26 + 97)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            #Non-alphabetic characters remain unchanged
            decrypted_text += char

        return decrypted_text
    
    #Main function to demonstrate encryption and decryption
if __name__ == "__main__":
    #input from the user 
    plain_text = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value (1-25): "))

    #Encrypt the message
    encrypted = encrypt(plain_text, shift)
    print(f"Encrypted Message: {encrypted}")

    #Decrypt the message
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted Message: {decrypted}")
        