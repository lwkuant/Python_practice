def sum_sequence(n):
    if n == 1:
        return 1
    else:
        return n + sum_sequence(n-1)
