import json
from math import log10
import string
#from parsivar import Normalizer, Tokenizer, FindStems
from hazm import stopwords_list, Normalizer, WordTokenizer
from parsivar import FindStems
from matplotlib import pyplot as plt

stopwords = set(stopwords_list())
my_stemmer = FindStems()
#my_stemmer = Stemmer()
#mytoken = Tokenizer()
mytoken = WordTokenizer()
my_normalizer = Normalizer()
punctuations = string.punctuation
punctuations += ''.join(['،','؛','»','«','؟'])

# dictionary is a list of "term" objects
dictionary = []
#stopwords = set(stopwords_list())
pos_ind = {}

"""class Docterm:        
    def __init__(self, docId, token): 
        self.count = 0 
        self.docId = docId 
        self.token = token 
        self.positions = []
    def insert(self, position): 
        self.count += 1 
        self.positions.append(position) 
        self.positions = sorted(self.positions)  

class term:
    def __init__(self, token):
        self.count = 0
        self.token = token
        self.docTerms = dict()
    def insert(self, docId, Position):
        self.count += 1
        if docId not in self.docTerms.keys(): 
            self.docTerms[docId] = Docterm(docId, self.token) 
        self.docTerms[docId].insert(Position)

def notfound(word, docId, index):
    newTerm = term(word)
    dictionary.append(newTerm)
    newTerm.insert(docId, index)        

def term_add(token_list, docId):
    for index in range(len(token_list)):
        word = token_list[index]
        if word in stopwords:
            continue
        found = False
        if (len(dictionary) == 0):
            notfound(word, docId, index)
            continue
        for term in dictionary:
            if term.token == word:
                found = True
                term.insert(docId, index)
                break
            # we only create a new object of term 
            # when it doesn't exist in dictionary
        if found == False:
            notfound(word, docId, index)
    return    
"""
def findInDictionary(word):
    for term_ in dictionary:
        if term_.token == word:
            return term_.docTerms

def length(e):
    return len(e.keys())

def intersect(doc_0, doc_1):
    results = []
    ind_0 = 0
    ind_1 = 0
    while ind_0 < len(doc_0) and ind_1 < len(doc_1):
        if doc_0[ind_0] == doc_1[ind_1]:
            results.append(doc_0[ind_0])
            ind_0 += 1
            ind_1 += 1
        else:
            if doc_0[ind_0] < doc_1[ind_1]:
                ind_0 += 1
            else:
                ind_1 += 1
    return results            

def showResult(doc_id):
    for news_ in newsList:
        print(doc_id)
        print(news_[doc_id]['title'])
        print(news_[doc_id]['url'])

def merge(list_doc, have_exclamation, have_double_quote):
        #print(merge)
        if type(list_doc) == dict:
            list_doc.sort(key=length)
        score = dict()

        if not have_exclamation and not have_double_quote:
            for i in range(len(list_doc)):
                for doc in list(list_doc[i]):
                    if doc not in score:
                        score[doc] = 1
                    else:
                        score[doc] += 1    
            sort_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)
            show_first_five_records = False
            if len(sort_scores) > 100:
                show_first_five_records = True
            i = 0
            for doc_id in sort_scores:
                #print("rank: ", len(list_doc) - doc_id[1] + 1, "doc:", doc_id[0])
                if (show_first_five_records) and i > 4:
                    break
                print("rank: ", len(list_doc) - doc_id[1] + 1)
                showResult(doc_id[0])
                i += 1
                #print(newsList[int(doc_id[0])]['title'])
                #print(newsList[int(doc_id[0])]['url'])
        else:
            #for i in range(len(list_doc)):
                #print(i)
                #lis = list(list_doc[i])
                #for elem in lis:
                        #print(elem, type(elem))
            if (len(list_doc) < 2):

                show_first_five_records = False
                if len(list_doc[0]) > 100:
                    show_first_five_records = True
                i = 0    
                for result in list_doc[0]:
                    #print(result)
                    if (show_first_five_records) and i > 4:
                        break
                    showResult(result)
                    i += 1
                return
            midsect = intersect(list(list_doc[0]), list(list_doc[1]))
            #for result in midsect:
                #print(result)
            j = 2  
            while j < len(list_doc):
                midsect = intersect(midsect, list(list_doc[j]))       
                j += 1
            show_first_five_records = False
            if len(midsect) > 100:
                show_first_five_records = True
            i = 0    
            for result in midsect:
                #print(result)
                if (show_first_five_records) and i > 4:
                    break
                showResult(result)
                i += 1
                #print(newsList[int(result)]['title'])
                #print(newsList[int(result)]['url'])     

