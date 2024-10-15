from bs4 import BeautifulSoup

import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, features = "html.parser")

table = soup.find("table")
table = soup.find("table", class_ = "wikitable sortable")

tables = soup.find_all("table")

world_titles = table.find_all("th")

titles = [title.text.strip() for title in world_titles]

column_data = table.find_all("tr")

df = pd.DataFrame(columns = titles)

for row in column_data[1:]:
    row_data = row.find_all("td")

    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)

    df.loc[length] = individual_row_data

df.to_csv("companies.csv", index = False)