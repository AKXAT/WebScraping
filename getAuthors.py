import bs4
import requests
from collections import Counter
#this is the code to select specific authors from all the pages on the website
base_url = "http://quotes.toscrape.com/page/{}/"
n=11
author = []
for page in range(1,n):
    raise_request = requests.get(base_url.format(page))
    get_the_html_code = bs4.BeautifulSoup(raise_request.text,"lxml")
    choose_specific_class = get_the_html_code.select(".container")
    #check = get_the_html_code.select(".col-md-8")[1]
    for each_class in choose_specific_class:
        choose_specific_author = each_class.select(".author")
        for each_author in choose_specific_author:
            author.append(each_author.getText())

unique_author_set = set(author)
print(unique_author_set)