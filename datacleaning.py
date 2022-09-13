import requests
from bs4 import BeautifulSoup
import xlrd
import os
import pandas as pd

all_topics = ["https://forum.lowyat.net/topic/2216598","https://forum.lowyat.net/topic/4479325"]
length = [1000,80]
raw_data = {}

os.chdir('/mnt/c/Users/kenne/jupyter/jupyter/')
cwd = os.getcwd()
print(cwd)
os.chdir('/mnt/c/Users/kenne/jupyter/jupyter/IOI_properties/')
cwd = os.getcwd()
print(cwd)

#arrange for key and value
for count in range(0,len(all_topics)):
    name = str(all_topics[count][-7:])+".xlsx"
    print(name)
    df = pd.read_excel(name,engine='openpyxl')
    raw_data[all_topics[count][-7:]] = df

all_data = {}
word_list = []
date_list = []

#format is raw_data[page_id][column][row]
print(raw_data['4479325'][1][0])
for df in raw_data:
    topic_data = {}
    i=0
    while i < (len(raw_data[df])):
        word_list = []
        date_list = []
        for text in range(0,20):
            words = str(raw_data[df][text][i]).replace('@',"").replace('QUOTE',"").split()
            word_list.append(words)
        topic_data[i] = word_list
        i+=1
        for text in range(0,20):
            date = str(raw_data[df][text][i]).replace(',',"")
            date_list.append(date)
        topic_data[i] = date_list
        i+=1
    all_data[df] = topic_data
