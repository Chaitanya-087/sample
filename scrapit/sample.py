import requests
from bs4 import BeautifulSoup

class amazonscrap:
    url = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=1"
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    def parse(self):
        res = requests.get(self.url,headers = self.headers)
        soup = BeautifulSoup(res.content,"lxml")
        return soup
    def findtitle(self):
        tink = self.parse()
        print(tink.find("span",class_="zg-banner-text").get_text().strip())
    def booknames(self):
        pass

bot = amazonscrap()
bot.findtitle()