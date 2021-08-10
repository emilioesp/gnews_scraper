import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

#####################
#Volumen de noticias#
#####################

PAISES_BID = {'ARGENTINA': '#74ACDF',
              'BAHAMAS': '#2E778C',
              'BARBADOS': '#FFC000',
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
              'PUERTO RICO': '#0437F2',
              'EL SALVADOR': '#8cf0f5',
              'URUGUAY': '#0038A8',
              'NICARAGUA': '#0067C7',
              'VENEZUELA': '#FAD149',
              'TRINIDAD Y TOBAGO': '#EE4B2B',
              'JAMAICA': '#4CBB17',
              'SURINAME' : '#228B22',
              'GUYANA FRANCESA': '#488214'
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
                'br':'BRASIL',
                'uy': 'URUGUAY',
                'pr': 'PUERTO RICO',
                'bz': 'BELICE',
                'bb': 'BARBADOS',
                'tt': 'TRINIDAD Y TOBAGO',
                'jm': 'JAMAICA',
                'sr': 'SURINAME',
                'gf' : 'GUYANA FRANCESA',
                'do': 'REPUBLICA DOMINICANA',
                'ni' : 'NICARAGUA',
                'py' : 'PARAGUAY',
                'pa' : 'PANAMA',
                'bo': 'BOLIVIA',
                'cr' : 'COSTA RICA',
                've' : 'VENEZUELA'
               }
paises_codes_correct = {'ar':'ARGENTINA',
                'co': 'COLOMBIA',
                'mx': 'MÉXICO',
                'cl': 'CHILE',
                'ec': 'ECUADOR',
                'pe': 'PERÚ',
                'gt': 'GUATEMALA',
                'sv': 'EL SALVADOR',
                'hn': 'HONDURAS',
                'br': 'BRASIL',
                'uy': 'URUGUAY',
                'pr': 'PUERTO RICO',
                'bz': 'BELICE',
                'bb': 'BARBADOS',
                'tt': 'TRINIDAD Y TOBAGO',
                'jm': 'JAMAICA',
                'sr': 'SURINAME',
                'gf': 'GUYANA FRANCESA',
                'do': 'REPÚBLICA DOMINICANA',
                'ni': 'NICARAGUA',
                'py': 'PARAGUAY',
                'pa': 'PANAMÁ',
                'bo': 'BOLIVIA',
                'cr': 'COSTA RICA',
                've': 'VENEZUELA'
               }


paises = ['ar', 'bb', 'bo', 'br', 'bz', 'cl', 'co', 'cr', 'do', 'ec', 'gt', 'hn', 'jm', 'mx', 'ni', 'pa', 'pe', 'pr', 'py', 'sr', 'sv', 'tt', 'uy', 've']
# Se quitó gf
df = pd.DataFrame()
for pais in paises:
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
    df_date = df_date[df_date['date']>= '2017-01-01']
    # SMA 7-days
    df_date['Núm. noticias'] = df_date['count'].rolling(7, min_periods=1).mean()*10
    df_date['país'] = [paises_codes_correct[pais]] * len(df_date)
    df = pd.concat([df, df_date])

fig = px.line(df, x='date', y = 'Núm. noticias',
              color_discrete_sequence=[k[1] for k in PAISES_BID.items()],
              color='país',
              facet_row_spacing=0.04,
              height=900,    
              facet_col='país', facet_col_wrap=3)
fig.update_yaxes(matches=None)
fig.for_each_annotation(lambda a: a.update(text=a.text.replace("país=", "")))
for axis in fig.layout:
    if type(fig.layout[axis]) == go.layout.YAxis:
        fig.layout[axis].title.text = ''

for axis in fig.layout:
    if type(fig.layout[axis]) == go.layout.XAxis:
        fig.layout[axis].title.text = ''

fig.update_layout(
    # keep the original annotations and add a list of new annotations:
    annotations = list(fig.layout.annotations) + 
                  [go.layout.Annotation(x=-0.07,
                          y=0.5,
                          font=dict(size=14),
                          showarrow=False,
                          text="Núm. de noticias",
                          textangle=-90,
                          xref="paper",
                          yref="paper"
                          )],
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',)


fig.write_image(f"images/SMA_7d_noticias_sep.png")
