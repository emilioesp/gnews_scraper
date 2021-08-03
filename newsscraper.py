import requests
import numpy as np
from tqdm import tqdm
from bs4 import BeautifulSoup
from newspaper import Article
from textblob import TextBlob
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from textblob import Word
from nltk.corpus import stopwords
import networkx as nx
import multiprocessing as mp
import unicodedata
import re
from datetime import date, timedelta, datetime
from gensim.summarization.summarizer import summarize
import urllib.parse


def search(query):
    q = "+".join(query.split(" "))
    return q


def get_article_web(web, langauge='es', retries=10):
    article = Article(web, language=langauge)
    for j in range(retries):
        try:
            article.download()
            article.parse()
            title, authors, text = article.title, article.authors, article.text
            image = article.top_image if article.has_top_image() else ''
            date = str(article.publish_date)
            break
        except:
            title, authors, text, image, date = '', '', '', '', ''
    return title, authors, text, image, date



# ----------------------------------- https://news.google.com/search?q=fibras%20quimicas&hl=es-419&gl=MX&ceid=MX%3Aes-419

def create_query_news(query, country_code, language='es-419', get_text=False, num=10):
    engine_countries = ['ar', 'br', 'cl', 'co', 'mx', 'pe', 've']
    if query == '':
        news_url = "https://news.google.com/rss?&hl={}&gl={}&ceid={}:{}".format(language, country_code, country_code, language)
    elif country_code in engine_countries:
        news_url = 'https://news.google.com/rss/search?q=' + search(query) + '&hl={}&gl={}&ceid={}:{}'.format(language, country_code, country_code, language)
    else:
        news_url = 'https://news.google.com/rss/search?q=' + search(query) + '&hl={}&gl=US&ceid=US:{}'.format(language, language)
    #news_url = urllib.parse.quote_plus(news_url)
    try:
        response = requests.get(news_url,  timeout=10)
        soup = BeautifulSoup(response.content, "xml")
        items, news = soup.findAll("item"), []
        for i in items[: num]:
            dic = {}
            dic['title'], dic['link'], dic['date'] = i.title.text, i.link.text, i.pubDate.text
            if get_text:
                title, authors, text, image, date = get_article_web(i.link.text, langauge='es', retries=10)
                dic['title'], dic['authors'], dic['text'], dic['image'], dic['date'] = title, authors, text, image, date
            news.append(dic)
        response.close()
        del response
    except:
    	news=[]
    return news


def similarity_between_text(textos_en):
    text_join = unify_text(textos_en)
    list_words = TextBlob(text_join)
    list_words = np.array(list(set(list_words.words)))
    matrix = np.zeros((len(list_words), len(textos_en)))
    j = 0
    for j in range(0, len(textos_en)):
        t = textos_en[j]
        tex = list(TextBlob(t).words)
        matrix[:,j] = np.isin(np.array(list_words), tex)*1
    S = cosine_similarity(matrix)
    return S


def create_days_between_dates(begin='2020-01-01', end='2020-01-01'):
    B, E = begin.split('-'), end.split('-')
    B, E = [int(b) for b in B], [int(e) for e in E]
    sdate, edate = date(B[0], B[1], B[2]), date(E[0], E[1], E[2])  # start date, end date
    delta = edate - sdate       # as timedelta
    days = []
    for i in range(delta.days + 1):
        days.append(sdate + timedelta(days=i))
    days = [str(d.year)+'-'+('0' + str(d.month))[-2:]+'-'+('0' + str(d.day))[-2:] for d in days]
    return days


