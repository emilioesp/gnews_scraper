from tqdm import tqdm
import pandas as pd
import itertools
from info import countries_info
import newsscraper


def get_news(country, query, start_day, end_day):
    country_info = countries_info[country.upper()]
    combinations = list(itertools.product(query, country_info['newspapers']))
    input_dict_list = [{'country_code': country.upper(), 'keyword': c[0],
                        'paper': c[1], 'start_day': start_day, 'end_day': end_day,
                        'num': 100, 'language': country_info['gl_language_id'],
                        'text': False} for c in combinations]
    news = newsscraper.extract_keyword_news_from_paper_dict_mp(
                       input_dict_list, cut_by=20, maxlenght=20)
    news = list(itertools.chain.from_iterable(news))
    df = pd.DataFrame(news)
    try:
        df['date'] = df['date'].apply(newsscraper.create_date_corrected)
        df['title_corrected'] = df['title'].apply(newsscraper.extract_good_title)
        df = df.drop_duplicates(subset=['link'])
        df = df.sort_values('date')
    except:
        pass
    return df
    

def get_news_paper(country, query, periodico, start_day, end_day):
    country_info = countries_info[country.upper()]
    combinations = list(itertools.product(query, periodico))
    input_dict_list = [{'country_code': country.upper(), 'keyword': c[0],
                        'paper': c[1], 'start_day': start_day, 'end_day': end_day,
                        'num': 100, 'language': country_info['gl_language_id'],
                        'text': False} for c in combinations]
    news = newsscraper.extract_keyword_news_from_paper_dict_mp(
                       input_dict_list, cut_by=20, maxlenght=20)
    news = list(itertools.chain.from_iterable(news))
    df = pd.DataFrame(news)
    df['date'] = df['date'].apply(newsscraper.create_date_corrected)
    df['title_corrected'] = df['title'].apply(newsscraper.extract_good_title)
    df = df.drop_duplicates(subset=['link'])
    df = df.sort_values('date')
    return df
