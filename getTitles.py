import bs4
import requests
from collections import Counter
# this is the code for getting all the titles of from the above page 
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books = []
for x in range(1,50):
   get_the_information = requests.get(base_url.format(x))
   html_code = bs4.BeautifulSoup(get_the_information.text,'lxml')
   product = html_code.select(".product_pod")
   for y in range(len(product)):
       titles = product[y].select("a")[1]
       books.append(titles.getText())