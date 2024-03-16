#take input from the user and check if the number is divisible by sum of digits or not
s=0
a=int(input("enter the number"))
while(a>0):
    digit=a%10
    s=s+digit
    a=a//10
if(a%s==0):
    print("divisible")
else:
    print("not divisible")
