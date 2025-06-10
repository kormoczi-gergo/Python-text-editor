def _import(path):
    text = ""
    with open(path, 'r', encoding="utf-8") as f:
        text = f.readlines()
    return text

def save(path, char_list):
    lines = ["".join(line)+'\n' for line in char_list]  #join the lines of the charlist and put a \n at the end
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
