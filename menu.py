import os
from keyboard_ import key_pressed



def show_menu(menu_toggled): #showing menu options
    menu_options = ["writing", "save", "import", "clear field", "Exit"] #resetting menu eptions
    menu_options[menu_toggled] = menu_options[menu_toggled].upper() # showing what is selected
    menu_visual = (" "*8).join(menu_options)    #formatting
    print(menu_visual)
    print("\n\t", menu_descriptions[menu_toggled])



menu_options = ["writing", "save", "import", "clear field", "Exit"]
menu_descriptions = ["Continue editing the text", "save text", "import text from file", "clear textfield",  "Exit program"]

def toggle_menu(): #main menu interface
    menu_toggled = 0 #menu option selected

    while True: #menu tui while not quitting
        os.system("clear")
        
        show_menu(menu_toggled)  #show mune inteface

        action = key_pressed()  #executing menu action
        if action[0] == "move_cursor":  #moving option selector
            horizontal_movement = action[1][1]
            if  0 <= menu_toggled + horizontal_movement <= len(menu_options) - 1:  #and not beyond limits
                menu_toggled += horizontal_movement

        elif action[0] == "enter": #selecting an option
            selected = menu_options[menu_toggled]

            match selected:
                case "save":
                    return "save"
                case "import":
                    return "import"
                case "clear field":
                    return "clear"
                case "Exit":
                    return "exit"
                case "writing":
                    return "writing"
