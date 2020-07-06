import requests
import re
from bs4 import BeautifulSoup
c = 32
# https://pinoybix.org/2015/10/practice-quiz-in-data-communications-and-networking.html
response = requests.get(
    'https://pinoybix.org/2020/02/quiz-in-data-communications-and-networking-ece-board-exam.html')
a = response.text
z = re.findall('<div style="border-top: #ffd324 1px solid; border-right: #ffd324 1px solid; background: #fff6bf; border-bottom: #ffd324 1px solid; padding-bottom: 10px; padding-top: 10px; padding-left: 10px; margin: 10px 0px; border-left: #ffd324 1px solid; padding-right: 10px" align="justify">&#160;<strong>(.*)</strong></div>', a)
z = z[:c]
a = z
for z, i in enumerate(a):
    print(f'Chapter {z + 1}')
    for j in i.split('</a>, <a'):
        p = re.findall(
            'title="(.*)" href="(.*)" rel="noopener noreferrer"', j)[0]
        print(p[0].replace('MCQs', 'Quiz').replace('MCQ', 'Quiz'))
        response = requests.get(p[1])
        sdata = response.text
        soup = BeautifulSoup(sdata, features="lxml")
        try:
            mydivs = soup.findAll('div', {"class": "wps-active"})
            sdata = f'''{mydivs[0]}'''
        except:
            mydivs = soup.findAll('div', {"class": "pf-content"})
            sdata = f'''{mydivs[0]}'''
        soup = BeautifulSoup(sdata, features="lxml")
        p = soup.find_all('p')
        for i in p:
            if 'NEXT: MCQ in' not in i.text:
                print(i.text.replace(
                    'Choose the letter of the best answer in each questions.', ''))
