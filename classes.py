#create a class f15 with functions lights ,fans and ac when light function is clled it prints out
#color of the light which is taken as parameter to the function when fan function is called it displays the speed,which is taken as the parameter to the function
#ac displays the room temp and out side temp

class f15:
    def lights(self,color):
        print("the color is",color)
    def fan(self,speed):
        print("speed is",speed)
    def ac(self,temp1,temp2):
        self.ot=temp2
        self.it=temp1
        print("room temp and outside temp is", temp2,temp1)
    def display(self,ot,it):
        self.diff=self.ot-self.it
        print(self.diff)
    def _init_ p(self):
        print("999")
teja=f15()
teja.lights("white")
teja.fan(5)
teja.ac(12,34)
teja.display() 
