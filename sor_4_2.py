def fibon(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibon(n-2)+fibon(n-1)

for i in range(1,31):
    print(fibon(i),end=" ")
