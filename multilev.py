#create a class with name placements which has a function info info displays "we have 623 sells and still counting"
#create another class with name department with function display which will display the names of the department present in the college.
#create a class pragati with a funcion welcome which displays the message welcome to pragati engg college. pragati class should also display
#the details about departments and placements



class placements:
    def info(self):
        print("we have 623 placements and still counting")




class department(placements):
    def display(self):
        print("departments present in the college: \n1.information technology \n2.cse \n3.data science \n4.mech \n5.civil")




class pragati(department):
    def welcome(self):
        print("welcome to pragati engg college")


obj1=pragati()
obj1.welcome()
obj1.info()
obj1.display()


