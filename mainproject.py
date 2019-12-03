import primegen
import checkprime
import phiN
import eKeyGen
import random
import encrypt

#takes user input for either generating prime numbers or testing users numbers
user_input = input('Do you want to try prime numbers or generate them? ').lower()

#if user wants to try their numbers, it runs a while loop until user's inputs are both prime
while user_input == 'try':
    p = int(input('(Hidden) P Value: '))
    q = int(input('(Hidden)) Q Value: '))
    user_input_p = checkprime.checkprime(p)
    user_input_q = checkprime.checkprime(q)
    if user_input_p == 'try' or user_input_q == 'try':
        user_input = 'try'
    else:
        user_input = 'good'
        
#if user wants to generate their number, it generates 2 prime numbers with specified bits and encrypts
if user_input == 'generate':
    p,q = primegen.primegen()
    N = p * q
    print(f'(Public)N = {N}')
    phiN = phiN.phiN(N)
    print(f'(Hidden)phiN = {phiN}')
    e_true = eKeyGen.eKey(N,phiN)
    eKey = random.choice(e_true),N
    print(f'(Public)Encryption Key  = {eKey}')
    message = encrypt.encrypt(eKey)
    print(f'Your Cipher Text is: {message}')
    
#when users inputs are both correct prime numbers, it encrypts
elif user_input == 'good':
    N = p * q
    print(f'(Public)N = {N}')
    phiN = phiN.phiN(N)
    print(f'(Hidden)phiN = {phiN}')
    e_true = eKeyGen.eKey(N,phiN)
    eKey = random.choice(e_true),N
    print(f'(Public)Encryption Key  = {eKey}')
    message = encrypt.encrypt(eKey)
    print(f'Your Cipher Text is: {message}')

#if user inputted something wrong, it spits out error code
else:
    print(f'Please read manual')
