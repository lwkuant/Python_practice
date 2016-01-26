def distance(a,b):
    import math
    return round(math.sqrt(sum([(float(cor1 - cor2))**2 for cor1, cor2 in zip(a, b)])),2)
    
