from urllib.request import urlopen
from bs4 import BeautifulSoup as bss
from gtts import gTTS
import os, platform,lxml

def thanthi():
    url = 'https://www.dailythanthi.com/'
    requesting = urlopen(url).read()
    soup = bss(requesting, 'lxml')
    hline = 'வணக்கம் செய்திகள் வசிப்பது உங்கள் பைதான்;'
    ls = []
    banner ='''
  _____ _                 _   _     _   _   _                   
 |_   _| |__   __ _ _ __ | |_| |__ (_) | \ | | _____      _____ 
   | | | '_ \ / _` | '_ \| __| '_ \| | |  \| |/ _ \ \ /\ / / __|
   | | | | | | (_| | | | | |_| | | | | | |\  |  __/\ V  V /\__ \\
   |_| |_| |_|\__,_|_| |_|\__|_| |_|_| |_| \_|\___| \_/\_/ |___/
                                                                
'''
    for tmp in soup.find_all('h4'):
        ls.append(tmp.text.strip()+';')

    items = ls[1:8]
    nline = '\n\n'
    one = '\n'
    des = '='*120
    under = '='*18
    tab = '\t'*8
    creat = 'Created by: நரேன் '
    print(nline,banner,one,tab,creat,one,tab,under)

    for val in items:
        print('\n',"{} {}".format('[+]', val))
       
    if platform.system() == 'Linux':
        changer = os.chdir('/home')
        present_user = os.environ['USER']
        again = os.chdir("{}{}".format(present_user,"/Desktop"))

    elif platfom.system() == "Windows":
        os.chdir("e:")
          
    sam = ','.join(items)
    spk = gTTS(hline+sam, lang='ta')
    spk.save('tamil_news.mp3')
    print(nline,"\t","!-AUDIO_Created_ON(Location) : > ",'[ {} ]'.format(os.getcwd()))
thanthi()
