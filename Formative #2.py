def shift_letter(letter, shift):
    if letter == " ":
        return " "
        
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    index = alphabet.index(letter)
    shifted_index = (shift + index) % 26
    letter_result = alphabet[shifted_index]
    return letter_result

def caesar_cipher(message, shift):
    translated = []
    for letter in message:
        if letter == " ":
            translated.append(" ")
        else:
            alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            index = alphabet.index(letter)
            shifted_index = (shift + index) % 26
            translated.append(alphabet[shifted_index])

    return "".join(translated)

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " " 

    else:
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        index_letter = alphabet.index(letter)
        index_letter_shift = alphabet.index(letter_shift)
        index_shift = (index_letter_shift + index_letter) % 26 
        letter_result = alphabet[index_shift] 
    
    return letter_result 

def vigenere_cipher(message, key):
    key_cover = key * (len(message) // len(key)) + key[:len(message) % len(key)]

    keyphrase = []
    key_index = 0
    for letter in message:
        if letter == " ":
            keyphrase.append(" ")
            key_index += 1
        else:
            alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            index_message = alphabet.index(letter)
            index_key = alphabet.index(key_cover[key_index])
            index_shift = (index_message + index_key) % 26
            keyphrase.append(alphabet[index_shift])
            key_index += 1

    return "".join(keyphrase)

def scytale_cipher(message, shift):
    if len(message) % shift == 0:
        message_to_construct = message
    else:
        message_to_construct = message + "_" * (shift - len(message) % shift)

    scytale = ""
    for i in range(len(message_to_construct)): 
        scytale += message_to_construct[(i // shift) + (len(message_to_construct) // shift) * (i % shift)] 
    
    return scytale

def scytale_decipher(message, shift): 
    decipher = ""
    for i in range(shift):
        for j in range(len(message) // shift):
            decipher += message[j * shift + i]
       
    return decipher


