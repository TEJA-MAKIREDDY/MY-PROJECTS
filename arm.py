def count(n): 
    if(n==0):
        print(n%10,end="")
        return 0
    else:
        return 1+count(n//10)
def arms(n,c):
    if(n>0):
        dig=n%10
        return dig**c+arms(n//10,c)
    else:
        return 0
       
n=int(input("Enter your number"))
c=count(n)
res=arms(n,c)
if(res==n):
    print("Great Work Armstrongggg")
else:
    print(res,"Not Armstring Bruvvv")
