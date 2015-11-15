def Findlongest(str):
    container_num = range(len(str))  
              
    for i in range(len(str)):
        n = 1
        j = i
        while (j != (len(str)-1)) and (str[j] <= str[j+1]):
            n += 1
            j += 1
        container_num[i] = n

        ind = container_num.index(max(container_num))
        
    return str[ind:ind+max(container_num)]                                                            
                        
    
