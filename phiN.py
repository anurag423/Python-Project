def phiN(N):
    #function calculates Euler's Totient number, which is the amount of numbers that are relatively prime with N
    import numpy as np
    
    #checks how many factors of the N value exist   
    factors = []
    factors = np.array(factors,dtype=int)
    for i in range(2,N):
        if N % i == 0:
            factors = np.append(factors, i)
            
    #removes numbers that are not relatively prime N
    coprimes = []
    coprimes = np.array(coprimes,dtype=int)
    for i in range(1,N):
        coprimes = np.append(coprimes, i)
    for i in range(0,len(coprimes)):
        for j in range(0,len(factors)):
            if coprimes[i] % factors[j] == 0:
                coprimes[i] = 0    
                
    #creates list of numbers that are relatively prime with N        
    final_coprimes = []
    final_coprimes = np.array(final_coprimes,dtype=int)
    for i in range(0,len(coprimes)):
        if coprimes[i] != 0:
            final_coprimes = np.append(final_coprimes, coprimes[i])
            
    #checks how many numbers are relatively prime with N and outputs it as phiN
    phiN = len(final_coprimes)
    return phiN
    