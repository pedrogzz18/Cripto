def cesar_encrypt(message:str, key:int, alphabet:list[str]):
    n = len(message)
    a = len(alphabet)

    message = message.upper()
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i].upper()

    encrypt_message = ""

    for i in range(n):
        if(message[i] == " "):
            encrypt_message += " "
        else:
            encrypt_message += (alphabet[(alphabet.index(message[i]) + key)%a])
    
    return encrypt_message

def cesar_decrypt(message:str, key:int, alphabet:list[str]):
    n = len(message)
    a = len(alphabet)

    message = message.upper()
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i].upper()

    decrypt_message = ""

    for i in range(n):
        if(message[i] == " "):
            decrypt_message += " "
        else:
            decrypt_message += (alphabet[(alphabet.index(message[i]) - key)%a])
    
    return decrypt_message


