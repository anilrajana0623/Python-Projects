#Cashir Flow
def enterproducts():
    buyingdata = {}
    enterdetails = True

    while enterdetails:
        details = input('Press A to add product and Q to Quit: ')

        if details == 'A':
            product = input('Enter Product: ')
            quality = int(input('Enter Quality:'))
            buyingdata.update({product:quality})
        elif details == 'Q':
            enterdetails = False
        else:
            print('Please select a correct option')
    return buyingdata

#enterproducts()
def getPrice(product,quantity):
    pricedata = {'Biscuit':3,'Chicken':5,'Egg':1,'Fish':3,'Coke':2, 'Bread':2,'Apple':3,'Onion':3}

    subtotal = pricedata[product]*quantity
    print(product + ':$'+str(pricedata[product])+'x'+str(quantity)+'='+str(subtotal))
    return subtotal

def getdiscount(billamount,membership):
    discount = 0
    if billamount >= 25:
        if membership == 'Gold':
            billamount = billamount * 0.80
            discount = 20
        elif membership == 'Silver':
            billamount = billamount * 0.90
            discount = 10
        elif membership == 'Bronze':
            billamount = billamount * 0.95
            discount = 5
        print(str(discount) + '% Off for'+membership+''+'membership on total amount: $'+ str(billamount))
    else:
        print('No discount on amount lessthan $25')
    return billamount

def makebill(buyingdata, membership):
    billamount = 0
    for key,value in buyingdata.items():
        billamount += getPrice(key,value)
    billamount = getdiscount(billamount,membership)
    print('The discounted amount is $'+ str(billamount))

buyingData = enterproducts()
membership = input('Enter customer membership: ')
makebill(buyingData,membership)