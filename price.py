#write a prgm to check the on road price of a bike and then the conditions, if the price is greater than 72k(thousand) them income tax is 10% of 
#the road tax will be 10% and insurance willbe 15% of actual price, 
#if the price is greater than 1.5 lak thousandand less than 2lak rupees the tax will be 25% and insurance will be 20%,
#if the price is above 2lak rupees then tax will be 35% and insurance will be of 28%,
#otherwise minimum bike with us starts from 72000
price = int(input("enter the price"))
if price >= 72000 and price<150000:
    tax = (10/100)*price
    insurance = (15/100)*price
    print(price+tax+insurance)
elif price >=150000 and price < 200000:
    tax = (25/100)*price
    insurance = (20/100)*price
    print(price+tax+insurance)
elif price > 200000:
    tax = (35/100)*price
    insurance = (28/100)*price
    print(price+tax+insurance)
else:
    print("minimum bike with us starts from 72000")
