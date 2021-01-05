import bs4
import requests
from collections import Counter
#code to get the top ten quotes from all the pages 
base_url = "http://quotes.toscrape.com/page/"
top_quotes = []
page_counter = 1
while True:
    raise_request = requests.get(base_url+str(page_counter))

    if "No quotes found!" in (raise_request.text):
        print("LAST PAGE")
        break
    else:
        page_counter +=1
        pass
    beautiful_soup = bs4.BeautifulSoup(raise_request.text,"lxml")
    main_class = beautiful_soup.select(".container")[0]
    get_tags = main_class.select(".tag")
    for each_tag in get_tags:
        top_quotes.append(each_tag.getText())
my_list = Counter(top_quotes)
print(my_list)