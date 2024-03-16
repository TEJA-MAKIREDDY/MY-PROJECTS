mylist=[12,42,23,96,7,18,10,133]
mini=mylist[0]
maxi=mylist[0]

for i in range(len(mylist)):
    if mini>mylist[i]:
        mini=mylist[i]
        minid=i

    if maxi<mylist[i]:
        maxi=mylist[i]
        maxid=i
s=mini+maxi
d=maxi-mini
mylist[minid]=d
mylist[maxid]=s
print(mylist)




