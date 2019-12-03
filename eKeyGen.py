def eKey(N,phiN):
    import numpy as np
    
    #generates factors of both N and phiN
    factors_N= []
    factors_N = np.array(factors_N,dtype=int)
    for i in range(2,N):
        if N % i == 0:
            factors_N = np.append(factors_N, i)
    factors_phiN = []
    factors_phiN = np.array(factors_phiN,dtype=int)
    for i in range(2,phiN):
        if phiN % i == 0:
            factors_phiN = np.append(factors_phiN, i)
            
    #creates list of possible encryption key values
    possible_e = []
    possible_e = np.array(possible_e,dtype=int)
    for i in range(2,phiN):
        possible_e = np.append(possible_e, i)
        
    #if possible eKey values aren't coprime with N or phiN, it removes them
    for i in range(0,len(possible_e)):
        for j in range(0,len(factors_N)):
            if possible_e[i] % factors_N[j] == 0:
                possible_e[i] = 0
    for i in range(0,len(possible_e)):
        for j in range(0,len(factors_phiN)):
            if possible_e[i] % factors_phiN[j] == 0:
                possible_e[i] = 0
                
    #saves all possible eKey values in vector true_e
    true_e = []
    true_e = np.array(true_e,dtype=int)
    for i in range(0,len(possible_e)):
        if possible_e[i] != 0:
            true_e = np.append(true_e, possible_e[i])
    return true_e