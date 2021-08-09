from tqdm import tqdm
import pandas as pd
import clean_news
from get_news import *
from summarizer_news import summarize_news
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import os
# from apply_model import polaridad

def create_months_between_dates(begin='2019-01-01', end='2021-05-01'):
    """
    Input:
        begin: str ofthe initial date,
        end: str of the final date,
    Return:
        months: list of all the months between the initial and the final date
    """
    B, E = begin.split('-'), end.split('-')
    B, E = [int(b) for b in B], [int(e) for e in E]
    sdate, edate = date(B[0], B[1], B[2]), date(E[0], E[1], E[2])
    delta = edate - sdate
    months = []
    for i in range(int(delta.days/30) + 1):
        months.append(sdate + relativedelta(months=+i))
    months = [str(d.year)+'-'+('0' + str(d.month))[-2:]+'-'+('0' + str(d.day))[-2:] for d in months]
    return months

def create_weeks_between_dates(begin='2019-01-01', end='2021-07-15'):
    """
    Input:
        begin: str ofthe initial date,
        end: str of the final date,
    Return:
        weeks: list of all the weeks between the initial and the final date
    """
    B, E = begin.split('-'), end.split('-')
    B, E = [int(b) for b in B], [int(e) for e in E]
    sdate, edate = date(B[0], B[1], B[2]), date(E[0], E[1], E[2])
    delta = edate - sdate
    weeks = []
    for i in range(int(delta.days/7) + 1):
        weeks.append(sdate + relativedelta(weeks=+i))
    weeks = [str(d.year)+'-'+('0' + str(d.month))[-2:]+'-'+('0' + str(d.day))[-2:] for d in weeks]
    return weeks


queries = ['migracion', 'migrante', 'refugiad']

queries_br = ['migraçao', 'migrante', 'refugiad']

queries_en = ['migration', 'migrant', 'refugee']

queries_nl = ['migratie', 'migrant', 'vluchteling']

queires_fr = ['migration', 'migrant','réfugié']

# paises = ['ar', 'co', 'mx', 'cl', 'ec', 'pe', 'gt', 'sv', 'hn', 'br',
#           'uy', 'pr', 'bz', 'bb', 'tt', 'jm', 'sr', 'bo', 'cr', 'do',
#           'ni', 'uy', 'py', 'gf']

paises = [ 'gt', 'hn', 'mx',
          'ni', 'pa', 'pe', 'pr', 'py', 'uy', 've']

for pais in paises:
    if pais == 'br':
        q = queries_br
    elif pais in ['bz', 'bb', 'tt', 'jm']:
        q = queries_en
    elif pais == 'sr':
        q = queries_nl
    elif pais == 'fr':
        q = queries_fr
    else:
        q = queries
    print(pais)
    months = create_months_between_dates(begin='2019-01-01', end='2021-07-15')
    df = pd.DataFrame()
    for j in tqdm(range(len(months)-1)):
        df1 = get_news(pais, q, months[j], months[j+1])
        df = pd.concat([df, df1], ignore_index=True)
        df.to_csv('./news/news_'+pais+'.csv', sep='\t', index=False)


news = os.listdir('news')

topics = ['migracion', 'migrante', 'migrantes', 'refugiados', 'refugiado',
          'refugiada', 'refugiadas', 'migra', 'migración', 'migratoria',
          'refugian', 'migraçao', 'xenofob', 'extranjer', 'ciudadanos',
          'desplazad',
          'migration', 'migrant', 'refugee',
          'migratie', 'migrant', 'vluchteling', 'xenofobie', 'buitenland'
          ]

for n in news:
    print(n)
    df = pd.read_csv('news/'+n, sep='\t')
    df = df.dropna()
    df = df.drop_duplicates()
    df1 = clean_news.get_topics(df, topics)
    df1.to_csv('./news_cln/'+n[:-4]+'_cln.csv', sep='\t', index=False)

import nltk
nltk.download('punkt')


for n in paises:
    print(n)
    df_t = pd.read_csv('news_cln/news_'+n+'_cln.csv', sep='\t')
    df_t['summary'] = [summarize_news(url, lenguaje='es', SENTENCES_COUNT=3) for url in df_t['link']]
    df_t.to_csv('./news_resumen/news_'+n+'_resumen.csv', sep='\t', index=False)
