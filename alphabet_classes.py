import string
from collections import OrderedDict

"""
NOTES:

1. Is it ok to extend classes from lists? I saw something that said that isn't a
good idea, but I don't see any immediate disadvantages.

2. In what cases should functions be nested in classes? It seems like it makes sense
sometimes, but I could see it getting confusing, especially in unfamiliar code.
"""

class Alphabet(list):
    def __init__(self, *args):
        list.__init__(self, *args)

    def rearrange_alphabet(self, ordered_letters):
        """Rearanges the alphabet closer to the correct order using a list of known ordered letters"""
        for active_letter, next_letter in zip(ordered_letters, ordered_letters[1:]):

            # Find active and next letters' index in list, or add it to the end of alphabet
            active_letter_index = self.get_index(active_letter)
            next_letter_index = self.get_index(next_letter)

            # If current_letter is after next_letter in alphabet, move it in front.
            if active_letter_index > next_letter_index:
                self.remove(active_letter)
                self.insert(next_letter_index,active_letter)

    def get_index(self, letter):
        """
        Get the index location in alphabet for a letter. If the letter does not
        exist, add it to the end of alphabet
        """
        if letter not in self:
            self.append(letter)

        return self.index(letter)

    def __str__(self):
        """Print current alphabet knowledge"""
        return '\n'.join(["Letter {0} => '{1}'".format(i+1, letter) for i,letter in enumerate(self)])

    def build_conversion_dict(self):
        """
        Build OrderedDict for conversion to unscrambeled alphabet
        Note: Assumes complete english alphabet exists in object
        """
        return OrderedDict((scrambled_letter, alpha_letter) for scrambled_letter, alpha_letter in zip(self,string.ascii_lowercase))


class WordList(list):
    def __init__(self, *args):
        list.__init__(self, *args)

    def generate_similar_words(self, min_root_length=3):
        def get_root_word(active_word, adjacent_word, min_length):
            """Generates root words by comparing adjacent words. Can set a minimum length"""
            for i,_ in enumerate(active_word):
                # Continue to next letters while the word fragments match
                root_length = i + min_length
                if active_word[:root_length+1] != adjacent_word[:root_length+1]:
                    break
            return active_word[:root_length]

        def find_words_matching_root(active_word, entry_num, root):
            """Generate words with a similar root"""
            root_length = len(root)

            # TODO - Is this loading the entire list in memory again? Maybe islice
            for potential_match in self[entry_num:]:
                if active_word[:root_length] == potential_match[:root_length]:
                    yield potential_match
                else:
                    break

        # Generate lists of words with all similar roots, as well as the actual root
        for entry_num,active_word in enumerate(self[:-1]):
            adjacent_word = self[entry_num+1]
            root = get_root_word(active_word, adjacent_word, min_root_length)
            similar_words = list(find_words_matching_root(active_word, entry_num, root))
            if len(similar_words) > 2:
                yield root, similar_words

    @classmethod
    def word_list_from_file(cls, file_name):
        """Extract word list from file to strip extra whitespace and for easier parsing"""
        with open(file_name) as f:
            return cls([word.strip() for word in f])

def main(file_name, min_root_length=3):
    """
    Builds the word list from the text file of the scrambeled dictionary
    Generates lists of similar words by comparing roots
    Rearanges alphabet based on information from similar words
    Finally, converts word list and prints converted words and ordered alphabet

    Args:
        file_name: Text file of scrambeled word list
        min_root_length: Adjusts the unscrambeling alogrithm based on the minimum root length
    """

    alphabet = Alphabet()
    word_list = WordList.word_list_from_file(file_name)

    for root, similar_words in word_list.generate_similar_words(min_root_length):
        ordered_letters = [word[len(root)] for word in similar_words if len(word) > len(root)]
        alphabet.rearrange_alphabet(ordered_letters)

    conversion_dict = alphabet.build_conversion_dict()
    for word in word_list:
        converted_word = ''.join([conversion_dict[letter] for letter in word])
        print converted_word

    print alphabet

if __name__ == '__main__':
    file_name = 'alphabet.txt'
    min_root_length = 3
    main(file_name, min_root_length)
