import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

#####################
#Volumen de noticias#
#####################

PAISES_COLOR = {'ARGENTINA': '#74ACDF',
              'BAHAMAS': '#2E778C',
              'BELICE': '#171696',
              'BOLIVIA': '#367634',
              'BRASIL': '#479C3B',
              'CHILE': '#CE3A28',
              'COLOMBIA': '#FAD149',
              'COSTA RICA': '#CF302B',
              'REPUBLICA DOMINICANA': '#042D62',
              'ECUADOR': '#452C25',
              'GUATEMALA': '#4898D1',
              'GUYANA': '#6cb36d',
              'HONDURAS': '#0F52BA',
              'MEXICO': '#2C6947',
              'PANAMA': '#DD6E6A',
              'PERU': '#671815',
              'PARAGUAY': '#6A016A',
              'EL SALVADOR': '#8cf0f5',
              'URUGUAY': '#0038A8',
              'NICARAGUA': '#0067C7',
              'VENEZUELA': '#FAD149',
              }
paises_codes = {'ar':'ARGENTINA',
                'co':'COLOMBIA', 
                'mx':'MEXICO',
                'cl':'CHILE',
                'ec':'ECUADOR',
                'pe':'PERU',
                'gt':'GUATEMALA',
                'sv':'EL SALVADOR',
                'hn':'HONDURAS',
                'br':'BRASIL'}
paises = ['ar', 'co', 'mx', 'cl', 'ec', 'pe', 'gt', 'sv', 'hn', 'br']
serie_vol = go.Figure()
for pais in paises:
    print(pais)
    df_news = pd.read_csv(f'news_cln/news_{pais}_cln.csv', sep='\t')
    df_news['date'] =  pd.to_datetime(df_news['date'], format='%Y-%m-%d')
    df_news.sort_values('date', inplace = True)
    df_date = df_news.groupby('date').count().reset_index()
    min_date = df_date.iloc[0]['date']
    max_date = df_date.iloc[-1]['date']
    idx = pd.date_range(min_date,max_date)
    s = df_date.set_index('date')['link']
    s.index = pd.DatetimeIndex(s.index)
    s = s.reindex(idx, fill_value=0)
    df_date = s.to_frame().reset_index().rename({'index': 'date', 'link': 'count'},axis=1)
    X = df_date['date'].tolist()
    Y = df_date['count'].tolist()
    serie_vol.add_trace(go.Scatter(x=X, y=Y,
                            mode='lines',
                            name=paises_codes[pais].title(),
                            marker=dict(color=PAISES_COLOR[paises_codes[pais]])
                            #visible=True if prov in main else 'legendonly'
                           ))
serie_vol.update_layout( #showlegend=False,
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       yaxis_title="",
                       margin = dict(l=10, r=10, b=10, t=10),
                       font = dict(color='white'))
serie_vol.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ]), bgcolor='#272B30'
    )
)
