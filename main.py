import os
from keyboard_ import key_pressed
from menu import toggle_menu
from file_handling import _import, save






               #line  #row
cursor_index = [0,     0]


def split_to_charlist(text_split): #breaks lines into chars
    char_list = []
    str_buffer = []
    for line in text_split:
        for char in line: 
            if char != '\n':
                str_buffer.append(char)
        char_list.append(str_buffer)
        str_buffer = []
    return char_list

def output_text(char_list): #turn the charlist back into a string
    lines = []
    for line in char_list:
        lines.append("".join(line))
    for line in lines:
        print(line)
    
def insert_cursor(char_list, index): #insert cursor into the charlist based on cursor coordinates
    char_list[index[0]].insert(index[1], '|')
    return char_list


def move_cursor_coord(cursor_index, action): #move cursor coordinates
    if cursor_index[0] < 1 and action[0]  < 0: pass                                                                          #first culumn cant go up
    elif cursor_index[0] == 0 and cursor_index[1] < 1 and action[1] == -1:  pass                                             #first char, cant go left
    elif cursor_index[0] >= len(char_list) - 1 and action[0] >= 1:   pass                                                    #last row cant go down
    elif cursor_index[0] >= len(char_list) - 1 and cursor_index[1] >= len(char_list[cursor_index[0]]) and action[1] > 0:pass #last char, cant go right

    elif action[1] < 0 and cursor_index[1] == 0:    #last line with going left
        cursor_index[0] -= 1
        cursor_index[1] = len(char_list[cursor_index[0]])
    elif action[1] > 0 and cursor_index[1] >= len(char_list[cursor_index[0]]): # next line with going right
        cursor_index[0] += 1
        cursor_index[1] = 0

    else:
        for i in range(0,2):
            cursor_index[i] += action[i]

    if cursor_index[1] > len(char_list[cursor_index[0]]):#return cursor to the last char if it is too big
        cursor_index[1] = len(char_list[cursor_index[0]])
    return cursor_index


def remove_cursor(char_list, index): #remove cursor so in the next frame the cursor can be in a new coord
    char_list[index[0]].pop(index[1]) 
    return char_list

def insert_char(char_list, index, char): #inserts a pressed character into the char_list
    char_list[index[0]].insert(index[1], char)
    return char_list

def delete(char_list, index): #pops the char that is on the left of the cursor
    char_list[index[0]].pop(index[1] - 1)
    return char_list

def new_line(char_list, row, column):
    char_list[row].insert(column, '\\n') #insert a \n into the str at the cursor coordinates
    text = "" #join the char_list into a string with \n meaning the end of a line
    buffer = ""
    for line in char_list:
        for char in line:
            buffer += char
        buffer += '\\n'
        text += buffer
        buffer = ""
    text_split = text.split('\\n') #resplit the characters into a charlist
    char_list = split_to_charlist(text_split)
    return char_list


def text_to_split(text): # text to [lines: [chars: '0', 'd'], ['d', 'h']]
    text_split = text.split('\n') #split up the text for lines
    return split_to_charlist(text_split) #split up the lines to characters for easy indexing





text = ""
char_list = text_to_split(text)

while True:
    os.system("clear")

    print("press Ctrl + t to enter the menu")   #print menu field
    print( "_" * len("press Ctrl + t to enter the menu") , '\n')

    #printing text with cursor
    char_list = insert_cursor(char_list, cursor_index)  #insert cursor into the charlist
    output_text(char_list) #write the text onto the terminal
    char_list = remove_cursor(char_list, cursor_index)  #remove the cursor
    action = key_pressed() #get what key is pressed

    #executing actions based on what key was pressed
    if action[0] == "move_cursor":
        cursor_index = move_cursor_coord(cursor_index, action[1]) #moves cursor coord

    if action[0] == "write":
        char_list = insert_char(char_list, cursor_index, action[1]) #inserts character into the coordinate of the cursor
        cursor_index = move_cursor_coord(cursor_index, [0, 1]) # move the cursor coord one to the right
    
    if action[0] == "delete":
        char_list = delete(char_list, cursor_index) #deletes one char from the char_list
        cursor_index = move_cursor_coord(cursor_index, [0, -1]) #move the cursor one to the left

    if action[0] == "enter":
        char_list = new_line(char_list, row=cursor_index[0], column=cursor_index[1])
        cursor_index = move_cursor_coord(cursor_index, [1,0]) #move the cursor to the next line
        cursor_index[1] = 0  #put the cursor at the start of the line

    if action[0] == "toggle_menu":
        menu_command = toggle_menu() #executing menu command

        if menu_command == "save":
            os.system("clear")
            path = input("path to save: ")
            save(path, char_list)

        elif menu_command == "import":
            os.system("clear")
            path = input("path of file: ")
            text = _import(path)
            char_list = split_to_charlist(text)

        elif menu_command == "clear":
            char_list = [['']]
            cursor_index = [0, 0]


        elif menu_command == "exit":
            break
