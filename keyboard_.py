import sys, tty, termios

def key_pressed(): #gets what char the user typed or what key he pressed
    action = ["", ""] #action that get returned and stored   ["do", "what"]
    presses =[]
    arrow_key_pressed = False

    fd = sys.stdin.fileno()  #standart terminal IO mode
    old_settings = termios.tcgetattr(fd)    #stores standart IO mode

    try:
        tty.setraw(sys.stdin.fileno())  #setting the terminal to raw mode
    except:
        print("terminal couldnt be set to raw mode")

    for i  in range(0,3): # range( 0,3 ) cuz a arrowkey code is 3 char long 

        char = sys.stdin.read(1) #read 1 char
        presses.append(char)   #append char to the pressed (no need to press \n) ,  can store caracters like arrow key   ['\x1b', '[', 'B']

        if "\x1b" in presses[0]:  # arrow key pressed returns    
            arrow_key_pressed = True #cursor moving mode
        else:
            break    #typing mode and only need to get one char

    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  #restore original terminal setting


    if arrow_key_pressed == True: #if arrow key were pressed
        action[0] = "move_cursor"
        match presses[2]: 
            case 'A':    #['\x1b', '[', 'A']
                action[1] = [-1, 0]
            case 'B':    
                action[1] = [1, 0]
            case 'D':   
                action[1] = [0, -1]
            case 'C':    
                action[1] = [0, 1]
    
    else:
        if presses[0] == '\x7f':#delete
            action = ["delete", ""]

        elif presses[0] == '\r': #\n
            action = ["enter", ""]

        elif presses[0] == '\x14':  #toggle menu
            action = ["toggle_menu", ""]

        else:
            action = ["write", char]
    return action