def create_date_corrected(stri):
    mons = ['','Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    date_split = stri.split(' ')
    day, month, year = date_split[1], date_split[2], date_split[3]
    date_corrected = year + '-' + ('0'+str(mons.index(month)))[-2:] +'-'+ ('0'+str(day))[-2:]
    return date_corrected


def extract_keyword_news_from_paper_dict(dic):
    '''
    version: 2021/07/22
    '''
    country_code = dic['country_code']
    keyword = dic['keyword']
    paper = dic['paper']
    start_day = dic['start_day']
    end_day = dic['end_day']
    num = dic['num']
    language = dic['language']
    text = dic['text']
    rv = []
    q = keyword + ' * source:https://{}+after:{}+before:{}'.format(paper, start_day, end_day)
    news_1 = create_query_news(q, country_code, language, text, num)
    q = keyword + ' * source:http://{}+after:{}+before:{}'.format(paper, start_day, end_day)
    news_2 = create_query_news(q, country_code, language, text, num)
    q = keyword + ' * https://{}+after:{}+before:{}'.format(paper, start_day, end_day)
    news_3 = create_query_news(q, country_code, language, text, num)
    q = keyword + ' * http://{}+after:{}+before:{}'.format(paper, start_day, end_day)
    news_4 = create_query_news(q, country_code, language, text, num)
    q = keyword + ' * {}+after:{}+before:{}'.format(paper, start_day, end_day)
    news_5 = create_query_news(q, country_code, language, text, num)
    q =  keyword + ' * site:{}'.format(paper)
    news_6 = create_query_news(q, country_code, language, text, num)
    for news_q in [news_1, news_2, news_3, news_4, news_5, news_6]:
        for note in news_q:
            if note not in rv:
                if paper in note['link']:
                    rv.append(note)
    return rv


def extract_keyword_news_from_paper_dict_mp(list_dic, cut_by=85, maxlenght=85):
    entero, list_dic_cutted = len(list_dic) // cut_by, []
    for i in range(entero + 1):
        list_dic_cutted.append(list_dic[i*cut_by: (i+1)*cut_by])
    if len(list_dic) <= maxlenght:
        pool = mp.Pool(processes = maxlenght)
        rv = pool.map(extract_keyword_news_from_paper_dict, list_dic)
        pool.close()
        pool.join()
    else:
        rv = []
        for l in list_dic_cutted:
            pool = mp.Pool(processes = maxlenght)
            rv += pool.map(extract_keyword_news_from_paper_dict, l)
            pool.close()
            pool.join()
    return rv


def extract_articles_from_web_list_mp(list_dic, cut_by=50, maxlenght=50):
    entero, list_dic_cutted = len(list_dic) // cut_by, []
    for i in range(entero + 1):
        list_dic_cutted.append(list_dic[i*cut_by: (i+1)*cut_by])
    if len(list_dic) <= maxlenght:
        pool = mp.Pool(processes=maxlenght)
        rv = pool.map(get_article_web, list_dic)
        pool.close()
        pool.join()
    else:
        rv = []
        for l in list_dic_cutted:
            pool = mp.Pool(processes=maxlenght)
            rv += pool.map(get_article_web, l)
            pool.close()
            pool.join()
    return rv


def drop_unnamed_columns(df_file):
    cols = list(df_file.columns)
    un = [c for c in cols if 'Unnamed' in c]
    if len(un)==0:
        rv = df_file
    else:
        rv = df_file.drop(un, axis=1)
    return rv


def extract_good_title(title):
    periodico = title.split(' - ')[-1]
    rv = title.replace(periodico, '')
    rv = rv.replace(' - ','').replace(' | ','')
    return rv


def create_summarize_gen(texto, word_count=50, ratio=0.6):
    try:
        s = summarize(texto.strip(), ratio=ratio, word_count=word_count, split=False)
    except:
        s = texto
    return s


def create_summarize_gen_mp(list_dic, cut_by=50, maxlenght=50):
    entero, list_dic_cutted = len(list_dic) // cut_by, []
    for i in range(entero + 1):
        list_dic_cutted.append(list_dic[i*cut_by: (i+1)*cut_by])
    if len(list_dic) <= maxlenght:
        pool = mp.Pool(processes=maxlenght)
        rv = pool.map(create_summarize_gen, list_dic)
        pool.close()
        pool.join()
    else:
        rv = []
        for l in tqdm(list_dic_cutted):
            pool = mp.Pool(processes=maxlenght)
            rv += pool.map(create_summarize_gen, l)
            pool.close()
            pool.join()
    return rv
