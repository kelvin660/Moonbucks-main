import os
from itertools import chain
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from dumpstorage import Store as st  # save object as persistent storage


class Trie:

    def __init__(self):
        self.head = {}

        # Insert the word into the trie
    def insert(self, word):
        cur = self  # root of trie
        for char in word:
            if char not in cur.head:
                cur.head[char] = Trie() # append new trie node that contains dict to all its branches
            cur = cur.head[char]        # traverse to new node
        cur.head['*'] = True

    def search(self, pattern):
        cur = self
        for char in pattern:
            if char not in cur.head:  # not matching
                # print("\"{}\" pattern is not found".format(pattern))
                return False
            cur = cur.head[char]      # traverse to branch
        if '*' in cur.head:
            # print(pattern, "Pattern found")
            return True

    def insertAll(self, words):
        for i in words:
            self.insert(i)

def getPositiveWords():
    url = 'https://positivewordsresearch.com/list-of-positive-words/'
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    division = soup.find("div", class_ = 'entry-content')
    paras = list(division.find_all('p'))[3:-2]

    pos_words = [para.text.lower().replace('\xa0', '').split(', ') for para in paras]
    pos_words = list(chain.from_iterable(pos_words))
    pos_words = [word.strip() for word in pos_words]
    return pos_words

def getNegativeWords():
    url = 'https://positivewordsresearch.com/list-of-negative-words/'
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    division = soup.find("div", class_ = 'entry-content') 
    paras = list(division.find_all('p'))[1:-1]

    neg_words = [para.text.lower().replace('\xa0', '').split(', ') for para in paras]
    neg_words = list(chain.from_iterable(neg_words))
    neg_words = [word.strip() for word in neg_words]
    return neg_words

# File must be formatted, without "\n" in them
# Returns a list of strings (containing ' and ,)
def readFile(file_name):
    with open(os.path.join("articles", file_name), 'r') as f:
        content = f.read() # This reads the contents from the file as a string and tokenizes it
    return content

# Takes in a list of strings(words) and return lemmatized version of them
def lemmatize(text):
    lemma_func = WordNetLemmatizer()

    # Pair each word with its respective POS tag
    # Contains map object ('WORD', 'TAG')
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(text)) 
    
    # Removes punctuations 
    nltk_tagged_no_punc = [w for w in nltk_tagged if w[0].isalnum()]
    
    # Function to clasify the tokenized, tagged part of speech tag method of NLTK (nltk.pos_tag)
    # x[0] = WORD
    # x[1] = POS_TAG
    func = lambda x: (x[0], nltk_pos_tagger(x[1]))
    
    # Apply the lambda function to all elements in 'nltk_tagged'
    # Contains map object ('WORD', 'N')
    wordnet_tagged = map(func, nltk_tagged_no_punc)
    lemmatized_sentence = []

    # Removes stop words
    stop_words_eng = set(sw.words('english'))

    for word, tag in wordnet_tagged:
        if not word.lower() in stop_words_eng:
            if tag is None:
                lemmatized_sentence.append(word.lower())
            else:
                lemmatized_sentence.append(lemma_func.lemmatize(word.lower(), tag))
    
    '''
        == FORMAT FOR return_list ==
            len(return_list) = 3
            return_list[0] -> Number of words 
            return_list[1] -> Number of words (without stop words)
            return_list[2] -> Lemmatised text
    '''

    return_list = []
    return_list.append(len(nltk_tagged_no_punc))
    return_list.append(len(lemmatized_sentence))
    return_list.append(lemmatized_sentence)

    return return_list

# Helper method that uses POS tagger as the callback function
# Eg: 'V'BN -> V
def nltk_pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wn.ADJ
    elif nltk_tag.startswith('V'):
        return wn.VERB
    elif nltk_tag.startswith('N'):
        return wn.NOUN
    elif nltk_tag.startswith('R'):
        return wn.ADV
    else:          
        return None

def countSentiment(pos_trie, neg_trie, file_name):
    # Read file
    txt = readFile(file_name)

    #Lemmiatize file: a list
    from_lemmatize = lemmatize(txt)
    lemma_txt = from_lemmatize[2] # Lemmatized sentence
    sentiment = 0
    pos_words = []
    neg_words = []
    
    return_list = [] # Used for plotting graph

    # Search for the word in both positive and negative trie
    for w in lemma_txt:
        if pos_trie.search(w):
            sentiment += 1
            pos_words.append(w)
        elif neg_trie.search(w):
            sentiment -= 1
            neg_words.append(w)
    
    '''
        == Format of return_list ==
            len(return_list) = 7
            return_list[0] -> Number of words
            return_list[1] -> Number of positive words
            return_list[2] -> Number of negative words
            return_list[3] -> List of positive words
            return_list[4] -> List of negative words
            return_list[5] -> Sentiment score
            return_list[6] -> Number of words (without stop words)
    '''

    return_list.append(from_lemmatize[0])
    return_list.append(len(pos_words))
    return_list.append(len(neg_words))
    return_list.append(pos_words)
    return_list.append(neg_words)
    return_list.append(sentiment)
    return_list.append(from_lemmatize[1])

    return return_list


if __name__ == "__main__":
    # Use this code to load the tries tree into an object
    pos_trie = st.load("positiveTrieobj")
    neg_trie = st.load("negativeTrieobj")
    
    country_code = ["de", "gb", "jp", "nz", "sg"]
    num = [1, 2, 3, 4, 5]
    # <countrycode>-<number>.txt
    article_path = [x + "-" + str(y) + ".txt" for x in country_code for y in num]
    
    combined = [countSentiment(pos_trie, neg_trie, article) for article in article_path]
    print(combined)
    
    # for article in article_path:
    #     print("Article", article)
    #     var = countSentiment(pos_trie, neg_trie, article)
    #     print(var)

