import math


x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
af=[]
bf=[]

def prime_or_not(a, b):
    flag1=False
    flag2=False
    if a>1:
        for i in range(2,a):
            if (a%i)==0:
                flag1=True
                break
    if b>1:
         for i in range(2,b):
            if (b%i)==0:
                flag2=True
                break
    if flag1==True and flag2==True:
        return True
    else:
        return False

def gcd(a, b):
    if prime_or_not(x, y)==False:
        return 1
    else:
        for i in range(1, a+1):
            if (a%i)==0:
                af.append(i)
        for i in range(1, b+1):
            if (b%i)==0:
                bf.append(i)
    common = set(af).intersection(bf)
    return max(common)

print("GCD of the number is ", gcd(x,y))
print(math.gcd(x, y))
        
