#write a function which takes 2 arguments a and b typecast the value of 2nd argument into integer then multiply  both the arguments and print the last digit of the result


def name(a,b):
    b=int(b)
    c=a*b
    print(c%10)

name(12,13)#positional arguments
name(b=34,a=35)#keyword arguments


def city(name="ramanagadu",city="guntur"):#default arguments
    print(name, "from", city)
city()
city("babu","hyderabad")



#unknown arguments
def func(**name):
    print("my name is" ,name["lname"])

func(fname = "prashant", lname = "jha",)


