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
        try:#this is here to prevent mistakes in the input 
            USER = input(">")
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
                        OTRO = raw_input(">") #you ask him if he wants to add another
                        OTRO = OTRO.lower() #you convert his answer
                        if OTRO == "y":
                            ADD = True #returns the condition, in a loop
                        elif OTRO == "n":
                            ADD = False #kills the question
                            USERCON = True #kills the user answer
                            MENU = True #return to menu
                        else:
                            print "Only enter Y or N" #if the user is trying to add something else
                    except ValueError: #if the user enters letters instead of numbers
                        print "Enter only numbers"
            else:
                pass #if the user is trying to add other numbers other than 123

        except SyntaxError: #this is applying to everything - take a closer look at this
            print "Enter only numbers 1, 2 or 3"
        except NameError:
            print "Enter only numbers 1, 2 or 3"
