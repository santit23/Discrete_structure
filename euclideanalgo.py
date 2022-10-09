a = 7293
b = 4389

def primeornot(x, y):
    flag1 = False
    flag2 = False
    if x>1:
        for i in range(2, x):
            if (x%i)==0:
                flag1 = True
                break
    if y>1:
        for i in range(2, y):
            if (y%i)==0:
                flag2 = True
                break

    if flag1==True and flag2==True:
        return True
    else:
        return False    

def gcd(x, y):
    if primeornot(x, y) == False:
        return 1
    r = x%y
    while r!=0:
        x=y
        y=r
        r=x%y
    return y

print(gcd(a,b))
