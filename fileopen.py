import requests 
import bs4 
url = "https://www.nytimes.com/2023/03/30/learning/whats-going-on-in-this-graph-april-5-2023.html"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text)
pretty_html_string = soup.prettify()
print(pretty_html_string)
with open("NYTweb.html", "w") as f:
    f.write(pretty_html_string)

with open("NYTweb.html", "r") as f:
    pretty_html_string = f.read()


soup = bs4.BeautifulSoup(pretty_html_string)
print(soup.prettify())