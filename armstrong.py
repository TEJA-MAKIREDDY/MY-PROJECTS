#ARMSTRONG NUMBER
n=153
n=0
s=0
a=n
a1=n
while (n>0):
    digit=n%10
    n=n//10
    c=c+1
n=a
while (n>0):
    digit=n%10
    s=s+(digit)**c
    n=n//10
if s==a:
    print("num are Armstrong")
else:
    print("num are not Armstrong")
