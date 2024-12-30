import json
from math import sqrt
import math
import string
#from parsivar import Normalizer, Tokenizer, FindStems
from hazm import stopwords_list, Normalizer, WordTokenizer
from parsivar import FindStems
#from matplotlib import pyplot as plt

stopwords = set(stopwords_list())
my_stemmer = FindStems()
#my_stemmer = Stemmer()
#mytoken = Tokenizer()
mytoken = WordTokenizer()
my_normalizer = Normalizer()
punctuations = string.punctuation
punctuations += ''.join(['،','؛','»','«','؟'])

#stopwords = set(stopwords_list())
pos_ind = {}
            

def showResult(doc_id):
    for news_ in newsList:
        print(doc_id)
        print(news_[doc_id]['title'])
        print(news_[doc_id]['url'])

def normalize_doc(doc_id):
        leng = 0.0
        for term in pos_ind.keys():
            if doc_id in pos_ind[term][1]:
                w = pos_ind[term][1][doc_id]['w']
                leng += w * w
                #print(doc_id, term, w, leng)
        return sqrt(leng)     

def query_vector():
        N = 12202 
        Scores = [0.0] * N
    
        query = input().split(" ")
        for word in query:
            if word in pos_ind.keys():
                print(pos_ind[word][0])
                for doc in champion_list(word):
                    Scores[int(doc)] += pos_ind[word][1][doc]['w']  
            else:
                print('کلمه یافت نشد!', word)
                if len(query) == 1:
                    return
            for doc in champion_list(word):
                Scores[int(doc)] /= normalize_doc(doc)         


    #for d in range(len(Length)):
        #Scores[d] /= Length[d]
    #for d in range(len(Length)):
        #print(Scores[d])    
        k = 10
        champions_sc = []
        max_id = 0
        for i in range(k):
            max_score = float('-inf')
            for j in range(N):
                if Scores[j] > max_score and j not in champions_sc:
                    max_score = Scores[j]
                    max_id = j
            champions_sc.append(max_id)
        for doc in champions_sc:
            showResult(str(doc))    
    #return champions_sc                        
    

def preprocess(words, is_query):
    d = '"'   
    for word in words: 
        #print(word)
        #word.replace('\u200c', ' ')
        word = my_normalizer.normalize(word)
        if word in stopwords or word in punctuations:
            if is_query:
                if word == '!' or word == d:
                    continue  
            words.remove(word)    
        #newword = my_stemmer.convert_to_stem(word)
        newword = my_stemmer.convert_to_stem(word)
        if newword != word and word in words:
            #print(word)
            #print("stem", newword)
            words.remove(word)
            words.append(newword)

def champion_list(term):
        k = 10
        #term_ch_list = {}
        max_doc_id = 0
   
    #for term in pos_ind.keys():
        champions = []
        for i in range(k):
            max_weight = float('-inf')
            if (i + 1 > len(pos_ind[term][1].keys())):
                break
            for doc_id in pos_ind[term][1]:
                if pos_ind[term][1][doc_id]['w'] > max_weight and doc_id not in champions:
                    max_doc_id = doc_id
                    max_weight = pos_ind[term][1][doc_id]['w']
            champions.append(max_doc_id)
        #print(term, champions)    
        #term_ch_list[term] = champions
        for i in range(k):
            print(champions[i])
        return champions        


newsList = []
with open('IR_data_news_12k.json', 'r') as js_file:
    for jsonObj in js_file:
        js_data = json.loads(jsonObj)
        newsList.append(js_data)
number_of_tokens = 0
for news in newsList:
    x = news.keys()
    for i in x:
        print(i)
        #if (int(i) % 500 == 0 and int(i) / 500 < 5):
            #print(len(pos_ind))
            #print(number_of_token)
        normalized_content = my_normalizer.normalize(news[i]['content'])
        #if i == 6929:
            #print(normalized_content)
        #print("content: " , normalized_content)
        words = mytoken.tokenize(normalized_content)
        #number_of_tokens += len(words)
        preprocess(words, False)
        for pos, term_ in enumerate(words):
            if term_ in pos_ind:
                # frequency of term increases by 1
                pos_ind[term_][0] += 1
                if i in pos_ind[term_][1].keys():
                    pos_ind[term_][1][i]['pos'].append(pos)
                else:
                    #print(term_, pos_ind[term_][1])
                    pos_ind[term_][1][i] = {}
                    pos_ind[term_][1][i]['pos'] = [pos]
                    pos_ind[term_][1][i]['w'] = 0.0
            else:
                # Initialize the list.
                pos_ind[term_] = []
				# The total frequency is 1.
                pos_ind[term_].append(1)
				# The postings list is initially empty.
                pos_ind[term_].append({})	
                pos_ind[term_][1][i] = {}
				# Add doc ID to postings list.
                pos_ind[term_][1][i]['pos'] = [pos]
                # initial weight for each doc
                pos_ind[term_][1][i]['w'] = 0.0
            #print(term_, pos_ind[term_][1])     


N = 12202
for term in pos_ind.keys():
    #print(pos_ind[term][1])
    list_of_docs = list(pos_ind[term][1].keys())
    idf = math.log10(N / len(list_of_docs))
    for doc in list_of_docs:
        #print(type(pos_ind[term][1][doc]['pos']))
        f_td = len(pos_ind[term][1][doc]['pos'])
        w_td = idf * (1 + math.log10(f_td))
        pos_ind[term][1][doc]['w'] = w_td
    #print(term, pos_ind[term][1])

#champion_list()   
query_vector()  
#list_of_champions = query_vector()


#print(tf)
