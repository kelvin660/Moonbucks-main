from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet


def lemmatize(file_name, output_file):
    with open(file_name, 'r', encoding='utf-8') as f:
        contents = f.read().split(' ')
    lemmatizer = WordNetLemmatizer()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    tag= nltk.pos_tag(contents)
    out = open(output_file, "w")
    for x in tag:
        out.write(lemmatizer.lemmatize(x[0], tag_dict.get(x[1][0].upper(), wordnet.NOUN))+' ')
    f.close()

class Node:
    def __init__(self):
        self.head = {}
        self.category = ""
        self.frequency =0
        self.IsEndOfWord = False

class Trie:
    positive_num = 0
    negative_num=0
    neutral_num=0

    def __init__(self):
        self.root = Node()

    # Input suffix into the trie letter by letter
    def insertWord(self, word, category):
        cur = self.root  # root of trie
        for char in word:
            if char not in cur.head:
                cur.head[char] = Node()   # append new trie node that contains dict to all its branches
            cur = cur.head[char]        # traverse to new node
        cur.category = category   # append the index of char in the txt
        if(category=='neutral'):
            cur.frequency+= 1
        cur.isEndOfWord = True
        # print(cur.category)

    def insert(self, positive, negative):
        with open(positive, 'r', encoding='utf-8') as f:
            contents = f.read().split(' ')
            for x in contents:
                self.insertWord(x,'positive')
        f.close()
        with open(negative, 'r', encoding='utf-8') as f:
            contents = f.read().split(' ')
            for x in contents:
                self.insertWord(x,'negative')
        f.close()

    def search(self, input_file):

        with open(input_file, 'r', encoding="utf-8") as f:
            contents = f.read().split(' ')
            for word in contents:
                cur = self.root
                for char in word:
                    if char not in cur.head:  # not matching
                        break
                    cur = cur.head[char]      # traverse to branch

                if cur.category == 'positive':
                    self.positive_num +=1
                    cur.frequency+=1
                elif cur.category == 'negative':
                    self.negative_num +=1
                    cur.frequency+=1
                elif cur.category == 'neutral':
                    self.neutral_num +=1
                    cur.frequency+=1
                else:
                    self.insertWord(word,'neutral')
                    self.neutral_num +=1

    def sentiment(self,  positive, negative, input_file):
        self.insert(positive,negative)
        self.search(input_file)
        self.fre()
        print("positve frequecny : " + str(self.positive_num))
        print("negative frequecny : "+ str(self.negative_num))
        print("neutral frequency : "+ str(self.neutral_num))

    def fre(self):
        cur = self.root
        for char in 'LOVE':
            if char not in cur.head:  # not matching
                break
            cur = cur.head[char]
        print(cur.frequency)


if __name__ == "__main__":
    # lemmatize("input_file.txt", "lemmatized.txt")
    suffixTrie = Trie()
    suffixTrie.sentiment('positive.txt','negative.txt','lemmatized.txt')