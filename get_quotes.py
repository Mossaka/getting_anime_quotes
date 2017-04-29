'''

This file will get all the quotes from website: http://www.less-real.com
and write to a json file with contents: author, anime, quote

All quotes credit to http://www.less-real.com

'''

import requests
from bs4 import BeautifulSoup as bs
from writeJson import write_to_json

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                                 "Chrome/22.0.1207.1 Safari/537.1"}

main_url = "http://www.less-real.com/?p="

python_list = []

def get_quotes( url ):
    try:
        start_url = requests.get(url, headers=headers)
        bsObj = bs(start_url.text, 'lxml')

        quotes_div = bsObj.findAll("div", {"class": "quote"})

        for quote_div in quotes_div:
            author = quote_div.findAll('a', href=True)[0].string
            anime = quote_div.findAll('a', href=True)[-1].string
            quote = quote_div.find('span', {'class': 'quoteText'}).string

            python_dic = {}
            python_dic["author"] = author
            python_dic["anime"] = anime
            python_dic["quote"] = quote

            python_list.append(python_dic)

            print("appending quote from {} to file right now".format(author))
    except:
        print("this {} is not working".format(url))


if __name__ == '__main__':
    for i in range(1, 424):
        get_quotes(main_url + str(i))

    print(len(python_list))

    write_to_json(python_list)