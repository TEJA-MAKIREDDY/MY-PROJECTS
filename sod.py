#count the sum of digits in a given number

def sod(n):
    
    if n==0:
        return 0
    return n%10+sod(n//10)
n=int(input("enter: "))
print(sod(n))
