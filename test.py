import collections
import sys

print(sys.version)
sentence = 'hi rob this is a python program'

word_dict = collections.OrderedDict()
for word in sentence.split(' '):
     word_dict[word] = len(word)
print(word_dict)

summoner_info = {
    'name': 'a',
    'id': 123,
    'summonerLevel': 4,
}

print("""
Summoner's Name:  {name}
Summoner's ID:    {id}
Summoner's Level: {summonerLevel}
""".format(**summoner_info))


def error_message(response):
    error_message_dict = {
        400: "Please enter a different Summoner's Name...",
        401: "Unauthorized request, please try again...",
        # ...
    }
    try:
        return error_message_dict[response.status_code]
    except KeyError as e:
        return 'Unknown error, code: {0}'.format(e.args[0])

print(error_message(response))
