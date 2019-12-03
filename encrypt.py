def encrypt(eKey):
    #takes message for encryption
    message = input("Input message for encryption: ")
    message = list(message)
    
    for i in range(0,len(message)):
        #makes sure only alphanumeric values are encrypted so no hypens or spaces
        if message[i].isalpha():
            if message[i].isupper():
                #converts from ascii to alphabet number, ie A = 1
                message[i] = ord(message[i]) - 64
                #encrypts as according to encryption key and changes back to ascii
                message[i] = chr((message[i] ** eKey[0] % eKey[1]) % 26 + 65)
            elif message[i].islower():
                #converts from ascii to alphabet number, ie A = 1
                message[i] = ord(message[i]) - 96
                #encrypts as according to encryption key and changes back to ascii
                message[i] = chr((message[i] ** eKey[0] % eKey[1]) % 26 + 97)
                
    message = ''.join(message)
    return message
