import requests
import lxml
from bs4 import BeautifulSoup as bs
import pdfkit
import os
from time import sleep
import sys
class Finder():
    def res_domain(self):
        try:
            self.lang = sys.argv[1]
        except IndexError:
            print("-> Enter an Argument!!!")
            sys.exit(0)
        urls = "https://www.tutorialspoint.com/{}".format(self.lang)
        # print(urls)
        agnt = {"User-Agent":"Mozilla/6.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
        res = requests.get(url=urls,headers=agnt)
        self.cont = res.content
    def res_soup(self):
        obj.res_domain()
        sp_object = bs(self.cont,"lxml")        
        sp_find = sp_object.find_all("ul", {"class": "nav nav-list primary left-menu"})

        self.box =[]
        for tm in sp_find:
            s=tm.findAll("a")
            
            for tmp in s:
                link=tmp["href"]
                if ".htm" in link:
                    linkers = link
                    url = "https://www.tutorialspoint.com"
                   
                    ls = str(url+linkers)
                    self.box.append(ls)
                    
    # def res_print(self):
    #     print(len(self.box))
    #     # print(self.box)

    def res_downloader(self):
        self.page_name = str("{}/{}.html".format(os.getcwd(),self.lang))
        for tm in self.box:
            #print(tm)
            agent = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
            req = requests.get(url=tm,headers=agent)   
            bss = bs(req.content, "lxml")
            for ts in bss.find_all("script"):ts.decompose()
            for tmp in  bss.find_all("a"):tmp.decompose()
            for tm in bss.find_all("hr"):tm.decompose()
            assider = bss.find("aside", {"class": "sidebar"})
            liadv = bss.find("div", {"class":"simple-ad"})
            bfooter = bss.find("div", {"class":"footer-copyright"})
            adv = bss.find("div",{"class": "bottomadtag"})
            adver = bss.find("div",{"class":"col-md-7 middle-col"})
            headerr = bss.header
            metool = bss.find("div",{"class":"center-aligned tutorial-menu"})
            try:
                ad_h = adver.findNext("h1")
                ad_c = ad_h.findNext("div")
                ad_c.decompose()
                bfooter.decompose()
                assider.decompose()
                headerr.decompose()
                liadv.decompose()
                adv.decompose()
                metool.decompose()
                
            except AttributeError:None


            with open(self.page_name, "a")as f:
                f.write(str(bss.get_text))
        print("__Almost__")
        pdfkit.from_file(self.page_name,"{}.pdf".format(self.lang))
        try:
            os.remove(self.page_name)
        except Expection:None
        print("__Done__")
obj=Finder()

obj.res_soup()
#obj.res_print()
obj.res_downloader()
