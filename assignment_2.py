donald_list = [ 'Political appointments by Donald Trump', 'Political positions of Donald Trump', 'Foreign policy of the Donald Trump administration', 'Donald Trump', 'Presidency of Donald Trump']
donald_url_list = ['https://en.wikipedia.org/wiki/Political_appointments_by_Donald_Trump', 'https://en.wikipedia.org/wiki/Political_positions_of_Donald_Trump', 'https://en.wikipedia.org/wiki/Foreign_policy_of_the_Donald_Trump_administration', 'https://en.wikipedia.org/wiki/Donald_Trump', 'https://en.wikipedia.org/wiki/Presidency_of_Donald_Trump']
donald_word_list = ['bad', 'dumb', 'stupid', 'denied', 'apprehend', 'contradicted']
donald_word_list_2 = ['good', 'successful', 'accomplished', 'amazing', 'impeccable', 'positive' ]

from mediawiki import MediaWiki

import bs4
import sys
import requests
import nltk
# nltk.download() I already downloaded this 

def print_analysis_of_wiki_article():
    """ 
    For each article, this code converts the articles to text files, performs a sentiment analysis, and checks to see if certain positive and negative words are present in the articles and displays their frequencies if they are present
    """
    for i in range(len(donald_list)):
        current = donald_list[i]
        wikipedia = MediaWiki()
        wikiarticle = wikipedia.page(current)
        print(wikiarticle.title)
        # print(wikiarticle.content)
        url = donald_url_list[i]
        res = requests.get(url)
        res.raise_for_status()
        wiki = bs4.BeautifulSoup(res.text,"html.parser")
        file_to_write = open(url.split('/')[-1]+".txt", "a")  # append mode
        for i in wiki.select('p'):
            text_to_write = i.getText().encode('utf-8') 
            file_to_write.write(str(text_to_write))

        file_to_write.close()
        from nltk.sentiment.vader import SentimentIntensityAnalyzer

        sentence = wikiarticle.content
        score = SentimentIntensityAnalyzer().polarity_scores(sentence)
        print(score)
        
        f = open(f'{file_to_write.name}')  
        for line in f:
            word = (line.strip()).split()          
            unwanted_chars = ".,-_ "
            wordfreq = {}
            for raw_word in word:
                word = raw_word.strip(unwanted_chars)
                if word not in wordfreq:
                    wordfreq[word] = 0 
                wordfreq[word] += 1
        for word in donald_word_list:
            if word in wordfreq:
                print(word, wordfreq[word])
        for word in donald_word_list_2:
            if word in wordfreq:
                print(word, wordfreq[word])
    
    
print_analysis_of_wiki_article()