import json
import re
from bs4 import BeautifulSoup
import urllib.request

with open('questions.json', 'r') as f:
    json_data = f.read()
    json_data = json_data.replace("\\\\'", "'")
    json_data=json_data.replace('\t', ' ')

# print (json_data[3386380:3386388])

data = json.loads(json_data)



print (data[0])

print (data[0]['questionURL'])
with open('out.json', 'w') as outfile:
    outfile.write('[')

first=0
count=0

for jsonobj in data:
    k=0
    url=jsonobj['questionURL']
    page = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    try:
        html= urllib.request.urlopen( page )
        soup = BeautifulSoup(html)
        s=soup("div", {"class":"question-answer"})

        for foo in soup.find_all('div', {'class': 'question-answer'}):
            bar = foo.find('span', {'class': 'date_posted_fmt'})
            date=bar.text
            i=date.index('\'')
            j=date.rfind('\'')

            # print(date[i+1:j])
            jsonobj['questionPostDate']=date[i+1:j]
            count+=1
            if(count % 100 == 0):
                print(count, " done")

            # print (count)
            # print (jsonobj)

            # with open('out.json', 'a') as outfile:
            #     if first != 0:
            #         outfile.write(' , ')
            #     json.dump(jsonobj, outfile)
            #     first+=1

    except Exception:
        print (Exception)
        continue


with open('out.json', 'w') as outfile:
    json.dump(data, outfile)