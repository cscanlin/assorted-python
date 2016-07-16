from itertools import product
from functools import reduce
# from pprint import pprint
# import pdb

def column_consistent(column):
    for i, tup1 in enumerate(column):
        for tup2 in column[-i:]:
            if tup1[0] == tup2[0] and tup1[1] != tup2[1]:
                return False
    else:
        return True

def blanks_0(column):
    for tup in column:
        if tup[0] == ' ' and tup[1] != 0:
            return False
    else:
        return True

def yield_letter_options(letters_column, prev_columns=[], prev_carry=0):
    letter_options = product(range(10), repeat=len(letters_column))
    for prod in letter_options:
        column = list(zip(letters_column, prod))
        addends, result = column[:-1], column[-1]
        addend_sum = sum(addend_tup[1] for addend_tup in addends) + prev_carry
        next_carry = addend_sum // 10
        next_columns = column + prev_columns
        if addend_sum % 10 == result[1] and column_consistent(column) and blanks_0(column):
            yield next_columns, next_carry
        else:
            yield None, None

def recursive_word_search(words_list, matching_dicts=[], i=1, prev_columns=[], prev_carry=0):
    letters_column = [word[-i] for word in words_list]
    for next_columns, next_carry in yield_letter_options(letters_column, prev_columns, prev_carry):
        print(next_columns)
        if next_columns is None:
            continue
        elif i == 5:
            matching_dicts.append({tup[0]: str(tup[1]) for tup in next_columns})
        else:
            i += 1
            return recursive_word_search(words_list, matching_dicts, i, next_columns, next_carry)
    return matching_dicts

def replace_text(text_to_replace, dic):
    return reduce(lambda a, kv: a.replace(*kv), dic.items(), text_to_replace) if text_to_replace else None

def print_results(num_sub_dict, words_list):
    try:
        print(num_sub_dict)
        equation = [int(''.join([replace_text(letter, num_sub_dict) for letter in word])) for word in words_list]
        print(equation)
        for num in equation:
            print(num)

        print(sum(equation[:-1]), equation[-1])
    except:
        pass

if __name__ == '__main__':
    # pdb.set_trace()
    words_list = [' they', '  are', ' very', 'smart']
    matching_dicts = recursive_word_search(words_list)
    for num_sub_dict in matching_dicts:
        print_results(num_sub_dict, words_list)

    # words_list = [' they', '  are', ' very', 'smart']
    #
    # matching_dicts = recursive_word_search(words_list)
