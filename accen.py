
#calicucale sum the the numbers divisible by six and not divisible by six in the range of first 30 numbers
s1=0
s2=0
for i in range(1,31):
    if(i%6==0):
        s1=s1+i
    else:
        s2=s2+i
print(s1)
print(s2)
        
