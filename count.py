#count the no. of digits in a given number

def cod(n):
    
    if n==0:
        return 0
    return 1+cod(n//10)
n=int(input("enter: "))
print(cod(n))

