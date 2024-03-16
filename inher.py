class faculty:#parent class
    def _init_(self, f_name,dpartment, f_id):
        self.f_name = f_name
        self.dpartment = dpartment
        self.f_id = f_id
    def print_info(self):
        print("faculty information=",self.f_name,self.f_id)
obj=faculty("asish","computer_science",1001)
obj.print_info()



class cse(faculty):
    pass
obj=cse("jyoti mam","computer_science",1002)
obj.print_info()
