
import requests
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_extract_sentiment(url):
    analyzer = SentimentIntensityAnalyzer()
    frame_shape = ['cat eye','oversized','pilot','round','square','circular','oval']
    lenses = ['gradient','mirrored','tinted']
    color = ['blue','black','brown','green','grey','gold','metallic','multicolour','neutrals','neutrals','orange','pink','purple','red','silver','white','yellow']
    p_list = {}
    for i in frame_shape:
        p_list[i] = 'shape'
    for i in lenses:
        p_list[i] = 'lenses'
    for i in color:
        p_list[i] = 'color'
    property_words = frame_shape + lenses + color
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            'style',]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    datas = output.split('\n')
    phrases = []
    for data in datas:
        for d in data.split('.'):
            if len(d.split(' ')) > 4:
                phrases.append(d)



    sentiment_words = []

    for sentence in phrases:
        vs = analyzer.polarity_scores(sentence)
        for word in sentence.split(' '):
            for p_word in property_words:
                if p_word in word.lower():
                    sentiment_words.append([p_word, vs['compound'],p_list[p_word]])


    return pd.DataFrame(sentiment_words).groupby(0).mean()