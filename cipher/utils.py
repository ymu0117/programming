"""
Define helper functions 
"""
import math 
import re 


def convert_2d_list(my_list, key, word):
    """Convert 1d list to 2d list, 
    each row has key elements and pad with word 
    to make rectangular shape. 
    """
    remainder = len(my_list) % key
    my_list.extend([word] * remainder)
    num_rows = len(my_list) // key
    two_d_list = [[my_list[j*key+i] for i in range(key)] for j in range(num_rows)] 
    return two_d_list


def transpose_2d_list(two_d_list):
    """Transpose 2d list. 
    """
    row = len(two_d_list)
    col = len(two_d_list[0])
    if row <= 1 or col <= 1:
        raise ValueError('List need to be two d to make transpose.')
    return [[two_d_list[x][y] for x in range(row)] for y in range(col)]


def convert_1d_list(two_d_list):
    """Convert two dimensional list to one dimension and remove padding words. 
    """
    row = len(two_d_list)
    col = len(two_d_list[0]) 
    return [two_d_list[x][y] for x in range(row) for y in range(col) if not isinstance(two_d_list[x][y], str)]


def convert_transpose_2d(my_list, key, word):
    """Convert transposition cipher to 2 d list. 
    """
    remainder = key - len(my_list) % key
    col = math.ceil(len(my_list)/key)
    two_d_list = [[None for x in range(col)] for y in range(key)]
    for k in range(key):
        if k < (key - remainder):
            two_d_list[k] = my_list[k*col:(k+1)*col]
        else:
            start = (key-remainder)*col+(k-key+remainder)*(col-1)
            two_d_list[k] = my_list[start:start+(col-1)]
            two_d_list[k].append(word)
    return two_d_list


def calc_percent(words, dictionary):
    count = 0
    for x in words:
        if x.lower() in dictionary:
            count += 1
    return count / len(words)


def word2pattern(word, case_type):
    """Convert word to pattern. 
    For example, for word 'abandon', the pattern will 
    be '0.1.0.2.3.4.2'
    Parameters
    ----------
    word: str
    case_type: options = {'insensitive', 'sensitive'}
    """
    if case_type == 'insensitive':
        word = word.lower()
    elif case_type == 'sensitive':
        pass
    else:
        raise ValueError('Case type is not defined.')

    pattern = []
    int_map = {}
    i = 0
    for w in word:
        if w not in int_map:
            int_map[w] = str(i) 
            i += 1
        pattern.append(int_map[w])
    return '.'.join(pattern)


def create_pattern_map(dictionary, case_type):
    """Map words in the defined dictionary to patterns. 
    """
    pattern_map = {}
    for k in dictionary.keys():
        pattern = word2pattern(k, case_type)
        if pattern not in pattern_map:
            pattern_map[pattern] = []
        pattern_map[pattern].append(k) 
    return pattern_map


def simple_extract_words(txt):
    """Extracting words using re, assuming white space and symbols 
    are preserved when being entryped  
    """
    return re.findall(r'\w+', txt)


def compile_extract_words(txt):
    """Using re.compile to extract words. 
    """
    pattern = re.compile('[^A-Za-z\s]')
    return pattern.sub('', txt).split()       


def word2table(word, pattern_map, case_type, alphabet):
    """Map cipherword to a dictionary, where each letter of the 
    cipherword will have a list of values that correspond to the words 
    in the dictionary that have same pattern. 
    """
    if case_type == 'insensitive':
        word = word.lower()
    elif case_type == 'sensitive':
        pass
    else:
        raise ValueError('Case type is not defined.')

    table = {letter: [] for letter in alphabet}
    pattern = word2pattern(word, case_type)
    for i, w in enumerate(word):
        for candidate in pattern_map[pattern]:
            if candidate[i] not in table[w]: 
                table[w].append(candidate[i])
    return table


def update_intersected_table(intersected_table, letter_map_table): 
    for k in letter_map_table.keys():
         if k in intersected_table:
            intersected_table[k] = intersected_table[k].intersection(letter_map_table[k])
         else:
            intersected_table[k] = letter_map_table[k]
    return intersected_table


def get_intersected_table(alphabet, tables):
    intersected_table = {letter: [] for letter in alphabet}

    for letter in intersected_table.keys():
        for table in tables:
            if table[letter] and intersected_table[letter]:
                intersected_table[letter] = list(set(intersected_table[letter]).intersection(set(table[letter])))
            elif table[letter] and not intersected_table[letter]:
                intersected_table[letter].extend(table[letter])
            else:
                continue
    return intersected_table 


def get_solved_mapping(table):
    solved_map = {}
    unsolved_map = {}
    for k, v in table.items():
        if len(v) == 1:
            solved_map[k] = v
        else:
            unsolved_map[k] = v
    return solved_map, unsolved_map 


def convert_txt(txt, key_map, case_type='insensitive'):
    converted_txt = []
    for t in txt:
        try: 
            if case_type == 'insensitive' and t.isupper():
                letter = list(key_map[t.lower()])[0]
                converted_txt.append(letter.upper())
            else:
                letter = list(key_map[t])[0]
                converted_txt.append(letter) 
        except KeyError:
            converted_txt.append(t)
            continue            
    return ''.join(converted_txt)

