from itertools import product, permutations
from functools import reduce
from math import factorial
from tqdm import tqdm
from pudb import set_trace

TEST_MAPPED = {'t': 4, 'h': 3, 'e': 6, 'y': 9, 'a': 8, 'r': 2, 'v': 5, 's': 1, 'm': 0}

def adjust_word_length(words_list):
    max_word_len = max([len(word) for word in words_list])
    return [(max_word_len - len(word))*'0' + word for word in words_list]

def mapped_letter_choices(words_list, unique_mappings_only):
    letters = set(''.join(words_list))
    letters.discard('0')

    if unique_mappings_only:
        if len(letters) <= 10:
            combo_iter = permutations(range(10), len(letters))
            total_iters = factorial(10)
        else:
            raise IndexError('Too many letters in word equation to keep unique. Try unique_mappings_only=False')
    else:
        combo_iter = product(range(10), repeat=len(letters))
        total_iters = 10**len(letters)

    with tqdm(total=total_iters) as pbar:
        for nums in tqdm(combo_iter):
            pbar.update(1)
            mapped = dict(zip(letters, nums))
            yield mapped
            # yield prod

def is_valid_mapping_slow(mapped, words_list):
    if not all_letters_used(mapped, words_list):
        return False

    equation = [int(''.join([replace_text(letter, mapped) for letter in word])) for word in words_list]
    addends, result = equation[:-1], equation[-1]
    return True if sum(addends) == result else False

def is_valid_mapping(mapped, words_list):

    # Return False if mapping would cause word to start with a 0
    if not all_letters_used(mapped, words_list):
        return False

    carry = 0
    for i in range(1, len(words_list[0])+1):
        column_letters = [word[-i] for word in words_list]
        addends_letters, result_letter = column_letters[:-1], column_letters[-1]
        mapped_addends = [mapped[letter] if letter != '0' else 0 for letter in addends_letters]
        valid, carry = valid_combo_with_remainder(mapped_addends, mapped[result_letter], carry)
        if valid is False:
            return False
    else:
        return True

def all_letters_used(mapped, words_list):
    for word in words_list:
        for letter in word:
            if letter == '0':
                continue
            else:
                if mapped[letter] == 0:
                    return False
                else:
                    break
    else:
        return True

def valid_combo_with_remainder(addends, result, prev_carry=0):
    column_result = sum(addends) + prev_carry
    if column_result % 10 == result:
        return True, column_result // 10
    else:
        return False, prev_carry

def replace_text(text_to_replace, dic):
    dic = {k: str(v) for k, v in dic.items()}
    return reduce(lambda a, kv: a.replace(*kv), dic.items(), text_to_replace) if text_to_replace else None

def print_results(valid_count, mapped, words_list):
    print('Mapping #{0}:'.format(valid_count))
    print(mapped)
    equation = [int(''.join([replace_text(letter, mapped) for letter in word])) for word in words_list]
    for num in equation:
        print(num)
    print(sum(equation[:-1]), equation[-1])
    print('\n')

def main(raw_words_list, unique_mappings_only=True):
    valid_mapping_count = 0
    words_list = adjust_word_length(raw_words_list)

    for mapped in mapped_letter_choices(words_list, unique_mappings_only):
        if is_valid_mapping(mapped, words_list):
            valid_mapping_count += 1
            print_results(valid_mapping_count, mapped, words_list)
            yield valid_mapping_count, mapped

if __name__ == '__main__':
    # set_trace()
    raw_words_list = ['they', 'are', 'very', 'smart']
    print(is_valid_mapping(TEST_MAPPED, adjust_word_length(raw_words_list)))
    # raw_words_list = ['hello', 'my', 'name', 'is', 'chris']

    valid_mappings = []
    for valid_mapping_count, mapped in main(raw_words_list, unique_mappings_only=False):
        valid_mappings.append(mapped)

    print(valid_mappings)
    print('Final Number of Matching Results: {0}'.format(valid_mapping_count))
