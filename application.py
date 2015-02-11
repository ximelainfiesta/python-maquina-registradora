# Register Machine Code
"""Starts the Register Machine Program"""
SHOP = {} #Empty diccionarie

MENU = True #Condition than allows the menu
while MENU == True:
    MAIN_MENU = """ 
---------Register Machine's Main Menu---------
-           What do you want to do?          -
-                 1. Add an item             -
-                 2. Sell Articles           -
-                 3. Exit                    -
----------------------------------------------
""" #My menu's design
    print MAIN_MENU #prints my beautiful menu

    USERCON = False #condition that will be killed if user wants to exit
    ADD = True #condition that will be killed if user decides to exit adding items
    while USERCON == False:
        try: #this is here to prevent mistakes in the input 
            USER = input(">")
            if USER == 3:
                USERCON = True
                MENU = False
                print "Thank you for using us"
            
            elif USER == 1:
                while ADD == True:
                    SHOP[raw_input("Item: ")] = float(input("Item Value: "))
                    print SHOP
                    print "Do you want to insert another article? Y/N"
                    OTRO = raw_input(">")
                    OTRO = OTRO.lower()
                    if OTRO == "y":
                        ADD = True
                    elif OTRO == "n":
                        ADD = False
                        USERCON = True
                        MENU = True
                    else:
                        print "Only enter Y or N"
            else:
                print "Enter only numbers 1, 2 or 3"

        except SyntaxError:
            print "Enter only numbers 1, 2 or 3"
        except NameError:
            print "Enter only numbers 1, 2 or 3"
