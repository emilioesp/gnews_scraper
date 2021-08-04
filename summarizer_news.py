from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser.
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import trafilatura

def summarize_news(url, lenguaje='es', SENTENCES_COUNT=10):
    tokenizer = Tokenizer(lenguaje)
    stemmer = Stemmer(lenguaje)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(lenguaje)
    # parser = HtmlParser.from_url(url, tokenizer)
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.process_record(downloaded, include_comments=False,
                                      include_tables=False, deduplicate=False,
                                      target_language="es", include_formatting=False)
    parser = parser = PlaintextParser.from_string(text, tokenizer)
    res = [str(s)+' ' for s in summarizer(parser.document, SENTENCES_COUNT)]
    rv = ''
    for s in res:
        rv += s
    return rv
