def fuzzy_search(sample, words):
    for word in words:
        found_index = 0
        for s_let in sample:
            for index, letter in enumerate(word[found_index:]):
                if s_let == letter:
                    found_index += index + 1
                    break
            else:
                break
        else:
            yield word
    else:
        yield None

sample = 'qui'

words = [
    'turquise',
    'turquoise',
    'turuise',
    'turiquese'
]

for match in fuzzy_search(sample, words):
    print(match)
