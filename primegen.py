def primegen():
    import numpy as np
    #asks user how many bits they want for P and Q values
    bits = int(input('How many bits? '))
    final = 2 ** bits
    
    #creates vector of values to final(2**bits)
    ints_to_final = list(range(2,final+1))
    ints_to_final = np.array(ints_to_final)
    
    #starts counter for operations at 0
    index = 0
    
    #while counter is less than the len of array, runs operations for prime generation
    while index < len(ints_to_final):
        #creates vector that removes numbers that are multiples of counter
        del_vect = []
        del_vect = np.array(del_vect)
        #for i in range 0 to current length of ints_to_final. run operation on each value
        for i in range(0,len(ints_to_final)):
            #if value is equal to counter, it is not counted as a composite
            if ints_to_final[i] == ints_to_final[index]:
                #puts zero in del_vect so that number is not removed
                del_vect = np.append(del_vect, 0)
            #if value is not equal to counter check if prime or not
            else:
                #check if number is a multiple of counter
                if ints_to_final[i] % ints_to_final[index] == 0:
                    #if number is a multiple of the counter, places in del_vect
                    del_vect = np.append(del_vect, ints_to_final[i])
                #if number is not a multiple of the counter, places zero in del_vect
                else:
                    del_vect = np.append(del_vect, 0)
        #for each counter value, ints_to_finals removes multiples of the counter
        ints_to_final = ints_to_final - del_vect    
        ints_to_final = ints_to_final[ints_to_final != 0]
        #raises counter by one, this checks if operation should stop and starts counter on next index value
        index = index + 1
        
    #prints and gives p and q values to main program
    random1 = int(np.random.choice(ints_to_final,1))
    print(f'(Hidden) P Value: {int(random1)}')
    random2 = int(np.random.choice(ints_to_final,1))
    print(f'(Hidden) Q Value: {int(random2)}')
    return random1,random2
