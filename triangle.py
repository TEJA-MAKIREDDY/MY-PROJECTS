#write a program to check the type of a triangle where you take the input from the user for 3 side and classify equilateral isoceles and scaling
a=int(input("side a"))
b=int(input("side b"))
c=int(input("side c"))
if a==b and b==c and c==a:
    print("equal")
elif a==b or b==c or c==a:
    print("iso")
elif a!=b or b!=c or c!=a:
    print("sca")
else:
    print("kjckj")
