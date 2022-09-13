import requests
from bs4 import BeautifulSoup
import xlsxwriter

all_topics = ["https://forum.lowyat.net/topic/2216598","https://forum.lowyat.net/topic/4479325"]
length = [1000,80]
website_data = {}
print(all_topics[0])

for count in range(0,len(all_topics)):
    pages = ['']
    for num in range(0,1200):
        if (num <= length[count]) and (num % 20 == 0):
            pages.append(num)
    topic_content = {}
    for page in pages:
        url = all_topics[count] + '/+' + str(page)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find('div', attrs = {'id':'topic_content'})
        texts = []
        dates = []

        for row in table.findAll('div', attrs = {'class':'postcolor post_text'}):
            texts.append(row.text)
        for row in table.find_all(attrs = {'style':'float: left;'}):
            try:
                date = row.find('span', attrs = {'class':'postdetails'})
                dates.append(date.text[:13].strip())
            except:
                continue
        topic_content[url[-3:]] = (texts, dates)
    website_data[all_topics[count][-7:]] = topic_content

#change file name after, in case of overwrites
with xlsxwriter.Workbook('test.xlsx') as workbook:  #generate file test.xlsx
    worksheet = workbook.add_worksheet()

#change depending on which page you wanna data scrape
    worksheet.write_row(0, 0, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    row_num = 1
    for data in website_data['2216598']:
        #raw_data['2216598'][data].fillna('', inplace=True)
        print(row_num)
        #change to acccount for the tuple(text,date) instead of just text
        print(website_data['2216598'][data][0])
        worksheet.write_row(row_num, 0, website_data['2216598'][data][0])
        row_num+=1
        worksheet.write_row(row_num, 0, website_data['2216598'][data][1])
        row_num+=1
workbook.close()
