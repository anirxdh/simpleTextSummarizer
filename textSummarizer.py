import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from string import punctuation
from nltk.stem.lancaster import LancasterStemmer
from bs4 import BeautifulSoup
import urllib.request
import operator

link = None
number = 0

def summariser(link, number):
   

    print("\nEnter Required Fields:\n")
    link = input("Enter URL: ")
    number = int(input("Enter number of sentences: "))
  
    custom = set(stopwords.words('english')+list(punctuation)+["\xa0","'","...","..","''","``","-","--",])	

    req = urllib.request.Request(link)
    response = urllib.request.urlopen(req)
    page = response.read()	
    
    soup = BeautifulSoup(page, 'lxml')
    paras = ' '.join([p.text for p in soup.findAll('p')])	

    #tokenisation 
    paras_sent = sent_tokenize(paras)
    paras_words = word_tokenize(paras)
    #stopword removal
    words = [word for word in paras_words if word not in custom]
    words = [word.lower() for word in words]
    counts = Counter(words)
    counts = counts.most_common()
	
    
    final_words_we_need = [x for x in counts if x[1]>3]
    final_words_we_need	

    d = {}
    for s in paras_sent:
        score = 0
        for w in final_words_we_need:
            if w[0] in s:
                score = score + w[1]
        d[s] = score	
	

    score_d = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
    score_d	

    our_summary = []
    for x in score_d[:3]:
        our_summary.append(x[0])	

    our_summary = ' '.join(our_summary[:])
    return(print("\n", our_summary))

summariser(link, number)

#https://www.thehindu.com/sport/athletics/asian-games-neeraj-chopra-is-first-indian-to-win-javelin-throw-gold/article24793285.ece
#https://www.ndtv.com/india-news/top-court-seeks-centre-whatsapps-reply-over-appointment-of-grievance-officer-1907068
