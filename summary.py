from bs4 import BeautifulSoup
from newspaper import Article
def summarize(url):
    
    import requests

    looking_head = requests.get(url)
    soup = BeautifulSoup(looking_head.text, features='lxml')
    # print(soup)
    article_header = soup.find('h1')
    article_header = article_header.text
    article = Article(url)

    article.download()
    article.parse()
    article = article.text
    #print(type(article.text))
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
    from sumy.nlp.stemmers import Stemmer


    LANGUAGE = "english"
    SENTENCES_COUNT = 10

    parser = PlaintextParser.from_string(article, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    paras = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        #print(sentence)
        paras.append(sentence)

    #print(paras[0])
    myText = open(f'{article_header}.txt','w')
    myText.write(f'{article_header}'+ '\n'+'\n')
    # myString = 'Type your string here'
    for para in paras:
        
        myText.write(str(para)+ '\n'+'\n')
    myText.close()
summarize(url = "https://en.citizendium.org/wiki/Iraq_War")