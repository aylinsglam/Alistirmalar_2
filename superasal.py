
def asal_mi(n):
    bolenler=list()
    a=int((n/2)+1)
    for i in range(2,a):
        if n%i==0:
            bolenler.append(i)
    if n!=1 and len(bolenler)==0:
        return True
    else:
        return False
    
def super_asal(m):
    while asal_mi(m)==True and 10<m:
        m=int(m/10)
    else:
        if m==2 or m==3 or m==5 or m==7:
            return True
        else:
            return False

for i in range(10001,100000,2):
    if super_asal(i)==True:
        print(i, end=" ")

