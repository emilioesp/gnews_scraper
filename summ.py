import pandas as pd
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def summarizers(text, lenguaje='es', SENTENCES_COUNT=3):
    tokenizer = Tokenizer(lenguaje)
    stemmer = Stemmer(lenguaje)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(lenguaje)
    parser = PlaintextParser.from_string(text, tokenizer)
    res = [str(s)+' ' for s in summarizer(parser.document, SENTENCES_COUNT)]
    rv = ''
    for s in res:
        rv += s
    return rv


def news_day(df):
    df['count'] = [1]*len(df)
    dfg1 = df.groupby('date').sum()
    df1 = df.drop_duplicates(subset=['summary'])
    dfgg = df1.groupby('date')['summary'].sum()
    dfg2 = dfgg.apply(summarizers)
    dfg = pd.concat([dfg1, dfg2], axis=1)
    dfg = dfg.reset_index()
    return dfg
