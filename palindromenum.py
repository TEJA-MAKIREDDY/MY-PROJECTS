#palindrome number
rev=0
n=1441
n1=n
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(rev==n1):
    print("yes")
else:
    print("not")






