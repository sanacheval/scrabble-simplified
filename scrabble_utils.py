# r = player's rack
# c = string containing one letter
# r[c] = how many tiles with letter c are on the rack
import dicts_utils, board_utils, random
def display_rack(r):
    """
    (dict) -> NoneType
    Displays letters in rack
    
    >>>r = {'f' : 3, 's' : 1, 't' : 2}
    >>>display_rack(r)
    FFFSTT
    
    >>>r = {'p' : 2, 'i' : 4, 't' : 1}
    >>>display_rack(r)
    PPIIIIT
    
    >>>r = {'k' : 3, 'u' : 6}
    >>>display_rack(r)
    KKKUUUUUU
    """
    #create flatten_dict of rack
    a = dicts_utils.flatten_dict(r)
    final_letters = ""
    #iterate through length of flatten_dict of rack
    for i in range(len(a)):
        final_letters += a[i].upper()
        i += 1
    print(final_letters)
    
def has_letters(r, word):
    """
    (dict, str) -> bool
    Returns True if letters of word are in r and subtracts them from r
    
    >>>r = {'r' : 3, 'e' : 4, 't' : 2, 'g' : 2}
    >>>has_letters(r, 'tree')
    True
    >>>r == {'r' : 2, 'e' : 2, 't' : 1, 'g' : 2}
    True
    
    >>>r = {'f' : 3, 'e' : 3, 'r' : 2, 'g' : 2, 'n': 1}
    >>>has_letters(r, 'green')
    True
    >>> r == {'f' : 3, 'e' : 1, 'r' : 1, 'g' : 1}
    True
    
    >>>has_letters(r, 'free')
    False
    """
    #count occurences of letters in word
    a = dicts_utils.count_occurrences(word)
    #remove occurences from rack
    return dicts_utils.subtract_dicts(r, a)

# pool is pool of letters to pick from
# n is positive integer
def refill_rack(r, pool, n):
    """
    (dict, dict, int) -> NoneType
    
    >>>random.seed(123)
    >>>r1 = {'c' : 2, 'j' : 1}
    >>>r2 = {'d' : 3, 'q' : 1, 's' : 4}
    >>>b = {'a' : 4, 'e' : 2, 'h' : 2, 'g' : 2, 'k' : 1, 'p': 2, 's' : 1, 'i' : 1, 'x': 3}
    
    >>>refill_rack(r1, b, 6)
    >>>r1 == {'c': 2, 'j': 1, 'a': 2, 'g': 1}
    True
    >>>b == {'a': 2, 'e': 2, 'h': 2, 'g': 1, 'k': 1, 'p': 2, 's': 1, 'i': 1, 'x': 3}
    True
    
    >>>refill_rack(r2, b, 10)
    >>>r2 == {'d': 3, 'q': 1, 's': 4, 'x': 1, 'g': 1}
    True
    >>>b == {'a': 2, 'e': 2, 'h': 2, 'k': 1, 'p': 2, 's': 1, 'i': 1, 'x': 2}
    True
    
    >>>refill_rack(r2, b, 8)
    >>>r2 == {'d': 3, 'q': 1, 's': 4, 'x': 1, 'g': 1}
    True
    >>>b == {'a': 2, 'e': 2, 'h': 2, 'k': 1, 'p': 2, 's': 1, 'i': 1, 'x': 2}
    True
    """
    for i in range(n):
        pool_in_list = dicts_utils.flatten_dict(pool)
        #check pool isn't empty
        if len(pool_in_list) != 0:
            #check r isn't at n letters
            r_in_list = dicts_utils.flatten_dict(r)
            if len(r_in_list) < n:
                #make random choice
                pool_letter = random.choice(pool_in_list)
                #add choice to r and remove from pool
                if pool_letter in r:
                    r[pool_letter] += 1
                    pool[pool_letter] -= 1
                    if pool[pool_letter] == 0:
                        del pool[pool_letter]
                    i += 1
                else:
                    r[pool_letter] = 1
                    pool[pool_letter] -= 1
                    if pool[pool_letter] == 0:
                        del pool[pool_letter]
                    i += 1
            else:
                break
        else:
            break

def compute_score(list_of_words, points_of_letters, valid_words):
    """
    (list, dict, dict) -> int
    Returns total score of words used
    
    >>>v = {'a' : 5, 'g' : 2, 'l' : 3, 'r' : 2}
    >>>w = ['apple', 'orange', 'pear', 'kiwi', 'strawberry']
    >>>d = dicts_utils.create_scrabble_dict(w)
    
    >>>compute_score(['apple', 'pear'], v, d)
    15
    
    >>>compute_score(['strawberry', 'grape'], v, d)
    0
    
    >>>compute_score(['kiwi'], v, d)
    0
    """
    #create empty total score
    total_score = 0
    #iterate through len(list_of_words)
    for i in range(len(list_of_words)):
        #check if valid word and add to scores
        if dicts_utils.is_valid_word(list_of_words[i], valid_words):
            total_score += dicts_utils.get_word_score(list_of_words[i], points_of_letters)
        else:
            return 0
    return total_score

