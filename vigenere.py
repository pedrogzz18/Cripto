import numpy as np

def vigenere_encrypt(message:str, key:str, alphabet:list[str]):

 
    n = len(message)
    m = len(key)
    a = len(alphabet)

    ptr_key = 0

    message = message.upper()
    key = key.upper()
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i].upper()

    encrypt_message = ""

    for i in range(n):
        if(message[i] == " "):
            encrypt_message += " "
        else:
            encrypt_message += (alphabet[(alphabet.index(message[i]) + alphabet.index(key[ptr_key%m]))%a])
            ptr_key += 1
    
    return encrypt_message

def vigenere_decrypt(message:str, key:str, alphabet:list[str]):

    n = len(message)
    m = len(key)
    a = len(alphabet)

    ptr_key = 0

    message = message.upper()
    key = key.upper()
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i].upper()

    encrypt_message = ""

    for i in range(n):
        if(message[i] == " "):
            encrypt_message += " "
        else:
            encrypt_message += (alphabet[(alphabet.index(message[i]) - alphabet.index(key[ptr_key%m]))%a])
            ptr_key += 1
    
    return encrypt_message
