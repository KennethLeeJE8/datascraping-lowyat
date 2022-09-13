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
for r,_,fs in os.walk("../IOI_properties/"):
    for f in fs:
        print(f)
        if f.endswith('.txt'):
            with open(os.path.join(r,f), 'r') as txt_file:
                #file1 = open(txt_file, 'r')
                lines = txt_file.readlines()
                # Strips the newline character
                words = []
                for line in lines:
                    words.append(line.strip())
                keywords[f[:-4]] = words
#key: document name
#value: list of dictionaries, where key is word and value is count
keyword_count = {}

#key:document name
#value: dictionary of lists, where key is word and value is list of comments
keyword_comments = {}
keyword_dates = {}

for doc_name in keywords:
    keyword_count[doc_name] = {}
    for keyword in keywords[doc_name]:
        #word_list.append({keywords[doc_name][count]:0})
        keyword_count[doc_name][keyword] = 0
print(keyword_count['properties']['ioi properties'])

for doc_name in keywords:
    keyword_comments[doc_name] = {}
    for keyword in keywords[doc_name]:
        keyword_comments[doc_name][keyword] = []

for doc_name in keywords:
    keyword_dates[doc_name] = {}
    for keyword in keywords[doc_name]:
        keyword_dates[doc_name][keyword] = ""

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

for topic_key in all_data:
    for i in range(0,len(all_data[topic_key])):
        for j in range(0,len(all_data[topic_key][i])):
            comment = " ".join(all_data[topic_key][i][j])
            for doc_name in keywords:
                for keyword in keywords[doc_name]:
                    #try to account for two word phrases in the search
                    #if comment.lower().find(keyword) != -1:
                    if contains_word(comment.lower(), keyword):
                        keyword_count[doc_name][keyword] +=1
                        url = "https://forum.lowyat.net/topic/"+topic_key+"/+"+str(i*20)
                        keyword_comments[doc_name][keyword].append([url,comment])

import xlsxwriter
page = {}

for doc_name in keywords:
    page[doc_name] = {}
    for keyword in keywords[doc_name]:
        page[doc_name][keyword] = True

for doc_name in keyword_comments:
    file_name = str(doc_name) + '.xlsx'
    if not os.path.exists(file_name):
        with xlsxwriter.Workbook(file_name) as workbook:
            worksheet = workbook.add_worksheet(name='word counter')
            for row_num, keyword in enumerate(keyword_count[doc_name]):
                output = [keyword, str(keyword_count[doc_name][keyword])]
                if keyword_count[doc_name][keyword] == 0:
                    page[doc_name][keyword] = False
                else:
                    worksheet.write_row(row_num, 0, output)
            for keyword in keyword_comments[doc_name]:
                if page[doc_name][keyword] == True:
                    worksheet = workbook.add_worksheet(name=keyword)
                    for row_num, comment in enumerate(keyword_comments[doc_name][keyword]):
                        worksheet.write_row(row_num, 0, comment)
print('Done')
