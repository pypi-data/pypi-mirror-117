from datakund_ai_scraper import *
import json
def read_file(file):
    with open(file+".txt",encoding="utf-8") as d:
        html=d.read()
    return html
html1=read_file("html1")
html2=read_file("html2")
res=scraper.parse(html1,html2)
#res=scraper.run(html1,id="7BMTY1B9RWC665V")
print("res",res)