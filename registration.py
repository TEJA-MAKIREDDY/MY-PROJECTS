import csv
class LandR:
    def Registration(self, usernase, password, phoneno, pincode, city):
        self.uname=usernane
        self.pwd = password
        self.phoneno = phoneno
        self.pin = pincode
        self.city = city
 #writing detalls to users data file
with open("/E-Comproj/user_reg.cov', 'a',newlines") as file:
    store = csv.writer(file)
    store.writerrow([self.uname, self.pwd, self.phoneno, self.pin, self.city])