def not_boolean_query(word):
    doc_res_list = []
    """for term_ in dictionary:
        if term_.token == word:
            doctermlist = term_.docTerms.keys()
            for i in range(10):
                if str(i) not in doctermlist:
                   doc_res_list.append(str(i))
            #for i in range(len(doc_res_list)):
                #print(doc_res_list[i])"""
    for i in range(12202):
        if str(i) not in pos_ind[word][1]:
            doc_res_list.append(str(i))
    #for el in doc_res_list:
        #print(el)        
    return doc_res_list    

def double_quote_check(words):
    quote_ind = []
    for index in range(len(words)):
        #print(words[index])
        if words[index] == '"':
            quote_ind.append(index)
    #for i in range(quote_ind):
       #print(quote_ind[i])
    return quote_ind  

def return_correct_order(poition_list0, position_list1, j):
    first_position = []
    for position in poition_list0:
        nex = int(position) + j
        if nex in position_list1:
            first_position.append(position)
    return first_position

def position_intersect(doc_0, doc_1, id):
    results = {}
    ind_0 = 0
    ind_1 = 0
    if (type(doc_0) == dict):
        list_doc_0 = list(doc_0.keys())
    else:
        list_doc_0 = doc_0    
    list_doc_1 = list(doc_1.keys())
    while ind_0 < len(list_doc_0) and ind_1 < len(list_doc_1):
        if list_doc_0[ind_0] == list_doc_1[ind_1]:
            if (type(doc_0) == dict):
                position_list0 = doc_0[list_doc_0[ind_0]]
            else:
                position_list0 = doc_0    
            pos_lists = return_correct_order(position_list0, doc_1[list_doc_1[ind_1]], id)
            if pos_lists is not None:
                results[list_doc_0[ind_0]] = pos_lists
                #results.append(list_doc_0[ind_0])
                #results[]
            ind_0 += 1
            ind_1 += 1
        else:
            if list_doc_0[ind_0] < list_doc_1[ind_1]:
                ind_0 += 1
            else:
                ind_1 += 1
    return results 


def exact_position_finder(listofDocTerms):
    j = 1 
    print('salam')
    doc_ids = []
    positions = {}
    #docterm_0 = listofDocTerms[0]
    #for list_doc in listofDocTerms:
        #print(list_doc)
    # for biword phrases
    """for key in docterm_0.keys():
        positions[key] = []
    for key in docterm_0.keys():
        if key in listofDocTerms[j].keys():
            for pos in docterm_0[key]:
                if int(pos) + 1 in listofDocTerms[j][key]:
                    
                    positions[key].append(pos)
    for i in positions.keys():
        print(positions[i])                
    j = 2
    # for n - 2 remaining words:
    if len(positions) == 0:
        print('پرسمان شما یافت نشد')
        return
    while j < len(listofDocTerms): 
        for key in positions.keys():
            if key in listofDocTerms[j].keys():
                for i in range(len(positions[key])):
                    if int(positions[key][i]) + j not in listofDocTerms[j][key]:
                        positions[key][i] = 12203
                    #else:
                        #positions[key] = pos    
        j += 1    

    for key in positions.keys():
        if len(positions[key]) == 0:
            continue
        for pos in positions[key]:
            if pos != 12203:
                doc_ids.append(key)"""
                        
                    

    #midsect = position_intersect(list(listofDocTerms[0]), list(listofDocTerms[1]))
    midsect = position_intersect(listofDocTerms[0], listofDocTerms[1], 1)
      
    #for i in midsect:
        #print(i)
            #for result in midsect:
                #print(result)
               
    if len(midsect) == 0:
        print('پرسمان شما یافت نشد', j)
        return 
    for key in midsect.keys():
        print("key:", key)
        print("list:", midsect[key])               
    j = 2  
    while j < len(listofDocTerms):
        print('salam')
        #midsect = position_intersect(midsect, list(listofDocTerms[j]))       
        midsect = position_intersect(midsect, listofDocTerms[j], j)
        if len(midsect) == 0:
            print('پرسمان شما یافت نشد', j)
            return 
        for key in midsect.keys():
            print("key:", key)
            print("list:", midsect[key])       

        j += 1
      
    for key in midsect.keys():
        if len(midsect[key]) != 0:
            doc_ids.append(key)    
    return doc_ids 

