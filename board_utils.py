def create_board(rows, columns):
    """
    (int) -> list
    Returns a two dimensional list with only space characters or raises a ValueError if inputs are not positive
    
    >>>create_board(5, 3)
    [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    >>>create_board(2, 4)
    [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    
    >>>create_board(-5, 2)
    Traceback (most recent call):
    ValueError: Inputs must be positive
    """
    #check rows and columns are positive integers
    if rows>0 and columns>0:
        #create board
        board = [[' ']*columns]*rows
        return board
    else:
        raise ValueError("Inputs must be positive")
    
def display_board(board_list):
    """
    (list) -> NoneType
    Displays board
    
    >>>b = [['A', 'R', 'T', ' '], [' ', ' ', 'O', ' '], [' ', ' ', 'E', ' ']]
    >>>display_board(b)
         0    1    2    3 
       +---------------+
    0  | A | R | T |   | 
       +---------------+
    1  |   |   | O |   | 
       +---------------+
    2  |   |   | E |   | 
       +---------------+
    >>>b = create_board(2, 3)
    >>>display_board(b)
         0   1   2 
       +-----------+
    0  |   |   |   | 
       +-----------+
    1  |   |   |   | 
       +-----------+
    >>>b = create_board(3, 3)
    >>>display_board(b)
         0    1    2 
       +-----------+
    0  |   |   |   | 
       +-----------+
    1  |   |   |   | 
       +-----------+
    2  |   |   |   | 
       +-----------+
    """
    #using a to iterate through len(board_list) for first line
    a = 0
    print("    ", end = " ")
    while a in range(len(board_list[0])):
        print("   ", a, end = ' ')
        a+=1
    #for new lines using i
    for i in range(len(board_list)):
        print("\n", " +", ("---"), end = '')
        print(("----")*(len(board_list[i])-2), end = '')
        print(("---+"))
        print(i, " |", end = " ")
        a = 0
        for a in range(len(board_list[i])):
            print(" ", board_list[i][a], " |", end = " ")
            a += 1
        i += 1
    #ending line:
    print("\n", " +", ("---"), end = '')
    print(("----")*(len(board_list[i-1])-2), end = '')
    print(("---+ \n"))
    
def get_vertical_axis(board_list, column_selected):
    """
    (list, int) -> list
    Returns list of strings containing elements from columns on board selected
    
    >>>b = [['C', 'A', ' '], ['A', 'R', 'T'], ['T', 'T', ' ']]
    
    >>>get_vertical_axis(b, 1)
    ['A', 'R', 'T']
    
    >>>get_vertical_axis(b, 0)
    ['C', 'A', 'T']
    
    >>>get_vertical_axis(2, 2)
    [' ', 'T', ' ']
    """
    #creating empty list
    vertical_list = []
    #iterate through len(board_list)
    for i in range(len(board_list)):
        #add to vertical list
        vertical_list += board_list[i][column_selected]
        i += 1
    return vertical_list

def find_word(new_list, i):
    """
    (list, int) -> str
    Returns word formed by letters including new_list[i]
    
    >>>find_word(['a', 't', ' ', 'a', 'r', 't'], 4)
    'art'
    
    >>>find_word(['g', 'r', 'e', 'e', 'n', '', 'g', 'o'], 6)
    'greengo'
    
    >>>find_word(['k', 'i', 't', 'e', ' ', 't'], 4)
    ' '
    """
    #check word isn't empty
    if new_list[i] == " ":
        return " "
    else:
        #using a as empty word to add to
        a = ""
        t = i
        #iterate through len(new_list)
        while t in range(len(new_list)):
            #check for empty characters
            if new_list[t] == " ":
                #b is the starting point of the word in new_list
                b = t+1
                break
            elif new_list[t] != " " and t == 0:
                #at t == 0 it should not continue going back
                b = 0
                break
            elif new_list[t] != " " and t != 0:
                t -= 1
                continue
            
        #iterate through len(new_list) to create word
        while b in range(len(new_list)):
            #check for empty characters
            if new_list[b] != " ":
                #add letters to word
                a += new_list[b]
                b += 1
            else:
                return a
        return a
    
def available_space(rc, i):
    """
    (list, int) -> int
    Returns number of empty squares starting from i
    
    >>>r = [' ', 'g', 't', ' ', ' ']
    >>>available_space(r, 1)
    2
    
    >>>r = [' ', ' ', ' ', 't', ' ']
    >>>available_space(r, 3)
    1
    
    >>>r = [' ', ' ', ' ', 'y']
    >>>available_space(r, 3)
    0
    """
    #define space to add to as we find empty characters
    space = 0
    #iterate through len(rc)
    while i in range(len(rc)):
        #check for empty characters
        if rc[i] == " ":
            space += 1
            i += 1
        else:
            i += 1
    return space

def fit_on_board(list_of_strings, letters, i):
    """
    (list, str, int) -> bool
    Returns True or False depending on if the word can fit on the board
    
    >>>a = ['a', ' ', ' ', 'b', ' ', ' ']
    >>>fit_on_board(a, 'cat', 1)
    True
    
    >>>a = ['a', 'r', 't', ' ', ' ', ' ', ' ', 'o', ' ']
    >>>fit_on_board(a, 'apple', 3)
    True
    
    >>>a = [' ', 't', ' ', 'g', 'r', ' ', ' ']
    >>>fit_on_board(a, 'dog', 1)
    False
    """
    #check for space at starting point
    if list_of_strings[i] == " ":
        #check if letters will fit
        if len(letters) <= available_space(list_of_strings, i):
            return True
        else:
            return False
    else:
        return False