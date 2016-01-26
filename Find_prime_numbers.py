def find_prime(n):
    prime_ls = []
    j = 2
    while(j <= n):
        ceil = j**0.5
        i = 2
        check = True 
        while(i <= ceil):
            if (j % i == 0):
                check = False
                break
            i += 1
        if check == True:                                
            prime_ls.append(j)                        
        j += 1
    return prime_ls
                                                        