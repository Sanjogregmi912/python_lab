#price of house is $1M. if buyer has good credit,they need to put down 10% otherwise they need to put down 20%.
#print the down payment
price_of_house=1000000
down_payment=input("choose if you have good credit or not?\n")
if(down_payment=="good credit"):
    print(f"the amount after good credit={int(10/100*price_of_house)}")
else:
    print(f"the amount when you havenot any good credit is {int(20//100*price_of_house)}")
