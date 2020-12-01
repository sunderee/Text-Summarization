# Scraping and HTTP requests
from bs4 import BeautifulSoup, ResultSet
import urllib.request

# NLTK
from nltk import download, sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Utils
from heapq import nlargest
from re import sub
from typing import Any, Dict, List, Tuple
from sys import argv


def scrape_text(url: str) -> str:
    """
    Scrape text from a given URL and return data in HTML paragraphs
    :param url: full URL of a resource we're straping
    :return: text found in HTML paragraph (p) tags
    """
    opened_url: Any = urllib.request.urlopen(url)
    data: Any = opened_url.read()

    parsed_data: BeautifulSoup = BeautifulSoup(data, 'lxml')
    paragraphs: ResultSet = parsed_data.find_all('p')

    text = ''
    for paragraph in paragraphs:
        text += paragraph.text

    return text


def preprocessing(text: str) -> Tuple[str, str]:
    """
    Preprocessing of text, remove square brackets, extra spaces,
    special characters and digits
    :param text: input (dirty) text, grrr
    :return: output (clean) text, meow
    """
    article_text: str = sub(r'\[[0-9]*]', ' ', str(text))
    article_text: str = sub(r'\s+', ' ', str(article_text))

    formatted_article_text: str = sub('[^a-zA-Z]', ' ', str(article_text))
    formatted_article_text: str = sub(r'\s+', ' ', str(formatted_article_text))

    return article_text, formatted_article_text


def weighted_occurrence_frequency(text: str) -> Dict[str, float]:
    """
    Find frequency of each word's occurrence in a clean text,
    returning dictionary of respective words and their normalized
    frequencies
    :param text: input text
    :return: dictionary of word/frequency key-value pairs
    """
    frequencies: Dict[str, float] = {}
    for word in word_tokenize(text):
        if word not in stop_words:
            if word not in frequencies.keys():
                frequencies[word] = 1
            else:
                frequencies[word] += 1

    maximum_frequency: float = max(frequencies.values())
    for word in frequencies.keys():
        frequencies[word] = frequencies[word] / maximum_frequency

    return frequencies


def compute_sentence_scores(text: str, frequencies: Dict[str, float]) -> Dict[str, float]:
    """
    Return scores of each sentence from the frequency of word occurrences
    and sentence tokenization results. Scores are given as a dictionary
    of respective sentences and their scores
    :param text: input text
    :param frequencies: word occurrence frequencies
    :return: dictionary of sentence/score key-value pairs
    """
    sentences: List[str] = sent_tokenize(text)

    scores: Dict[str, float] = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in frequencies.keys():
                if sentence not in scores.keys():
                    scores[sentence] = frequencies[word]
                else:
                    scores[sentence] += frequencies[word]
    return scores


def get_summary(scores: Dict[str, float], top_sentence_number: int = 7) -> str:
    """
    Get top (default 2) sentences with the highest scores and parse them
    together, returning a string
    :param scores: sentence scores
    :param top_sentence_number: number of sentences with top scores to
    use in the generated summary
    :return: joined string of the sentences with highest scores
    """
    summary_sentences = nlargest(top_sentence_number, scores, key=scores.get)
    return ' '.join(summary_sentences)


def generate_summary_from_url(url: str, length: int) -> str:
    """
    Main method.
    :param url: full URL of the resource we're scraping and generating
    report for
    :param length: number of sentences to use in the final report
    :return: report (string)
    """
    scraped_text: str = scrape_text(url)
    scraped_text, formatted_text = preprocessing(scraped_text)

    weights: Dict[str, float] = weighted_occurrence_frequency(formatted_text)
    scores: Dict[str, float] = compute_sentence_scores(scraped_text, weights)

    return get_summary(scores, length)


# Download stopwords (if they don't exist) and store all stopwords
# defined in the English language
download('stopwords')
stop_words: Any = stopwords.words('english')

# Download 'punkt' resource (if it doesn't exist)
download('punkt')

if len(argv) != 3:
    print('You need to provide two arguments: URL and number of sentences to include in summarization')
else:
    URL = argv[1]
    SENTENCES_IN_REPORT = int(argv[2])
    print(generate_summary_from_url(URL, SENTENCES_IN_REPORT))
