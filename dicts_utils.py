def count_occurrences(word):
    """
    (str) -> dict
    Returns a dictionary mapping the number of a certain letter in the word to the letter
    
    >>>d = count_occurrences('apple')
    >>>d == {'a' : 1, 'p' : 2, 'l' : 1, 'e' : 1}
    True
    
    >>>d = count_occurrences('tree')
    >>>d == {'t' : 1, 'r' : 1, 'e' : 2}
    True
    
    >>>d = count_occurrences('yellow')
    >>>d == {'y' : 1, 'e' : 1, 'l' : 2, 'o' : 1, 'w' : 1}
    True
    """
    #create empty dictionary
    occurrences = {}
    #iterate through elements in word
    for ele in word:
        #check if element already in dictionary
        if ele in occurrences:
            occurrences[ele] += 1
        else:
            occurrences[ele] = 1
    return occurrences

def flatten_dict(new_occurrences):
    """
    (dict) -> list
    Returns a list containing all the keys in the dictionary however many times the number they are given as a value
    
    >>>d = {'a' : 2, 'g' : 3, 'b' : 1, 'c' : 2}
    >>>list_d = flatten_dict(d)
    >>>list_d.sort()
    >>>list_d
    ['a', 'a', 'g', 'g', 'g', 'b', 'c', 'c']
    
    >>>d = {'giraffe' : 2, 'snake' : 4, 'tiger' : 1}
    >>>zoo_animals = flatten_dict(d)
    >>>zoo_animals.sort()
    >>>zoo_animals
    ['giraffe', 'giraffe', 'snake', 'snake', 'snake', 'snake', 'tiger']
    
    >>>d = {'d' : 2, 'h' : 1, 'z' : 3}
    >>>letters = flatten_dict(d)
    >>>letters.sort()
    >>>letters
    ['d', 'd', 'h', 'z', 'z', 'z']
    """
    #create empty list
    list_of_items = []
    #iterate through keys of dictionary
    for k in new_occurrences.keys():
        #add to list
        added_letters = [k]*new_occurrences[k]
        list_of_items += (added_letters)
    return list_of_items

def get_word_score(word, letter_scores):
    """
    (str, dict) -> int
    Returns score of word according to dictionary of scores of letters
    
    >>>d = {'a' : 3, 't' : 6, 'z' : 8}
    >>>get_word_score('cat', d)
    9
    
    >>>d = {'f' : 6, 't' : 2, 's' : 4}
    >>>get_word_score('fish', d)
    10
    
    >>>d = {'g' : 5, 'u' : 1, 'l' : 3, 'm' : 1}
    >>>get_word_score('gummy', d)
    8
    """
    #create empty score
    score = 0
    #iterate through len(word)
    for i in range(len(word)):
        #check if elements have scores and add to them if they do
        if word[i] in letter_scores:
            score += letter_scores[word[i]]
        else:
            score += 0
    return score

def is_subset(first_dict, second_dict):
    """
    (dict, dict) -> bool
    Returns True if first dictionary is a subset of the second dictionary
    
    >>>a = {'k' : 3, 'l' : 2}
    >>>b = {'h' : 4, 'k' : 6, 'l' : 4, 's' : 1}
    
    >>>is_subset(a, b)
    True
    >>>is_subset(b, a)
    False
    
    >>>a = {'d' : 5, 'j' : 1}
    >>>b = {'c' : 2, 'd' : 4, 'e' : 1, 'j' : 3}
    
    >>>is_subset(a, b)
    False
    >>>is_subset(b, a)
    False
    """
    #iterate through elements of first_dict
    for ele in first_dict:
        #check if elements are part of second_dict and have a lower or equal value
        if ele in second_dict:
            if first_dict[ele] <= second_dict[ele]:
                continue
            else:
                return False
        else:
            return False
    return True

def subtract_dicts(d1, d2):
    """
    (dict, dict) -> bool
    Returns True if d2 is subset of d1
    
    >>>a = {'h' : 2, 'j' : 3}
    >>>b = {'a' : 2, 'h' : 4, 'j' : 3, 't' : 5}
    >>>c = {'a' : 1, 't' : 2}
    
    >>>subtract_dicts(b, a)
    True
    >>>b == {'a' : 2, 'h' : 2, 't': 5}
    True
    
    >>>subtract_dicts(a, b)
    False
    
    >>>subtract_dicts(b, c)
    True
    >>>b == {'a' : 1, 'h' : 2, 't' : 3}
    True
    """
    #check if subset
    if is_subset(d2, d1):
        #iterate through elements in d2 and remove them from d1
        for ele in d2:
            d1[ele] = d1[ele] - d2[ele]
            if d1[ele] == 0:
                del d1[ele]
        return True
    else:
        return False
    
def create_scrabble_dict(list_of_words):
    """
    (list) -> dict
    Returns dictionary containing all words mapped to their first letter and further mapped to their length
    
    >>>w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>>d = create_scrabble_dict(w)
    >>>d == {2 : {'a' : ['aa'], 'q' : ['qi'], 'z' : ['za']}, 3 : {'c' : ['cat', 'can', 'cow'], \
    'd' : ['dog', 'dad']}, 5 : {'h' : ['hippo'], 'u' : ['umami', 'uncle']}}
    True
    
    >>>w = ['apple', 'orange', 'pear', 'kiwi', 'strawberry']
    >>>d = create_scrabble_dict(w)
    >>>d == {4 : {'p' : ['pear'], 'k' : ['kiwi']}, 5 : {'a' : ['apple']}, 6 : {'o' : ['orange']}, \
    10 : {'s' : ['strawberry']}}
    True
    
    >>>w = ['tree', 'bush', 'leaf', 'park', 'mountain', 'river']
    >>>d = create_scrabble_dict(w)
    >>>d == {4: {'p': ['park'], 't': ['tree'], 'b': ['bush'], 'l': ['leaf']}, 8: {'m': ['mountain']}, \
    5: {'r': ['river']}}
    True
    """
    #create empty dictionary
    dict_of_words = {}
    #iterate through elements in list_of_words
    for ele in list_of_words:
        #create another empty dictionary
        new_dict = {}
        #check if len(ele) already in dict_of_words
        if len(ele) in dict_of_words:
            #check if first letter of ele in dict_of_words
            if ele[0] in dict_of_words[len(ele)]:
                dict_of_words[len(ele)][ele[0]].append(ele)
            else:
                dict_of_words[len(ele)][ele[0]] = [ele]
        else:
            new_dict[ele[0]] = [ele]
            dict_of_words[len(ele)] = new_dict
    return dict_of_words
    
def is_valid_word(word, dict_of_words):
    """
    (str, dict) -> bool
    Return True if word is in dictionary
    
    >>>w = ['tree', 'bush', 'leaf', 'park', 'mountain', 'river']
    >>>d = create_scrabble_dict(w)
    
    >>>is_valid_word('leaf', d)
    True
    
    >>>is_valid_word('ball', d)
    False
    
    >>>is_valid_word('mountain', d)
    True
    """
    #check if first letter in dict_of_words
    if word[0] in dict_of_words[len(word)]:
        #check if word in dict_of_words
        if word in dict_of_words[len(word)][word[0]]:
            return True
        else:
            return False
    else:
        return False
    
print(random(10.00, 15.00))