class father:
    def bike(self):
        print("harley Devidson")
    def laptop(self):
        print("laptop with 2GB RAM and 500")
class anji(father):
    def laptop(self):#method overriding
        print("As per any programming software")
        print ("laptop with 8GB RAM and 1TB")
obj = anji()
obj.bike()
obj.laptop()
