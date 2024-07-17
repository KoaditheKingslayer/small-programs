# String Manipulation Exercise: Vigenere Cypher

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

def mainLoop():
    while True:
        text = input("What String to Encrypt/Decrypt? \n")
        custom_key = input("Encryption/Decryption Key?\n")
        encrypt_or_decrypt = input("Encrypt or Decrypt?\n")
        if 'encrypt' in encrypt_or_decrypt.lower():
            print('Encrypted Text: ' + encrypt(text, custom_key) + '\n')
        elif 'decrypt' in encrypt_or_decrypt.lower():
            print('Decrypted Text: ' + decrypt(text, custom_key) + '\n')
        else:
            print('Error!')
        
mainLoop()