'''
Mini Project:
=============

Creating Super Market Invoice 
--------------------------------------------
  Rajana's Super Market
Name:
Address:

sno       Item    Quantity    Price
1         sugar      2          40
2         salt       3          60


   Total Price:100
--------------------------------------------

Item list with price - one method
'''
''' Creating Dictionary containers for inventory storage'''
products ={"Apple":20,"Biscuit":10,"Cornflour":50,"Egg":7,"Coke":20,"Onion":40, "Other":35} #Inventory data with Prices
buyingdata = {} #To Store User buying data as product and quantity
buyingdatewithprice ={} #To Store Product with final price

# To input the product details from the user
def enterproducts():
    enterdetails = True
    while enterdetails:
        details = input('Press A to add product and Q to Quit: ')
        if details == 'A':
            product = input(""""Apple":20,
            "Biscuit":10,
            "Cornflour":50,
            "Egg":7,
            "Coke":20,
            "Onion":40, 
            "Other":35
            Enter Product From Above: """)
            quality = int(input('Enter Quality:'))
            buyingdata.update({product: quality})
        elif details == 'Q':
            enterdetails = False
        else:
            print('Please select a correct option')

# To update the product the final price calculation
def Updating_buyingdatewithprice():
    for product,quantity in buyingdata.items():
        price = products[product]*quantity
        buyingdatewithprice.update({product:price})

#To print the invoice
def InvoicePrinting():
    print("="*20, "Welcome To Rajana's Super Market", "="*20)
    print(" "*20,"In-voice copy")
    print(" "*20,"-------------")
    print("Name : {}".format(Name))
    print("Address : {}".format(Address))
    print("S.no", " "*5, "Item"," "*5,"Quantity", " "*5, "Price")
    i=1
    total = 0
    for key,value in buyingdatewithprice.items():
        print(i, " "*7, key," "*10,products[key], " "*10, value)
        total = total + value
        i+=1
    print(" "*10,"Total Price =",total)
    print("="*20, "End of Invoice", "="*20)

#Input the customer details and products and printing the invoice 
#Starting point of the project
print("="*20, "Welcome To Rajana's Super Market", "="*20)
Name = input("Enter your Name: ")
Address = input("Enter Your Address:")
enterproducts()
Updating_buyingdatewithprice()
InvoicePrinting()


 








