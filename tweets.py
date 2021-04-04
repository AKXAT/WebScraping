import bs4
import requests

base_url = 'https://twitter-trends.iamrohit.in/india'
raise_request = requests.get(base_url)
get_html = bs4.BeautifulSoup(raise_request.text,'lxml')
choose_titles = get_html('div')[5].select('a')
choose_counts = get_html.select('div')[5].select('.tweet-count')
for i in range(0,10,1):
    for each_hashtag in choose_titles[i]:
        print(each_hashtag.replace("#",""))
    for each_count in choose_counts[i].find('span'):
        count = each_count.replace("Tweets","")
        remove_sign = count.replace("<","")
        print(remove_sign)