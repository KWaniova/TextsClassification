import re, string, unicodedata
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('gutenberg')
nltk.download('averaged_perceptron_tagger')
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import inflect

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    polish_stopwords = open('polish_stopwords.txt', 'r').read().split('\n')
    print(polish_stopwords[:10])
    for word in words:
        if word not in polish_stopwords:
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize list of tokenized words as verbs"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words):
    """
    Normalize words
    """
    words = remove_non_ascii(words)
    words = replace_numbers(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    # words = remove_stopwords(words)
    return words


# Load the Polish tokenizer
sent = nltk.data.load(
    'tokenizers/punkt/polish.pickle'
)

def remove_end_lines(text):
    data = []
    for item in text:
        data.append(item.replace('\n', ' '))
    return data


def tokenize_and_normalize(text):
    """
    Tokenize and normalize text
    """
    sentenses = sent.tokenize(text)
    print(sentenses)
    sentenses = remove_end_lines(sentenses)
    sents = []
    for s in sentenses:
        # print(s)
        words = nltk.word_tokenize(s)
        # print(words)
        words = normalize(words)
        # print(words)
        sents.append(" ".join(words))
    print(sents[:10])
    return sents