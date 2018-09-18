from urllib.request import urlopen
from bs4 import BeautifulSoup as bss
from gtts import gTTS
import os

url = 'https://www.dailythanthi.com/'


req = urlopen(url).read()

soup = bss(req, 'lxml')
ls = []

for tmp in soup.find_all('h4'):
    ls.append(tmp.text.strip())


pp = ls[1:8]
nline = '\n\n'
des = '='*50
print(nline,des,'TAMIL_NEWS',des)
for val in pp:
    print('\n')
    print("{} {}".format('[*]', val))

os.chdir('E:')

sam = ','.join(pp)

spk = gTTS(sam, lang='ta')
spk.save('tamil_news.mp3')
