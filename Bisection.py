def find_sqrt(n):
    assert n >= 0
    high = n
    low = 0
    cen = (high+low)/2.0
    eps = 1e-5

    while abs(cen**2-n) >= eps:
        if cen**2 > n:
            high = cen
            cen = (high+low)/2
        else:
            low = cen
            cen = (high+low)/2
    return cen             
