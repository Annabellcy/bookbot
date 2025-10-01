def get_string_num(contents):
    str_lst = contents.split()
    return len(str_lst)

def get_character_num(contents):
    contents = contents.lower()
    char_dic = {}
    for char in contents:
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] += 1
    return char_dic