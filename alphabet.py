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



def final_v2(file_name):
    """
    Final Approach v2 - For each word in the list, compare it to the next word. If the words
    share the same beginning and then differ by a letter we know this is a shared "root"
    (minimum root length is adjustable).

    Once we have the root, generate a list of all words with a similar root. Then we know
    that all of the letters that come after this root are in the correct order.
    """
    alphabet = []
    word_list = extract_word_list(file_name)

    def get_root_word(active_word, adjacent_word, min_length=3):
        """Generates root words by comparing adjacent words. Can set a minimum length"""
        for i,_ in enumerate(active_word):
            # Continue to next letters while the word fragments match
            root_length = i + min_length
            if active_word[:root_length+1] == adjacent_word[:root_length+1]:
                continue
            else:
                break
        return active_word[:root_length]

    def find_similar_words(active_word, entry_num, root):
        """Generate words with a similar root"""
        root_length = len(root)
        for potential_match in word_list[entry_num:]:
            if active_word[:root_length] == potential_match[:root_length]:
                yield potential_match
            else:
                break

    def generate_similar_words(word_list):
        """Generate lists of words with all similar roots, as well as the actual root"""
        for entry_num,active_word in enumerate(word_list[:-1]):
            adjacent_word = word_list[entry_num+1]
            root = get_root_word(active_word, adjacent_word)
            similar_words = list(find_similar_words(active_word, entry_num, root))
            if len(similar_words) > 2:
                yield root, similar_words

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

    def rearrange_alphabet(alphabet, ordered_letters):
        for i,active_letter in enumerate(ordered_letters[:-1]):
            next_letter = ordered_letters[i+1]

            # Find active and next letters' index in list, or add it to the end of alphabet
            active_letter_index, alphabet = get_alphabet_index(active_letter, alphabet)
            next_letter_index, alphabet = get_alphabet_index(next_letter, alphabet)

            # If current_letter is after next_letter in alphabet, move it in front.
            # Passes if next_letter_index is None (pass statements are optional)
            if next_letter_index is not None:
                if active_letter_index > next_letter_index:
                    alphabet.remove(active_letter)
                    alphabet.insert(next_letter_index,active_letter)
                else:
                    pass
            else:
                pass

        return alphabet

    def main(alphabet,word_list):
        """
        The main function which takes the list of words and any known data about the alphabet.
        !!!! Now works in one iteration !!!!
        """
        for root, similar_words in generate_similar_words(word_list):

            # This is why I love python. This comprehension returns the letter after the root
            # for each word in the list. Clear and concise!
            ordered_letters = [word[len(root)] for word in similar_words if len(word) > len(root)]

            # Remove Duplicates, lets us skip a conditional later. Could have been on previous line too
            unique_ordered_letters = list(OrderedDict.fromkeys(ordered_letters))

            # Rearanges the alphabet using the list of ordered letters
            alphabet = rearrange_alphabet(alphabet, unique_ordered_letters)

        return alphabet

    return main(alphabet,word_list)


"""
NOTES v2:
1. Would it be more efficient to use recursion for some of these functions? Specifically
for the rearrange_alphabet() function, it may be better to iterate through ordered_letters
recursively because they are moving by twos anyways.


NOTES v1:
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
#
if __name__ == '__main__':
    alphabet = final_v2(file_name)
    conversion_dict = build_conversion_dict(alphabet)
    for word in extract_word_list(file_name):
        converted_word = unscramble_word(word,conversion_dict)
        print converted_word
    print_output(alphabet)
