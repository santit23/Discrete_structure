a = 7
flag = False

if a>1:
    for i in range(2, a):
        if (a%i)==0:
            flag = True

            break

if flag==True:
    print("Not Prime number")

else: 
    print("Prime prime")