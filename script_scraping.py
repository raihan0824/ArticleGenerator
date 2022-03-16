import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import string
from urllib.request import urlopen
import pandas as pd
import urllib.request
pd.options.mode.chained_assignment = None 
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import warnings
warnings.filterwarnings('ignore')
import requests

blog_content=[]
blog_title = []
url_articles = 'https://www.efinancialcareers.com/news'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'}
for i in range(1,100): # loop the first 100 web pages.
    url_page = 'https://www.efinancialcareers.com/news?page={}'.format(i)
    response_1 = requests.get(url_page,headers=headers)
    htmls = BeautifulSoup(response_1.content, 'html.parser').findAll(lambda t: t.name == 'a' and not t.find('img'),href=re.compile('^/news/.+'))
    links = []
    for html in htmls: # loop all the post's link
        links.append(url_articles+html.get('href'))
    for link in links: 
        response_2 = requests.get(link,headers=headers)
        soup = BeautifulSoup(response_2.content,'html.parser')
        html_post = soup.findAll('p',class_=None,a_=False,href = None)
        blog_title.append(soup.findAll(class_='article-title')[0].text) # Get blog's title
        post_breakpoint = next((p.find('a').text for p in soup.findAll('strong') if p.find('a') is not None),None) # Add the breakpoint to avoid the text that's not the article
        if post_breakpoint is not None:
            try:
                index = [idx for idx, s in enumerate([p.text for p in html_post]) if post_breakpoint in s][0] # get the index of the first word that's not the article
                blog_content.append(''.join([p.text for p in html_post][0:index]).replace('\xa0',' '))  # only append blog_content with the article
            except IndexError:
                blog_content.append(''.join([p.text for p in html_post]).replace('\xa0',' ')) 
        else:
            blog_content.append(''.join([p.text for p in html_post]).replace('\xa0',' '))
            
pd.DataFrame(list(zip(blog_title,blog_content)),columns=['Title','Content']).to_csv('/Users/raihanafiandi/Documents/Upwork/df.csv') #save the scraped data to dataframe
