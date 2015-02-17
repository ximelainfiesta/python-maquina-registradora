# Register Machine Code
"""Starts the Register Machine Program"""
SHOP = {} #shows the current articles in the store
CLIENT = [] #List to save CLIENT's products
PRICES = [] #List to keep the PRICES
TOTAL = []

"""FUNCTIONS"""
def total():
    """Function that adds the tax to the total"""
    return price() + tax()

def tax():
    """Function that creates the tax"""
    return price() * 0.12

def price():
    """Function that rests the discount from the total"""
    return sum(PRICES) - cards()

def cards():
    """Function that adds the discount to the bill"""
    des = 0
    if "gold" in TOTAL: #if gold is in the list
        des = sum(PRICES) * 0.05 #add to the variable the discount
        return des #it returns the discount when called
    elif "silver" in TOTAL:
        des = sum(PRICES) * 0.02
        return des
    else: #if there is no card, will send 0 discount
        return des


def bill(): #below the %.2f converts in two digits float
    """Function to print the Bill's PRICES"""
    print "Your subtotal is: %.2f" %(sum(PRICES))#this function sums the list
    print "Your discount is: %.2f" %(cards()) #calls the function with 2 decimals
    print "Your Tax is: %.2f" %(tax()) #calls the tax with 2 decimals
    print "Your total is: %.2f" %(total()) #Calls the total with 2 decimals
    print "Thank you for shopping with us"

def bill_printing():#it prints the bill in order with prices
    """Function to sort the items and print them like a bill"""
    CLIENT.sort()
    for i in CLIENT:
        print CLIENT.count(i), i, "%.2f" %(SHOP[i]) #converts it in two decimals and it counts the items
        PRICES.append(SHOP[i]) #it adds the value to another list

def bill_calc():#it will allow the cashier enter the items to sell
    """Function that asks the cashier for the item"""
    calculus = True
    while calculus == True:
        try:
            cashier = raw_input("Enter the item: ")
            cashier = cashier.lower()
            if cashier == "done": #sends the program to another function
                bill_printing() #calls function
                calculus = False #kills the function
            elif cashier == "gold":
                TOTAL.append("gold") #it sends gold to an empty list
            elif cashier == "silver":
                TOTAL.append("silver")
            elif cashier == "silver" and "gold":
                TOTAL.append("gold")
            elif cashier not in SHOP: #it verifies than the item is in the store
                print "Item not in store"
            else:
                CLIENT.append(cashier) #adds the item to the new list
        except ValueError:
            print "Enter only items"

MENU = True #Condition than allows the menu
while MENU == True:
    USERCON = False #condition that will be killed if user wants to exit
    ADD = True #condition that will be killed if user decides to exit adding items
    while USERCON == False:
        try:#this is here to prevent mistakes in the input
            USER = input("""
---------Register Machine's Main Menu---------
-           What do you want to do?          -
-                 1. Add an item             -
-                 2. Sell Articles           -
-                 3. Exit                    -
----------------------------------------------
""")
            if USER == 3: #because it is input, its 3 not "3"
                USERCON = True #kills the user input
                MENU = False #kills the menu
                print "Thank you for using us" #prints a byebye message
            #because my condition is up, i start next option, adding items
            elif USER == 1:
                while ADD == True:
                    try:#it helps me corroborate the raw input
                        IVALUE = float(raw_input("Item Value: "))#converts raw_input into a float
                        SHOP[raw_input("Item: ")] = IVALUE#this is the ecuation for adding in a dicc
                        print SHOP #helps me see my adds - it is temp
                        print "Do you want to insert another article? Y/N"#after entered an item
                        ADDAGAIN = False #another block only with the question above
                        while ADDAGAIN == False:
                            OTRO = raw_input(">") #you ask him if he wants to add another
                            OTRO = OTRO.lower() #you convert his answer
                            if OTRO == "y":
                                ADDAGAIN = True #kills the add another item block
                            elif OTRO == "n":
                                ADDAGAIN = True #kills the add another item block
                                ADD = False #kills the question
                                USERCON = True #kills the user answer
                                MENU = True #return to menu
                            else:
                                print "Only enter Y or N" #if the user add something else
                    except ValueError: #if the user enters letters instead of numbers
                        print "Enter only numbers"
            elif USER == 2:
                bill_calc() #calls the function that prints my bill
                bill() #call the function that will print my total and discount
                MENU = True

            else:
                print "Enter only numbers 1, 2 or 3" #if the user add other numbers other than 123

        except SyntaxError: #this is applying to everything - take a closer look at this
            print "Enter only numbers 1, 2 or 3"
        except NameError:
            print "Enter only numbers 1, 2 or 3"