def phrase_query(q_ind, words):
    print('phrase_query')
    index = 0
    while (index < len(q_ind)):
        if index + 1 < len(q_ind):
            phrase_docs = []
            # first word is words[q_ind[index] + 1]
            # last word is words[q_ind[index + 1] - 1]
            for j in range(q_ind[index] + 1, q_ind[index + 1]):
                #docterm = findInDictionary(words[j])
                try:
                    docterm = pos_ind[words[j]][1]
                except KeyError:
                    print('!پرسمان شما یافت نشد')    
                phrase_docs.append(docterm)
            phrase_ouput = exact_position_finder(phrase_docs)
            """for key_ph in phrase_ouput.keys():
                if len(phrase_ouput[key_ph]) == 0:
                    phrase_ouput.pop(key_ph)       
            for key in phrase_ouput.keys():
                print("key:", key)
                print("list:", phrase_ouput[key]) """
            for i in phrase_ouput:
                print(i)    
            return phrase_ouput    
        index += 2    


def query_process(words):
    have_exclamation = False
    have_d_q = False
    j = 0
    listofDocterms = []
    docterm_ = None
    q_indexes = double_quote_check(words)
    if q_indexes is not None:
        print(q_indexes)
        #for q_index in q_indexes:
            #print(q_index)
        if len(q_indexes) > 0:  
            print('q_index > 0')  
            listofDocterms.append(phrase_query(q_indexes, words))
            have_d_q = True   
    #exc_pos = -1
    if words[0] == "!":
        have_exclamation = True
        docterm_ = not_boolean_query(words[1])
        if len(words) == 2:
            for el in docterm_:
                print(el)
            return      
        listofDocterms.append(docterm_)
        j = 1
        del words[0]
    
    for i in range(j, len(words)):
        if i >= len(words):
            break
        if len(q_indexes) >= 2:
            if i >= q_indexes[0] and i <= q_indexes[1]:
                continue
        if words[i] == '!':
            #exc_pos = i
            have_exclamation = True
            docterm_ = not_boolean_query(words[i + 1])
            del words[i]
        else:    
            #docterm_ = findInDictionary(words[i])
            try:
                docterm_ = list(pos_ind[words[i]][1].keys())
            except KeyError:
                print(words[i], 'پیدا نشد!')   
        if docterm_ is None:
            print('!پرسمان شما یافت نشد')
            return     
        listofDocterms.append(docterm_)

    merge(listofDocterms, have_exclamation, have_d_q)  

"""newsList = []
#inbade = 0
with open('readme.json', 'r') as js_file:
    #js_data = json.load(js_file)
    #print(js_data[str(inbade)]['title'])
    #inbade += 1
    for jsonObj in js_file:
        js_data = json.loads(jsonObj)
        newsList.append(js_data)

for news in newsList:
    x = news.keys()
    for i in x:
        print(i)
        #normalized_title = my_normalizer.normalize(news[i]['title'])
        #print("title: " , my_normalizer.normalize(news[i]['title']))
        normalized_content = my_normalizer.normalize(news[i]['content'])
        #print("content: " , normalized_content)
        words = mytoken.tokenize_words(normalized_content)
        #term_add(words, i)
        #print("tags: " , news[i]['tags'])
        #print("date: " , news[i]['date'])
        #print("url: " , news[i]['url'])
        #print("category: " , news[i]['category'])""" 
