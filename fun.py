#write a function to caliculate sum of first and last digit of a number the num should be taken as arugument
def value(a):
    b=a%10
    while(a>10):
        a=a//10
    print(a+b)
a=int(input("enter"))
value(a)
