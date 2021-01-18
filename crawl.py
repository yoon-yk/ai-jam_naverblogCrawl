# 네이버 블로그 크롤링
import parser
import csv

import requests  # HTTP �묒냽
from bs4 import BeautifulSoup as bs  # �뱁럹�댁� �뚯떛
from selenium import webdriver
import requests
import time


import parsing_blog
from parsing_blog import Parser
import download_naver_blog


""" 키워드 설정하기 """
driver = webdriver.Chrome("./chromedriver/chromedriver")

# 네이버 블로그 접속
keyword = "코알라"

# 키워드 설정하기 ( 각 단어를 띄워쓰기 !! )
# 정확하게 일치하는 단어
## " "
accurate = ['"정확"', '"자주"']

# 반드시 포함
# %2B
mustin = ["%2B냠냠", "%2B포함"]

# 제외
# -
exceptf = [" -광고", " -빼고"]

searchfor = keyword + "+" + mustin[0] + exceptf[0]

driver.get(
    "https://search.naver.com/search.naver?where=post&sm=tab_jum&query=" + searchfor
)


"""
媛� 寃뚯떆臾� 而⑦뀒�대꼫 : li.sh_blog_top
寃뚯떆臾� �쒕ぉ �댁쓽 留곹겕 : li.sh_blog_top dt a �대��� href �띿꽦
寃뚯떆臾� �띿뒪�� : div.se-module.se-module-text p span <- 臾몄옣�⑥쐞濡� �쒓렇媛� �щ젮�덉쓬
�댁떆�쒓렇 : span.ell
怨듦컧 �� : em.u_cnt._count
"""
with open("summary.csv", "w", encoding="utf-8", newline="") as csv_fp:
    writer = csv.DictWriter(
        csv_fp, fieldnames=["num", "content", "img", "sticker", "like", "tags"]
    )
    writer.writeheader()

bloglinklist = driver.find_elements_by_css_selector("li.sh_blog_top dt a")

k = 1

for i in bloglinklist:
    link = i.get_attribute("href")
    path = link[-12:]

    filename = str(k) + ".txt"
    k += 1
    # download_naver_blog �덉쓽 run �⑥닔 �ъ슜!
    download_naver_blog.run(link, filename)

    # get link

    driver.get(link)
    driver.switch_to_default_content  # 상위 프레임으로 전환
    driver.switch_to.frame("mainFrame")  # cafe_main 프레임으로 전환

    html = driver.page_source  # 현재 페이지의 주소를 반환
    soup = bs(html, "html.parser")

    # open csv file

    with open("out/" + path + "/" + filename, "r") as txtfile, open(
        "summary.csv", "a", encoding="utf-8"
    ) as csvfileout:
        parser = Parser(path, True)
        line = txtfile.read().replace("\n", " ")
        imgCnt = parser.imgCount()
        stiCnt = parser.stickerCnt()

        # fp_full = open(path + '/' + 'full_' + file_name,  "r", encoding='utf-8')
        # # 공감수를 fp_full에서 찾으려고 했는데 제거됐다 ...????
        # # likeCnt = ''
        # # result = re.findall('<em class="u_cnt _count">(.*)</em>', fp_full)
        # # likeCnt += result[0]
        # likeCnt = "hh"

        # # 전체 글 수
        # allPost = "zz"
        # # postUrl = html.select_one("li.allview a").attrs["href"]

        # 태그
        strtag = ""
        tags = soup.find_all("span", class_="ell")
        for tag in tags:
            tag = tag.text
            strtag += tag

        # 공감
        strheart = ""
        heart = soup.find_all("em", class_="u_cnt _count")
        for hrt in heart:
            hrt = hrt.text
            strheart += hrt

        # fp_full.close()

        writer = csv.DictWriter(
            csvfileout, fieldnames=["num", "content", "img", "sticker", "like", "tags"]
        )
        writer.writerow(
            {
                "num": filename.rstrip(".txt"),
                "content": line,
                "img": imgCnt,
                "sticker": stiCnt,
                "like": strheart,
                "tags": strtag,
            }
        )
