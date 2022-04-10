

#Encryption

caesar_logo = """
   ___                               ___ _       _               
  / __\__ _  ___  ___  __ _ _ __    / __(_)_ __ | |__   ___ _ __ 
 / /  / _` |/ _ \/ __|/ _` | '__|  / /  | | '_ \| '_ \ / _ \ '__|
/ /__| (_| |  __/\__ \ (_| | |    / /___| | |_) | | | |  __/ |   
\____/\__,_|\___||___/\__,_|_|    \____/|_| .__/|_| |_|\___|_|   
                                          |_|                    
"""
def encryptLetter(letter,position):
    number_loop_to_beginning  = 26
    number_letter = ord(letter)
    shifted_number_letter = number_letter+position
    if(shifted_number_letter>122):
        shifted_number_letter = shifted_number_letter-number_loop_to_beginning
    return chr(shifted_number_letter)

# def encryptSentence(sentence,position_move):
#     encrypted_word = ""
#     for letter in sentence:
#         encrypted_word +=encryptLetter(letter,position_move)
#     return encrypted_word
#Decryption

def decryptLetter(letter,position):
    number_loop_alphabet = 26
    number_of_encryptedalphabet = ord(letter)
    number_original = number_of_encryptedalphabet-position
    if(number_original<97):
        number_original = number_original+number_loop_alphabet
    return chr(number_original)

# def decryptSentence(encrypted_word,position_move):
#     decrypted_word = ""
#     for letter in encrypted_word:
#         decrypted_word +=decryptLetter(letter,position_move)
#     return decrypted_word

def caesarCipher(encrypt_or_decrypt,word,position_move):
    answer = ""
    for letter in word:
        if(encrypt_or_decrypt == "encrypt"):
            answer +=encryptLetter(letter,position_move)
        else:
            answer +=decryptLetter(letter,position_move)
    return answer


#Program Logic    
print("Welcome to my Supavich Caesar Cipher, let explore the world on encryption!")
print(caesar_logo)
encrypt_or_decrypt = input("Would you like to encrypt or decrypt a text?'encrypt' or 'decrypt'")
user_word = input("What word would you like to encrypt/decrypt using Caesar Cipher?")
position_move = int(input("How many position would you like to move?"))

# user_encrypted_word = encryptSentence(user_word,position_move)
# print(f"The encryption of the word {user_word} is {user_encrypted_word}")

            
answer = caesarCipher(encrypt_or_decrypt,user_word,position_move)
print(f'Your {"Encrypt" if (encrypt_or_decrypt=="encrypt") else "Decrypt"} word is {answer}')

# user_decrypted_word = decryptSentence(user_encrypted_word,position_move)
# print(f"The decryption of the word {user_encrypted_word} is {user_decrypted_word}")
#END OF LOGIC