from bs4 import BeautifulSoup
import requests

WEBSITE_TO_SCRAPE = "https://news.ycombinator.com/news"

response = requests.get(WEBSITE_TO_SCRAPE)

webpage_html = response.text

soup= BeautifulSoup(webpage_html, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_upvote = max(article_upvote)
largest_index = article_upvote.index(largest_upvote)


print(article_texts[largest_index])
print(article_links[largest_index])