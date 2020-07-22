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

""" 키워드 설정하기 """
driver = webdriver.Chrome("./chromedriver") #크롬드라이버 경로 지정
keyword = ""
accurate = ["\"ㅎㅎ\"", "\"자주\""]
mustin = ["%2B미니빔", " %2B지원받아"] #첫번째 원소만 건드리기
exceptf = [" -원고료", " -체험단"] #첫번째 원소만 건드리기
searchfor = keyword+"+"+mustin[0]+mustin[1]
# +mustin[1]
driver.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&query="+searchfor)

# 저장할 csv 파일 설정하기 
with open(searchfor+".csv",  "w", encoding='utf-8', newline='') as csv_fp:
    writer = csv.DictWriter(csv_fp, fieldnames = ["num", "content", "img", "sticker", "video", "tags", "widget", "isad"])
    writer.writeheader()

# set the max number of pages
page_num = 30

i=3
while i <= page_num:
    print("=======",i,"페이지","=======")
    bloglinklist = driver.find_elements_by_css_selector("li.sh_blog_top dt a")
    k=1
    for j in bloglinklist:
        print("--------",k,"--------")
        link=j.get_attribute('href')
        print("href :",link)
        foldername = str(i) + "_" +str(k)  # 각 폴더의 이름
        filename=str(k)+'.txt'
        k+=1
        download_naver_blog.run(link, filename, searchfor, foldername)
    i+=1
    driver.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&query="+searchfor+"&start="+str(10*i-9))

driver.close()