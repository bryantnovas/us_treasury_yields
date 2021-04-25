import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def scrape_and_save():
    url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield'
    html = pd.read_html(url, header=0, attrs={"class": "t-chart"})[0]
    with sqlite3.connect('db.sqlite3') as conn:
        html.to_sql('yields', conn, if_exists='replace')
    plot_screenshot(html)


def plot_screenshot(df):
    df1 = df.iloc[:, 1:5]
    df2 = df.iloc[:, 5:]

    plt.figure(1, figsize=(10, 8))
    plt.plot(df['Date'], df1)
    plt.xticks(rotation=60, fontsize='small')
    plt.title('Month based bonds yield change')
    plt.legend(labels=df1.columns)
    plt.ylabel('Interest %')
    plt.xlabel('Day')

    plt.savefig('./static/img/monthly_yields.png')

    plt.title('Year based bonds yield change')
    plt.plot(df2)
    plt.legend(labels=df2.columns)
    plt.ylabel('Interest % ')
    plt.xlabel('Day ')

    plt.savefig('./static/img/yearly_yields.png')


if __name__ == '__main__':
    scrape_and_save()
