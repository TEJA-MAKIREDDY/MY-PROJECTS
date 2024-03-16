#take a number inpuut from the user check if the sum of factors of that number is greater than the original number or not
sof=0
a=int(input("enter the number"))
for i in range(1,a):
    if(a%i==0):
        sof=sof+i
if (sof>0):
    print("abundent")
else:
    print("not")
