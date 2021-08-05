from tqdm import tqdm
import pandas as pd
from get_news import *
from clean_news import *
from summarizer_news import *
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import os

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


queries = ['migracion', 'migrante', 'refugiad']

queries_br = ['migraçao', 'migrante', 'refugiad']
queries_en = ['migration', 'migrant', 'refugee']

queries_nl = ['migratie', 'migrant', 'vluchteling']

queires_fr = ['migration', 'migrant','réfugié']

unprocess_files = ['./news/' + f for f in os.listdir('./news/')]

for f in unprocess_files:
    df = pd.read_csv(f, sep='\t')
    begin_date = df.date.values[-1]
    end_date = str(datetime.today())[:10]
    pais = f.split('_')[-1][:2]
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
    days = create_days_between_dates(begin_date, end_date)
    for j in tqdm(range(len(days)-1)):
        df1 = get_news.get_news(pais, q, days[j], days[j+1])
        df = pd.concat([df, df1], ignore_index=True)
        df.to_csv('news/news_'+pais+'.csv', sep='\t', index=False)


news = os.listdir('news')

topics = ['migracion', 'migrante', 'migrantes', 'refugiados', 'refugiado',
          'refugiada', 'refugiadas', 'migran', 'migración', 'migratoria',
          'refugian', 'migraçao', 'xenofob', 'extranjer', 'ciudadanos',
          'desplazad',
          'migration', 'migrant', 'refugee',
          'migratie', 'migrant', 'vluchteling', 'xenofobie', 'buitenland'
          ]
nowords = ['libia', 'libano', 'grecia', 'croacia', 'europa']
other_topic = ['euro', 'austria', 'aleman', 'francia', 'hungria', 'hungar', 'cadiz', 'suecia', 'bulgaria', 'italia',
               'mediterrane', 'españa', 'camboya', 'grieg', 'grecia', 'turquia', 'liberia', 'ghana', #'paris',
               'madrid', 'libia', 'etiopia', 'bangladesh', 'ceuta', 'marroqui', 'bitcoin', 'finlandia', 'belgica',
               'malasia', 'lituania', 'tunez', 'pakistan', 'afgan', 'ocean king', 'tokio', 'tokyo', 'olimpi',
               'bruselas', 'israel', 'marruecos', 'irak', 'britanic', 'reino unido', 'gran bretaña', 'subsharian',
               'yihad', 'nauru', 'vietnam', 'australia', 'kim jong un', 'pelicula', 'lesbos', 'inversion',
               'china','whatsapp', 'davies', 'bayern', 'catar', 'rohingya', 'dinamarca'] #se puede incluir siria y derivados, excepto para argentina
nowords = nowords + other_topic

for n in news:
    print(n)
    df = pd.read_csv('news/'+n, sep='\t')
    df = df.dropna()
    df1 = clean_news(df, topics, nowords)
    df1.to_csv('news_cln/'+n[:-4]+'_cln.csv', sep='\t', index=False)
