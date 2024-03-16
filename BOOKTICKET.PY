#create a class ticket which will be the abstract class inside that create a function bookticket which will be the abstact method and has nothing in it
#create a class make my trip which will use the book ticket function from ticket class to take the details such as name phone number emailid journy date
#and displays a message thakingyou for booking from make my trip.create a class irctc which uses the bookticket class and takes the same details as makemy
#trip but in the end it will give option to the user to select wheather it is one way or round trip if the user option is round trip it again asks the user to
#enter thereturn date aswell and then prints a message thankyou for choosing irctc else print the message for choosing irctc.create a class indigo which takes
#all the details as irctc and just asks which mode of transport you want to go in train,bus or car and displays a message  thankyou for choosing indigo

from abc import ABC, abstractmethod
class ticket(ABC):
    
    @abstractmethod
    def bookticket(self):
        pass

class make_my_trip(ticket):
    def bookticket(self):
        name=input("enter your name: ")
        phone=input("enter your phone number: ")
        email=input("enter your email: ")
        journey_date=input( "enter journey date:")
        transport_mode = input("Choose mode of transport (Train/Bus/Car): ")
        if transport_mode=="Train" or transport_mode=="bus" or transport_mode=="car":
            print(f"You'll be traveling by {transport_mode}.")
        else:
            print("choose only train car or bus")
            transport_mode = input("Choose mode of transport (Train/Bus/Car): ")
        print(f"Thank you for choosing make_my_trip! You'll be traveling by {transport_mode}.")

class irctc(ticket):
    def bookticket(self):
        name=input("enter your name: ")
        phone=input("enter your phone number: ")
        email=input("enter your email: ")
        journey_date=input( "enter journey date:")
        transport_mode = input("Choose mode of transport (Train/Bus/Car): ")
        if transport_mode=="Train" or transport_mode=="bus" or transport_mode=="car":
            print(f"You'll be traveling by {transport_mode}.")
        else:
            print("choose only train car or bus")
            transport_mode = input("Choose mode of transport (Train/Bus/Car): ")
        print(f"You'll be traveling by {transport_mode}.")
        trip_type = input("choose trip(oneway or round trip):")
        if trip_type == "round trip":
            return_date = input("Enter the return date: ")
            print("Thank you for choosing IRCTC! Your round trip is booked.")
        else:
            print("Thank you for choosing IRCTC! Your one-way trip is booked.")


class Indigo(ticket):
    def bookticket(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email ID: ")
        journey_date = input("Enter the journey date: ")
        transport_mode = input("Choose mode of transport (Train/Bus/Car): ")
        if transport_mode=="Train" or transport_mode=="bus" or transport_mode=="car":
            print(f"You'll be traveling by {transport_mode}.")
        else:
            print("choose only train car or bus")
            transport_mode = input("Choose mode of transport (Train/Bus/Car): ")
        print(f"Thank you for choosing Indigo! You'll be traveling by {transport_mode}.")



MakeMyTrip = make_my_trip()
MakeMyTrip.bookticket()


IRCTC =irctc()
IRCTC.bookticket()


indigo = Indigo()
indigo.bookticket()


    
