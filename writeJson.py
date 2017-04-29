import json
import os

'''
This file will write the python dictionary to json file
'''
animeQuote = {
    "author": "Yukino Miyashita",
    "anime": "Octave",
    "quote": 'Someone told me this: "Nothing is "forever" in human relationships". That might be true, but it sounds awfully lonely. But I realized today... If there really is no such thing as "forever"... Then having someone important is the happiest thing one can attain in life.'
}

animeQuote2 = {
    "author": "foo",
    "anime": "foo2",
    "quote": 'foofofofofoat might be true, but it sounds awfully lonely. But I realized today... If there really is no such thing as "forever"... Then having someone important is the happiest thing one can attain in life.'
}


def write_to_json(quote_dics):
    '''
    Write the dictionary to json file
    :param quote_dics: the dictionary that contains all the quotes
    '''
    assert type(quote_dics) == list and len(quote_dics) >= 1

    with open("quotes.json", 'w') as f:
        json.dump([], f)
    with open("quotes.json", 'w') as f:
        json.dump(quote_dics, f)