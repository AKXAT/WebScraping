import bs4
import requests
from collections import Counter
# the below code is to get all books which have a rating of three or below 
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books = []
for x in range(1,50):
    get_the_information = requests.get(base_url.format(x))
    html_code = bs4.BeautifulSoup(get_the_information.text,'lxml')
    print(type(html_code))
    product = html_code.select(".product_pod")
    for products in product:
        rating_one = len(products.select(".star-rating.One"))
        rating_two = len(products.select(".star-rating.Two"))
        rating_three = len(products.select(".star-rating.Three"))

        if rating_one != 0 or rating_two != 0 or rating_three !=0:
            book_title = products.select("a")[1]["title"]
            print(book_title)