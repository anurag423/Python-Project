def checkprime(x):
    import math as m
    #checks if number is divisible by any number from 2 to its square root
    counter = 0 
    square_root = int(m.sqrt(x))
    for i in range(2,square_root+1):
        if x % i == 0:
            counter = 1
            
    #if number is divisible by any number from 2 to its square root, it is removed
    if counter == 1 or x == 1:
        print(f'{x} is not a prime. Please retry.')
        user_input = 'try'
        
    else:
        print(f'{x} is a prime. Good job.')
        user_input = 'good'
    #returns user_input so the loop continues in main program
    return user_input