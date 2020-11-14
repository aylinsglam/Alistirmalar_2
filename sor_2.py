def topla(n):
    if n==1:
        return 1
    else:
        return n+topla(n-1)
