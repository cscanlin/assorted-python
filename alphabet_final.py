import string
from collections import OrderedDict

file_name = 'alphabet.txt'

def by_first_letter(file_name):
    """
    1st Approach - Find the first letter of each word and add to list if unique.
    Does not work because there are some letters that have no words beginning with them.
    """
    alphabet = []

    with open(file_name) as f:
        for word in f:
            first_letter = word[0]
            if first_letter not in alphabet:
                alphabet.append(first_letter)

    print_output(alphabet)
    return alphabet

def letter_by_letter(file_name):
    """
    2nd Approach - Iterate through each word letter by letter with the assumption that each subsequent letter
    is neccessarily after it in the alphabet. This is clearly a bad assumption upon closer examination.
    """
    alphabet = []

    with open('alphabet.txt') as f:
        for num,word in enumerate(f):

            word = word.strip()
            for i,active_letter in enumerate(word[:-1]):
                if active_letter in alphabet:
                    active_letter_index = alphabet.index(active_letter)
                    next_letter = word[i+1]
                    if next_letter in alphabet:
                        next_letter_index = alphabet.index(next_letter)
                        if active_letter_index > next_letter_index and next_letter not in word[:i]:
                            print word
                            print alphabet
                            print active_letter,next_letter
                            print active_letter_index,next_letter_index
                            alphabet.remove(active_letter)
                            alphabet.insert(next_letter_index,active_letter)
                            print alphabet
                            print '\n'
                    else:
                        pass

                else:
                    alphabet.append(active_letter)
    print_output(alphabet)
    return alphabet



def final(file_name):
    """
    Final Approach - For each word in the list, compare it to the next word. If the words
    share the same beginning and then differ by a letter, we know that the different letter
    in the current word must come before the different letter in the next word.
    """
    alphabet = []
    word_list = extract_word_list(file_name)

    def generate_active_and_next_word(word_list):
        """Generate curent word and next word where current word is shorter than next"""
        for entry_num,active_word in enumerate(word_list[:-1]):
            next_word = word_list[entry_num + 1]
            if len(active_word) <= len(next_word):
                yield active_word, next_word
            else:
                pass

    def get_alphabet_index(letter,alphabet):
        """
        Get the index location in alphabet for a letter. If the letter does not
        exist, add it to the end of aplahbet and return None for letter_index.
        """
        if letter in alphabet:
            letter_index = alphabet.index(letter)
        else:
            letter_index = None
            alphabet.append(letter)
        return letter_index, alphabet

    def main(alphabet,word_list):
        """
        The main function which takes the list of words and any known data about the alphabet.
        This function is inefficient and must be run twice for this list of words. Less than Ideal.
        """
        for active_word, next_word in generate_active_and_next_word(word_list):
            for i,_ in enumerate(active_word):
                # Continue to next letters while the word fragments match
                if active_word[:i] == next_word[:i]:
                    continue

                # Break the loop and move onwhen there is a difference and
                # store the different letters as active_letter and next_letter
                else:
                    active_letter = active_word[i-1]
                    next_letter = next_word[i-1]
                    break

            # Find active and next letters' index in list, or add it to the end of alphabet
            active_letter_index, alphabet = get_alphabet_index(active_letter,alphabet)
            next_letter_index, alphabet = get_alphabet_index(next_letter,alphabet)

            # If current_letter is after next_letter in alphabet, move it in front.
            # Passes if next_letter_index is None
            if next_letter_index is not None:
                if active_letter_index > next_letter_index:
                    alphabet.remove(active_letter)
                    alphabet.insert(next_letter_index,active_letter)
                else:
                    pass
            else:
                pass

        return alphabet

    # main() function has to be run twice because it is not very efficient...
    # TODO find a way to improve efficiency - maybe don't need entire first half of each word to match
    return main(main(alphabet,word_list),word_list)


"""
NOTES:

1. Would this all be better using classes? Maybe one for the text file, one for the alphabet.
The alphabet is passed around a lot, and I suspect improvements could be made to encapsulation

2. Also, what is really the best way to determine when a letter is truly after another
in the alphabet? I don't think the entire first half of the word is neccessary to validate
that the subsequent letters are in the correct order. Letter by letter doesn't work by itself
though. Maybe some sort of hybrid between the two?
"""


# Bonus Functions

def extract_word_list(file_name):
    """Extract word list from file to strip extra whitespace and for easier parsing"""
    with open(file_name) as f:
        return [word.strip() for word in f]

def print_output(alphabet):
    """Print output in desired format"""
    for i,letter in enumerate(alphabet):
        print "Letter {0} => '{1}'".format(i+1, letter)

def build_conversion_dict(alphabet):
    """Build OrderedDict for conversion to unscrambeled alphabet"""
    return OrderedDict((scrambled_letter,alpha_letter) for scrambled_letter,alpha_letter in zip(alphabet,string.ascii_lowercase))

def unscramble_word(word,conversion_dict):
    """Unscramble word using conversion_dict"""
    return ''.join([conversion_dict[letter] for letter in word.strip()])

if __name__ == '__main__':
    alphabet = final(file_name)
    conversion_dict = build_conversion_dict(alphabet)
    for word in extract_word_list(file_name):
        converted_word = unscramble_word(word,conversion_dict)
        print converted_word
    print_output(alphabet)
