# Register Machine Code
"""Starts the Register Machine Program"""
SHOP = {} #shows the current articles in the store
CLIENT = [] #List to save CLIENT's products
TOTAL = [] #List to keep the total
CARDS = ["gold", "silver"]

"""FUNCTIONS"""

def bill(): #below the %.2f converts in two digits float
    """Function to print the Bill's total"""
    print "Your Total is:  ", "%.2f" %(sum(TOTAL)) #this function sums the list
    print """ How would you like to pay?
              1. Gold Card              
              2. Silver Card   
              3. None                   
              """ #make this interactive
#In here must put the other functions to pay because it returns to my menu

def bill_printing():#it prints the bill in order with prices
    """Function to sort the items and print them like a bill"""
    CLIENT.sort()
    for i in CLIENT:
        print i, "%.2f" %(SHOP[i]) #converts it in two decimals
        TOTAL.append(SHOP[i]) #it adds the value to another list

def bill_calc():#it will allow the cashier enter the items to sell
    """Function that asks the cashier for the item"""
    calculus = True
    while calculus == True:
        try:
            cashier = raw_input("Enter the item: ")
            cashier = cashier.lower()
            if cashier == "done": #sends the program to another function
                bill_printing()
                calculus = False
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
                bill() #call the function that will print my total


            else:
                print "Enter only numbers 1, 2 or 3" #if the user add other numbers other than 123

        except SyntaxError: #this is applying to everything - take a closer look at this
            print "Enter only numbers 1, 2 or 3"
        except NameError:
            print "Enter only numbers 1, 2 or 3"
