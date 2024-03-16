#write the reccursive program to print digits in reverse order

def rev(n):
    if n==0:
        return
    print(n%10)
    return rev(n//10)
    
n=int(input("enter: "))
rev(n)
