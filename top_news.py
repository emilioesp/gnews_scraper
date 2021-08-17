import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import date, timedelta, datetime
import urllib.parse
from tqdm import tqdm
from info import countries_info
import newsscraper


def create_topic_news(country_code, get_text=False, num=10):
    engine_countries = ['ar', 'br', 'cl', 'co', 'mx', 'pe', 've']
    topic = countries_info[country_code.upper()]['topic_id']
    language = countries_info[country_code.upper()]['gl_language_id']
    if country_code in engine_countries:
        news_url = 'https://news.google.com/rss/topics/' + topic + '?hl={}&gl={}&ceid={}:{}'.format(language, country_code, country_code, language)
    else:
        news_url = 'https://news.google.com/rss/topics/' + topic + '?hl={}&gl=US&ceid=US:{}'.format(language, language)
    #news_url = urllib.parse.quote_plus(news_url)
    try:
        response = requests.get(news_url,  timeout=10)
        soup = BeautifulSoup(response.content, "xml")
        items, news = soup.findAll("item"), []
        for i in items[: num]:
            dic = {}
            dic['title'], dic['link'], dic['source'], dic['date'] = i.title.text, i.link.text, i.source.text, i.pubDate.text
            if get_text:
                title, authors, text, image, date = get_article_web(i.link.text, langauge='es', retries=10)
                dic['title'], dic['authors'], dic['text'], dic['image'], dic['date'] = title, authors, text, image, date
            news.append(dic)
        response.close()
        del response
    except:
    	news=[]
    return news


paises = [ 'ar', 'bo', 'cl', 'co', 'cr', 'do', 'gt', 'hn', 'mx',
          'ni', 'pa', 'pe', 'pr', 'py', 'uy', 've', 'ec']

today = date.today().strftime("_%Y_%m_%d")

for j in tqdm(range(len(paises))):
    pais = paises[j]
    print(pais)
    news = create_topic_news(pais, num=1000)
    df = pd.DataFrame(news)
    try:
        df['date'] = df['date'].apply(newsscraper.create_date_corrected)
        df['title_corrected'] = df['title'].apply(newsscraper.extract_good_title)
        df = df.drop_duplicates(subset=['link'])
        df = df.drop_duplicates(subset=['title_corrected'])
        df = df.sort_values('date')
    except:
        pass
    df.to_csv('./top_news/top_news_' + pais + today + '.csv', sep='\t', index=False)