"""used for debug positional index construction"""          
"""file_name = 'pos_index.json'
with open(file_name, 'a') as file:
    #term_id = 0
    for word in dictionary:
        #file.write(str(term_id))
        print(word.token)
        file.write(word.token + ": ")
        print(word.count)
        file.write(str(word.count) + "\n")  
        doc_ids = word.docTerms.keys()
        for doc_id in doc_ids:
            print("docid: ", doc_id)
            file.write(str(doc_id) + ":[")
            docterm = word.docTerms.get(doc_id)
            postingList = docterm.positions
            for position in postingList:
                print("position: ", position)
                file.write(str(position) + ",")
            file.write("]\n")
        file.write('\n')
    file.write('\n')    """   
#print(len(dictionary))
#for word in dictionary:
    #print("token:", word.token)
    #print("frequency: ", word.count)
    #doc_ids = word.docTerms.keys()
    #for doc_id in doc_ids:
        #print("docid: ", doc_id)
        #docterm = word.docTerms.get(doc_id)
        #postingList = docterm.positions
        #for position in postingList:
            #print("position: ", position)


def preprocess(words, is_query):
    d = '"'   
    for word in words: 
        #print(word)
        #print(word)
        #word.replace('\u200c', ' ')
        word = my_normalizer.normalize(word)
        if word in stopwords or word in punctuations:
            if is_query:
                if word == '!' or word == d:
                    continue
                """if word == '»' or word == '«':
                    words.remove(word)
                    words.append('"')
                    continue"""    
            words.remove(word)    
        #newword = my_stemmer.convert_to_stem(word)
        newword = my_stemmer.convert_to_stem(word)
        if newword != word and word in words:
            #print(word)
            #print("stem", newword)
            words.remove(word)
            words.append(newword)
        


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
        if (int(i) % 500 == 0 and int(i) / 500 < 5):
            print(len(pos_ind))
            print(number_of_tokens)
        #if int(i) == 2:
            #print(news[i]['content'])
        normalized_content = my_normalizer.normalize(news[i]['content'])
        #if i == 6929:
            #print(normalized_content)
        #print("content: " , normalized_content)
        words = mytoken.tokenize(normalized_content)
        number_of_tokens += len(words)
        preprocess(words, False)
        #term_add(words, i)
        for pos, term_ in enumerate(words):
            if term_ in pos_ind:
                # frequency of term increases by 1
                pos_ind[term_][0] += 1
                if i in pos_ind[term_][1]:
                    pos_ind[term_][1][i].append(pos)
                else:
                    pos_ind[term_][1][i] = [pos]
            else:
                # Initialize the list.
                pos_ind[term_] = []
				# The total frequency is 1.
                pos_ind[term_].append(1)
				# The postings list is initially empty.
                pos_ind[term_].append({})	
				# Add doc ID to postings list.
                pos_ind[term_][1][i] = [pos]

words_ = pos_ind.keys()
word_freq = {}
for word in words_:
            #print(word)
            #print(pos_ind[word][0])
    word_freq[word] = pos_ind[word][0]
sorted_pos = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)   
        # print('freq') 
x = []
y = []
counter = 0
for i in sorted_pos:
    y.append(log10(i[1]))
    x.append(log10(counter + 1))
    #x.insert(counter)
            #print(i[0], i[1])
    counter += 1   
        #print(x)
        #print(y)    
plt.plot(x, y)
plt.show()

# get free text from user as a query
for i in range(100):
    query = input()
    #normalized_query = my_normalizer.normalize(query)
    words = mytoken.tokenize(query)
    print(words)
    preprocess(words, True)
    print(words)
#for word in words:
    #print("word: ", word)
    #print("positional_index", pos_ind[word])
    if len(words) == 1:
    #found = False
        try:
            for doc in pos_ind[words[0]][1].keys():
                showResult(doc) 
        except KeyError:
            print('!پرسمان شما یافت نشد')       
    
    #if found != True:
        #print('!پرسمان شما یافت نشد')
    else:
        query_process(words)
        #double_quote_check(words)
        
#print(words)
"""for term_ in dictionary:
        if words[0] == term_.token:
            found = True
            docs = term_.docTerms.keys()
            for doc in docs:
                print(doc)"""