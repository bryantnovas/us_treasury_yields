import pandas as pd
import sqlite3


def scrape_and_save():
    url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield'
    html = pd.read_html(url, header=0, attrs={"class": "t-chart"})[0]
    with sqlite3.connect('db.sqlite3') as conn:
        html.to_sql('yields', conn, if_exists='replace')


if __name__ == '__main__':
    scrape_and_save()
