def carp(n):
    if n==1:
        return 1
    else:
        return n*carp(n-1)
