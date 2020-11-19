import random
a=random.randrange(10,99)
while a%11==0:
    a=random.randrange(10,99)

x=0
while x!=a:
    x=int(input("Lütfen 10 ile 98 arasında bir sayı giriniz: "))
    dogruyer=0
    yanlisyer=0
    while x<10 or 98<x:
        x=int(input("Lütfen 10 ile 98 arasında bir sayı giriniz: "))
    else:
        if str(a)[0]==str(x)[0] or str(a)[1]==str(x)[1]:
            dogruyer+=1
            print("dogruyer=" , dogruyer)
   
        elif str(a)[::-1]==str(x):
            yanlisyer+=2
            print("yanlışyer=" , yanlisyer)
        elif str(a)[0]==str(x)[1] or str(a)[1]==str(x)[0]:
            yanlisyer+=1
            print("yanlışyer=" , yanlisyer)
        else:
            print("skor 0 ")
        
else:
    print("tebrikler ", a ,"sayısını buldunuz")
        
                