def place_tiles(board, letters_to_add, row, column, direction_of_words):
    """
    (list, str, int, int, str) -> str
    Returns words created by letters_to_add or an empty list if the direction_of_words is neither 'right' or 'down'
    
    >>>b = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    
    >>>place_tiles(b, 'apple', 1, 0, 'right')
    ['apple']
    
    >>>place_tiles(b, 'tme', 0, 0, 'down')
    ['tame']
    
    >>>place_tiles(b, 'care', 4, 3, 'up')
    []
    """
    #check if direction_of_words correct
    if direction_of_words == 'right':
        t = 0
        #create empty list
        new_words_list = []
        #iterate through len(letters_to_add)
        for i in range(len(letters_to_add)):
            #check space is empty
            while board[row][column+t] != ' ':
                if column+t <= len(board[row]):
                    #add to check for empty spaces
                    t += 1
                else:
                    break
            #add letter to empty space
            board[row][column+t] = letters_to_add[i]
            #get vertical axis
            vertical_axis_list = board_utils.get_vertical_axis(board, column+t)
            #check for words in vertical axis and add them to list
            if len(board_utils.find_word(vertical_axis_list, row)) > 1:
                new_words_list.append(board_utils.find_word(vertical_axis_list, row))
                i += 1
            else:
                i += 1
        #find word created in row
        new_word = board_utils.find_word(board[row], column)
        new_words_list.append(new_word)
        return new_words_list
        
    elif direction_of_words == 'down':
        t = 0
        #create empty list
        new_words_list = []
        #iterate through len(letters_to_add)
        for i in range(len(letters_to_add)):
            #check space is empty
            while board[row+t][column] != ' ':
                if row+t <= len(board):
                    #add to check for empty spaces
                    t += 1
                else:
                    break
            #add letter to empty space
            board[row+t][column] = letters_to_add[i]
            #check for words in rows and add them to list
            if len(board_utils.find_word(board[row+t], column)) > 1:
                new_words_list.append(board_utils.find_word(board[row+t], column))
                i += 1
            else:
                i += 1
        #find vertical word and add to list
        vertical_axis_word = board_utils.get_vertical_axis(board, column)
        new_words_list.append(board_utils.find_word(vertical_axis_word, row))
        return new_words_list
        
    else:
        empty_list = []
        return empty_list
    
def make_a_move(board, r, letters_to_add, row, column, direction_of_words):
    """
    (list, dict, str, int, int, str) -> list
    Returns list of words made by letters_to_add or error if letters do not fit or player does not have letters
    or an empty list if the direction_of_words is neither 'right' or 'down'
    
    >>>b = [[' ', ' ', ' ', ' '], [' ', 'd', 'o', 'g'], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>>r = {'a' : 3, 'b' : 1, 'g' : 4, 'r' : 3, 's' : 5, 't' : 6, 'n' : 2, 'c' : 1}
    
    >>>make_a_move(b, r, 'trn', 0, 2, 'down')
    ['torn']
    >>>r == {'a' : 3, 'b' : 1, 'g' : 4, 'r' : 2, 's' : 5, 't' : 5, 'n' : 1, 'c' : 1}
    True
    
    >>>words = make_a_move(b, r, 'ca', 0, 0, 'right')
    >>>words.sort()
    >>>words
    ['ad', 'cat']
    >>>r == {'a' : 2, 'b' : 1, 'g' : 4, 'r' : 2, 's' : 5, 't' : 5, 'n' : 1}
    True
    
    >>>make_a_move(b, r, 'at', 0, 0, 'right')
    Traceback (most recent call last):
    IndexError: these letters do not fit on the board
    """
    #check direction_of_words is correct
    if direction_of_words == 'right':
        #check word fits on board
        if board_utils.fit_on_board(board[row], letters_to_add, column):
            #check person has letters
            if has_letters(r, letters_to_add):
                # place tiles
                return place_tiles(board, letters_to_add, row, column, direction_of_words)
            else:
                raise ValueError("player does not have these letters in their rack")
        else:
            raise IndexError("these letters do not fit on the board")
        
    elif direction_of_words == 'down':
        #get vertical list and check word fits on board
        vertical_list = board_utils.get_vertical_axis(board, column)
        if board_utils.fit_on_board(vertical_list, letters_to_add, row):
            #check person has letters
            if has_letters(r, letters_to_add):
                # place tiles
                return place_tiles(board, letters_to_add, row, column, direction_of_words)
            else:
                raise ValueError("player does not have these letters in their rack")
        else:
            raise IndexError("these letters do not fit on the board")
        
    else:
        empty_list = []
        return empty_list