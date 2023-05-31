import requests 
import bs4 
import pandas as pd
import matplotlib.pyplot as plt 
# url = "https://data.bls.gov/timeseries/APU0000708111" 
# response = requests.get(url)

#Opens and reads an HTML file 
with open("Eggweb.html", "r") as f:
    # assigns it to pretty html 
    pretty_html_string = f.read()


# soup = bs4.BeautifulSoup(pretty_html_string)
# print(soup.prettify())

#stores to dataframe 
df = pd.read_html("Eggweb.html") [1]
# reshapes into long format, changing columns 
df = pd.melt(
    df,
    id_vars="Year",
    value_vars=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    var_name= "Month",
    value_name="Cost",
    ignore_index= True
)
#change columns to be date, combining month and year 
df["Date"] = df["Year"].astype("str") + "-" + df["Month"] + "-1"
df['Date'] = pd.to_datetime(df["Date"], format = "%Y-%b-%d")
print(df)
# df['Date'] = pd.to_datetime(df[['Year','Month']].assign(Day = 1))
print(df.info ())
#creates the plot 
df.plot( x = "Date", y = "Cost")
#titles the plot
plt.xlabel("Date")
plt.ylabel("Cost")
plt.title("The Cost of Eggs Over 10 Years")


plt.show()