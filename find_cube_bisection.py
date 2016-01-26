def find_cube():
    x = float(raw_input("Enter the number which you want to find its cube root: "))
    eps = 10e-5
    low = 0.0
    hi = abs(x)
    mid = (hi + low)/2
    
    while (abs(mid**3 - abs(x)) > eps):
        if mid**3 > abs(x):
            hi = mid
            mid = (hi + low)/2
        else:
            low = mid
            mid = (hi + low)/2
    return round((mid if x > 0 else -mid),4)