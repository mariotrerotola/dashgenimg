from duckduckgo_search import ddg
from extract_text import get_extract_sentiment
import pandas as pd
from multiprocessing import Pool


def sent_link(lk):
    if 'sunglasshut' not in lk:
        try:
            get_extract_sentiment(lk).to_csv('data.csv', mode='a', header=False)
        except: 
            pass

if __name__ == '__main__':
    for i in range(1,10):
        ress = ddg('"glasses" "2023"', page = i)
        print(ress)
        links = [res['href'] for res in ress]
        print(links)
        with Pool(len(links)) as p:
            p.map(sent_link, links)
