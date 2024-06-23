from bs4 import BeautifulSoup
import requests
from datetime import date, datetime


def is_between(dateStr, startDateStr, endDateStr):
    date_obj = datetime.strptime(dateStr, '%Y-%m-%d %H:%M:%S').date()
    startDate = datetime.strptime(startDateStr, '%Y-%m-%d %H:%M:%S').date()
    endDate = datetime.strptime(endDateStr, '%Y-%m-%d %H:%M:%S').date()
    if startDate <= date_obj <= endDate:
        return True
    else:
        return False


url = 'https://filecxx.com/ru_RU/activation_code.html'
r = requests.get(url)
with open('index.html', 'w') as output_file:
    output_file.write(r.text)

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

codes = soup.find_all('pre', id='codes')
current_time = date.today()
current_date = current_time.strftime('%Y-%m-%d %H:%M:%S')
target = codes[0].text.split("\n", -1)
i = 0

while i < len(target):
    if target[i] == '':
        del target[i]
    i += 1
if "" in target:
    target.remove("")
i = 0
keys =[]
while i < len(target):
    if i % 2 == 0:
        if target[i] != '':
            dates = target[i].split(" - ", -1)
            if is_between(current_date, dates[0], dates[1]):
                keys.append(target[i+1])
            else:
                pass
    i += 1
print(keys[len(keys)-1])