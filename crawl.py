# 네이버 블로그 크롤링
import parser
import csv

import requests # HTTP �묒냽
from bs4 import BeautifulSoup  # �뱁럹�댁� �뚯떛
from selenium import webdriver
import requests
import time
import parsing_blog
from parsing_blog import Parser
import download_naver_blog


""" 키워드 설정하기 """ 
# download_naver_blog.py 에서 
# isad 값을 설정해주세요 !

driver = webdriver.Chrome("./chromedriver/chromedriver")

#네이버 블로그 접속
keyword = "치즈케이크"

# 키워드 설정하기 ( 각 단어를 띄워쓰기 !! )
#정확하게 일치하는 단어
## " "
accurate = ["\"정확\"", "\"자주\""]

#반드시 포함 
## %2B
mustin = ["%2B냠냠", "%2B포함"]

#제외 
## -
exceptf = [" -광고", " -빼고"]

searchfor = keyword+"+"+mustin[0]+exceptf[0]

# 저장할 csv 파일 설정하기 
with open(searchfor+".csv",  "w", encoding='utf-8', newline='') as csv_fp:
    writer = csv.DictWriter(csv_fp, fieldnames = ["num", "content", "img", "sticker", "video", "tags", "widget", "isad"])
    writer.writeheader()

# set the max number of pages 
page_num = 100

for i in range(1, page_num, 10) : 
    driver.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&query="+searchfor+"&start="+str(i))

    bloglinklist = driver.find_elements_by_css_selector("li.sh_blog_top dt a")
    k=1
    for i in bloglinklist:
        link=i.get_attribute('href')
        filename=str(k)+'.txt'
        k+=1
        download_naver_blog.run(link, filename, searchfor) #download_naver_blog �덉쓽 run �⑥닔 �ъ슜!


driver.close()