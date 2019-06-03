from bs4 import BeautifulSoup as bs
from textblob import TextBlob as tb
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import requests as req
import os

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import sys,time


class Tamil:
        def __init__(self,frame):
            self.label1 = Label(frame, text='LANGUAGE',fg="#d91e18",bg="#95a5a6")
            self.label1.place(x=100, y=80)
            data=("","English", "arab", "Hindhi", "Japnesh")
            self.cb=Combobox(frame, values=data)
            self.cb.place(x=100, y=120)
            
            btn = Button(frame, text="START",bg="#95a5a6",command=self.box)
            btn.place(x=100,y=160)

        def box(self):
            if self.cb.get() == "English":
                # return print(str(self.cb.get()))
                caller.collection(str(self.cb.get()))

            elif self.cb.get() == "arab":
                print(str(self.cb.get()))
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Hindhi":
                return print(str(self.cb.get()))
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Japnesh":
                return print(str(self.cb.get()))
                caller.collection(str(self.cb.get()))
        
        def Master(self,baseURL):
            url = baseURL
            agent = {
                        "UserAgent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
                    }
            requesting = req.get(
                                    url=url,
                                    headers=agent
                                )
            contManu = requesting.content
            soupObject = bs(contManu, 'html.parser')
            return soupObject

        def dailythanthi(self):
            tNews = 'https://www.dailythanthi.com/'
            resultObject = caller.Master(tNews)
            ls = []   
            for tmp in resultObject.find_all('h4'):
                ls.append(tmp.text.strip()+';')
                
            itm = ls[1:8]
            return itm

        def thehindu(self):
            tNews = 'https://www.thehindu.com/'
            resultObject = caller.Master(tNews)
            headList = []   
            cTag ={
                        "class":"story-card-news"
                  }
            for tmp in resultObject.find_all('div', cTag):
                for tm in tmp.findAll("h2"):
                    headList.append(tm.a.text.strip()+';')

            return headList   

        def usatoday(self):
            tNews = 'https://www.usatoday.com/'
            resultObject = caller.Master(tNews)
            
            headList = []   
            hTag = {
                         "class":"js-asset-link hfwmm-list-link hfwmm-light-list-link hfwmm-tertiary-link"
                   }
            for tmp in resultObject.find_all('a', hTag):
                 headList.append(tmp.span.text.strip()+';')

            return headList      
            
        def ahram(self):
            tNews = 'http://www.ahram.org.eg/'
            resultObject = caller.Master(tNews)
            headList = []   
            hTag = {
                         "id":"divLatestNews"
                   }
            for tmp in resultObject.find_all('div', hTag):
                  for tm in tmp.findAll("a"):
                        headList.append(tm.text.strip()+';')
            return headList

        def japan(self):
            tNews = 'https://www.nikkei.com/'
            resultObject = caller.Master(tNews)
            
            headList = []   
            hTag = {
                         "class":"m-miM09_title"
                   }
            for tmp in resultObject.find_all('h3', hTag):
                 headList.append(tmp.span.text.strip()+';')

            return headList   

        def collection(self,x):
            select = {
                  'tamil': caller.dailythanthi,
                  'Hindhi': caller.thehindu,
                  'English'  : caller.usatoday,
                  'arab' : caller.ahram,
                  'Japnesh': caller.japan
                  }
           
            self.rest = select[x]()
            caller.conVert()
            
        def conVert(self):
            list = self.rest     # original string
            self.sCointain =[]   # converted string
            msource = [] 
            for tmp in list:
                #   print("[+] {}".format(tmp))
                #   messagebox.showinfo("[+] {}".format(tmp))
                  convertion = tb(tmp)
                  self.out = convertion.translate(to='ta')
                #   print("[-] {}\n".format(self.out))
                #   messagebox.showinfo("[-] {}\n".format(self.out))
                  self.sCointain.append(str(self.out))
            
            for tmp, tm in zip(list,self.sCointain):
                msource.append("[+] "+tmp)
                msource.append("[-] "+tm+"\n")


            ans = ' \n'.join(msource)
            messagebox.showinfo("Title",ans)



            self.sCointain
            os.chdir(os.getcwd())
            caller.voice()
            caller.player()
                  
        def voice(self):
            lineString = '\','.join(self.sCointain)
            # print(sam)
            auGen = gTTS(lineString, lang='ta')
            auGen.save('t_news.mp3')
      
        def player(self):
            News = AudioSegment.from_mp3("{}/t_news.mp3".format(os.getcwd()))
            play(News)
      
        def selector(self):
            print("\n\tSELECT YOU ARE LANG!!!")
            print("\n\t\t[+]: India, [+]: Arab [+]: Japan, [+]: USA\n")

            #print("\tCHOOSE USE COMMANT WHILE (VOICE OR TEXT)\n")
#             conValue = input("Enter Value :>> ")
#             caller.collection(conValue)
# caller = Tamil1()
# caller.selector()
frame = Tk()
caller = Tamil(frame)
frame.configure(bg='#95a5a6')
frame.title("CODER!")
frame.geometry("400x300+10+10")
frame.mainloop()