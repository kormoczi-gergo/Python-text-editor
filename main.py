import os
from keyboard_ import key_pressed

               #line  #row
cursor_index = [0,     0]



def str_to_charlist(text_split): #breaks lines into chars
    char_list = []
    str_buffer = []
    for line in text_split:
        for char in line: 
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
    for i in range(0,2):
        cursor_index[i] += action[i]
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
    char_list = str_to_charlist(text_split)
    return char_list





text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

text_split = text.split('\n') #split up the text for lines

char_list = str_to_charlist(text_split) #split up the lines to characters for easy indexing


while True:
    os.system("clear")

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
