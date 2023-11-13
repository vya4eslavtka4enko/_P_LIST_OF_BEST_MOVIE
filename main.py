from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com')
y_hacker_news = response.text


soup = BeautifulSoup(y_hacker_news,'html.parser')
data = soup.find_all('span',{'class':"titleline"})
article_text = []
article_links = []
for article_tag in data:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = 'span', class_= 'score')]

maxs = max(article_upvotes)



print(maxs)
largest_index = article_upvotes.index(maxs)
print(article_text[largest_index])
print(article_links[largest_index])
# print(article_text)