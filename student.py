import csv
f = open("student.csv","a",newline="")
a = csv.writer(f)
a.writerow["studentID","rollno","name","mobilenumber"]
studentid = int(input("enter studentid:"))
rollno = int(input("enter your roll number:"))
name = input("enter your name")
mobilenumber=int(input("enter mobile number:"))
a.writerow(["studentID","rollno","name","mobilenumber"])
print("student record has saved")