import requests 
import bs4 
import pandas as pd
import matplotlib.pyplot as plt 
# url = "https://data.bls.gov/timeseries/APU0000708111" 
# response = requests.get(url)

# soup = bs4.BeautifulSoup(response.text)
# pretty_html_string = soup.prettify()
# print(pretty_html_string)
# with open("Eggweb.html", "w") as f:
#     f.write(pretty_html_string)

with open("Eggweb.html", "r") as f:
    pretty_html_string = f.read()


# soup = bs4.BeautifulSoup(pretty_html_string)
# print(soup.prettify())


df = pd.read_html("Eggweb.html") [1]
print(df)
print(df.info ())
df.plot( x = "Year", y = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
# df.plot (x = "Major", y = "Median")
plt.show()