def rev(str):
    str_new = ""
    for i in range(len(str)):
        str_new += str[len(str)-i-1]
    return str_new        
