import doctest, random, board_utils, dicts_utils, scrabble_utils

def get_words(file_name):
    """ (str) -> list

    Returns a list of containing the lines within the file file_name
    """
    f = open(file_name)
    words = f.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()
    
    f.close()
    
    return words

def get_scrabble_bag():
    """ () -> dict

    Returns a dictionary representing a standard scrabble bag
    
    """
    return {'a' : 9,
            'b' : 2,
            'c' : 2,
            'd' : 4,
            'e' : 12,
            'f' : 2,
            'g' : 3,
            'h' : 2,
            'i' : 9,
            'j' : 1,
            'k' : 1,
            'l' : 4,
            'm' : 2,
            'n' : 6,
            'o' : 8,
            'p' : 2,
            'q' : 1,
            'r' : 6,
            's' : 4,
            't' : 6,
            'u' : 4,
            'v' : 2,
            'w' : 2,
            'x' : 1,
            'y' : 2,
            'z' : 1}

def get_scrabble_letter_values():
    """ () -> dict

    Returns a dictionary with the standard scrabble letter values
    """
    return { 'a': 1,
             'b': 3,
             'c': 3,
             'd': 2,
             'e': 1,
             'f': 4,
             'g': 2,
             'h': 4,
             'i': 1,
             'j': 8,
             'k': 5,
             'l': 1,
             'm': 3,
             'n': 1,
             'o': 1,
             'p': 3,
             'q': 10,
             'r': 1,
             's': 1,
             't': 1,
             'u': 1,
             'v': 4,
             'w': 4,
             'x': 8,
             'y': 4,
             'z': 10}

def display_scores(names, scores):
    """ (list, list) -> NoneType

    Displays the names of the players and their score.
    
    >>> n = ['Giulia', 'Chris', 'Rahul', 'Yichen']
    >>> s = [63, 167, 190, 185]
    >>> display_scores(n, s)
    
    FINAL SCORES
    Giulia:  63
    Chris:  167
    Rahul:  190
    Yichen:  185
    """
    print("\nFINAL SCORES")
    for i in range(len(names)):
        print(names[i] + ": ", scores[i])


def play(bag, letter_values, valid_words):
    # create board
    board = board_utils.create_board(15, 15)
    n = int(input("How many players are you? "))
    
    # retrieve names of the players
    names = []
    for i in range(n):
        name = input("What's the name of player " + str(i+1) + "? ")
        names.append(name)
        
    # create one rack per player
    players = []
    for i in range(n):
        r = {}
        scrabble_utils.refill_rack(r, bag, 7)
        players.append(r)
        
    # create scores for each player
    scores = []
    for i in range(n):
        scores.append(0)
        
    last_turn = False
    
    while not last_turn:
        if bag == {}:
            last_turn = True
        # players take turns
        for i in range(n):
            # display info to the player
            board_utils.display_board(board)
            print(names[i] + ", it's your turn!")
            print("These are the letters on your rack:", end = ' ')
            scrabble_utils.display_rack(players[i])
            print()
            
            # ask for the info needed to make a move
            letters = input("Please enter the letters you'd like to use: ")
            while letters == '':
                letters = input("You should enter at least one letter: ")
            
            row_pos = int(input("Please indicate the row number of the starting position: "))
            col_pos = int(input("Please indicate the column number of the starting position: "))
            direction = input("Please indicate the direction ('right' or 'down'): ")
            
            # perfom the player move and update their score
            try:
                words = scrabble_utils.make_a_move(board, players[i], letters.lower(), row_pos, col_pos, direction)
                scores[i] += scrabble_utils.compute_score(words, letter_values, valid_words)
                scrabble_utils.refill_rack(players[i], bag, 7)
            except IndexError:
                print("\nNot enough space on the board. You lost your turn!\n")
            except ValueError:
                print("\nYou do not have those letters on your rack. You lost your turn!\n")
            
            # display current score
            print('\n' + names[i] + "'s score is:", scores[i], '\n')
        

    
    board_utils.display_board(board)
    # display final scores
    display_scores(names, scores)

            

def scrabble(file_name):
    words = get_words(file_name)
    valid_words = dicts_utils.create_scrabble_dict(words)
    bag = get_scrabble_bag()
    letter_values = get_scrabble_letter_values()
    play(bag, letter_values, valid_words)
    
if __name__ == "__main__":
    #doctest.testmod()
    random.seed(3)
    scrabble("words.txt")