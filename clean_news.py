import numpy as np
import pandas as pd


def strip_accents(w):
    """
    Dada una palabra 'w' quita los acentos. En caso de ser necesario.
    """
    w = w.lower()
    letters = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    for i, j in letters.items():
        w = w.replace(i, j)
    return w


def get_topics(df, words):
    """
    Dado un dataframe df y una lista de plabras a seleccionar 'words'
    Busca estas palabras en el titular de la noticia
    y en el link de la misma y si aparece alguna,
    entonces se conserva la noticia.
    """
    pattern = '|'.join(words)
    df1 = df.loc[df.title_corrected.str.contains(pattern)]
    return df1


def clean_topics(df, nowords):
    """
    Dado un dataframe df y una lista de plabras a seleccionar 'words'
    Busca estas palabras en el titular de la noticia
    y en el link de la misma y si aparece alguna,
    entonces se conserva la noticia.
    """
    pattern = '|'.join(nowords)
    df1 = df.loc[~df.title_corrected.str.contains(pattern)]
    return df1


def clean_news(df, words, nowords):
    df1 = get_topics(df, words)
    df2 = clean_topics(df1, nowords)
    return df2

# Topics for get_topics
topics = ['migracion', 'migrante', 'migrantes', 'refugiados', 'refugiado',
          'refugiada', 'refugiadas', 'migran', 'migración', 'migratoria',
          'refugian', 'migraçao', 'xenofob', 'extranjer', 'ciudadanos',
          'desplazad',
          'migration', 'migrant', 'refugee',
          'migratie', 'migrant', 'vluchteling', 'xenofobie', 'buitenland'
          ]

# Lista de paíse a quitar con clean_topics
nowords = ['libia', 'libano', 'grecia', 'croacia', 'europa']
other_topic = ['euro', 'austria', 'aleman', 'francia', 'hungria', 'hungar', 'cadiz', 'suecia', 'bulgaria', 'italia',
               'mediterrane', 'españa', 'camboya', 'grieg', 'grecia', 'turquia', 'liberia', 'ghana', #'paris',
               'madrid', 'libia', 'etiopia', 'bangladesh', 'ceuta', 'marroqui', 'bitcoin', 'finlandia', 'belgica',
               'malasia', 'lituania', 'tunez', 'pakistan', 'afgan', 'ocean king', 'tokio', 'tokyo', 'olimpi',
               'bruselas', 'israel', 'marruecos', 'irak', 'britanic', 'reino unido', 'gran bretaña', 'subsharian',
               'yihad', 'nauru', 'vietnam', 'australia', 'kim jong un', 'pelicula', 'lesbos', 'inversion',
               'china','whatsapp', 'davies', 'bayern', 'catar', 'rohingya', 'dinamarca'] #se puede incluir siria y derivados, excepto para argentina
nowords = nowords + other_topic
