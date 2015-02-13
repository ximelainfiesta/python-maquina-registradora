# Register Machine Code
"""Starts the Register Machine Program"""
SHOP = {} #shows the current articles in the store
CLIENT = [] #List to save CLIENT's products

def bill():#it will make the bill
    CLIENT.sort()
    for i in CLIENT:
        print i

def bill_calc():#it will allow the cashier enter the items to sell
    while True:
        try:
            X = raw_input("Enter the item: ")
            X = X.lower()
            if X == "done":
                bill()
                break
            else:
                CLIENT.append(X)
        except:
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
                bill_calc()


            else:
                print "Enter only numbers 1, 2 or 3" #if the user add other numbers other than 123

        except SyntaxError: #this is applying to everything - take a closer look at this
            print "Enter only numbers 1, 2 or 3"
        except NameError:
            print "Enter only numbers 1, 2 or 3"
