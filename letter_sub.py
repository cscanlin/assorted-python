#
#
# len(words)
#
# for num in range(0, 9):
#     if words[0][4] + words[1][4] + words[2][4] = result[4] % 10:
#         print word,num
#
#
# for i, word in enumerate(words):
#     word_len = 4
#     if words[i]
#     for i, letter in enumerate(word[::-1]):

from string import ascii_lowercase
from collections import OrderedDict

def check_nums(global_alphabet, addend_words, result_word):

    # print(list(zip(addend_words))[-1:])
    column_letters = [next(reversed(word.keys())) for word in addend_words]
    print(column_letters)
    sum_total = sum(global_alphabet[letter][-1] for letter in column_letters)
    sum_digit = sum_total % 10
    result_to_check = list(result_word.values())[-1][-1]
    print(result_to_check)
    if sum_digit != result_to_check:
        print(column_letters)
        column_letters = remove_nums(global_alphabet)
        print(column_letters)
        return 'done', '& done'
        return check_nums(global_alphabet, addend_words, result_word)
    else:
        sum_carry = sum_total // 10
        return sum_carry, sum_digit


def remove_nums(column):
    for i, digit_list in enumerate(column):
        if len(digit_list) > 1:
            column[i] = digit_list[:-1]
            return column
    return column

def main():
    global_alphabet = {letter: list(range(0, 10)) for letter in ascii_lowercase}
    addend_words = ['they', ' are', 'very']
    result_word = 'smart'
    addend_word_options = [OrderedDict((letter, list(range(0, 10))) for letter in word) for word in addend_words]
    result_word_options = OrderedDict((letter, list(range(0, 10))) for letter in result_word)
    # print(word_options)

    # for column in zip(*word_options):
    # sum_carry, sum_digit = check_nums(list(column))
    sum_carry, sum_digit = check_nums(global_alphabet, addend_word_options, result_word_options)
    print(sum_carry, sum_digit)

    # letters = ['y', 'e', 'y']
    # result = 't'

if __name__ == '__main__':
    main()
    # a = list(range(0, 7))
    # b = list(range(0, 3))
    # print(a[6])
    # print(b[6])

# for letter in letters:
#     for i in range(0, 9):
