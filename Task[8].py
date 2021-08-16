### Task[2] : apply same method on 5 articles, save result in csv file ###
import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

### To Get Headline ###
headlist = []
headline = soup.find_all(class_ = 'entry-title')
for h in range(5):
    headlist.append(headline[h].text)

### To Get Summary ###
summarylist = []
summary = soup.find_all('article')
for s in range(5):
    summarylist.append(summary[s].div.p.text)

### To Get Link ###
linklist = []
youtube = 'https://youtube.com/watch?v='
link = soup.find_all('article')
for i in range(5):
    try:
        link[i] = link[i].div.iframe.attrs['src']
        link[i] = link[i].split('/')[4].split('?')[0]
        link[i] = youtube + link[i]
        linklist.append(link[i])
    except:
        linklist.append('No Link')

with open ('Result.csv', 'w', encoding='utf-8', newline='\n')as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Headline', 'Summary', 'Link']) 
    for i in range(5):
        writer.writerow([headlist[i], summarylist[i], linklist[i]])
    


    

