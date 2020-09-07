# -*- coding: utf-8 -*- 

""" 
Reference code
https://github.com/chandong83/download-naver-blog
"""

import sys
import csv
import re
import requests
from bs4 import BeautifulSoup


from parsing_blog import Parser
import utils

out_path = 'out'
folder_path = ''

# determine if dataset is ad or not
# ( 검색어 설정에 따라 값을 바꿔주세요 )
isad = 1

# Crawling
def crawler(blog_url, path, file_name, csvname):
    parser = Parser(path, True)
    try:   
        soup = BeautifulSoup(requests.get(blog_url).text, 'lxml') 
       
        # full code 
        with open(path + '/' + 'full_' + file_name,  "w", encoding='utf-8') as fp_full:
            fp_full.write(str(soup))

        # extract text
        with open(path + '/' + file_name,  "w", encoding='utf-8') as fp:
            txt = ''

            # 일반 네이버 블로그(아마 스마트에디터) :se_component, se-component 관련 태그가 존재
            if 'se_component' in str(soup):
                for sub_content in soup.select('div.se_component'):
                    txt += parser.parsing(sub_content)
            else:
                for sub_content in soup.select('div.se-component'):
                    txt += parser.parsing(sub_content)

            # 외부 블로그, 과거 네이버 블로그에는 둘 다 없음
            # 외부 블로그는 포기하더라도 과거 네이버 블로그까지는 규칙이 있지 않을까
            ###
            # if not txt: #여전히 txt가 비어있으면
            #     for sub_content in soup.select('div#postViewArea p'):
            #         txt += parser.parsing(sub_content)
            ###
            fp.write(txt)    

        # add data to csv # open~~as txtfile 부분에 encoding 옵션 추가함 (정진)
        with open(path + '/' + file_name, 'r', encoding='utf-8') as txtfile, open(csvname+'.csv', 'a', encoding='utf-8') as csvfileout:
            print("csv 쓸거다")
            line = txtfile.read().replace("\n", " ")
            imgCnt = parser.imgCount()
            stiCnt = parser.stickerCnt()
            taglist = parser.hashtags(soup)
            #widgets = parser.widget(soup) #여기서 문제 발생, 일단 0으로 채워지게 함
            videoCnt = parser.videoCnt(soup)

            # add data as long as content is not empty
            if len(line) != 0 :
                writer = csv.DictWriter(csvfileout,fieldnames = ["num", "content", "img", "sticker", "video", "tags", "widget", "isad"])
                writer.writerow({'num' : path[4:] , 'content' : line, 'img' : imgCnt, 'sticker' : stiCnt, 'video' : videoCnt, 'tags' : taglist, 'widget' : 0, 'isad' : isad })
                
        return True

    except Exception as e:
         print(e)
         return False


# download_naver_blog. run
def run(url, output, csvname, foldername): #foldername 인수 추가함
    global out_path
    if not utils.check_out_folder():
        print('폴더 생성에 실패했습니다.')
        exit(-1)
        
    save_folder_path=''
    redirect_url=''
    redirect_url = Parser.redirect_url(url)
    

    ###
    # foldername 인수로 받아 폴더명으로 사용
    save_folder_path = out_path + '/' + foldername
    if utils.check_folder(save_folder_path):
        if utils.check_folder(save_folder_path+'/img'):
            print(foldername + '와 ' + foldername + 'img 폴더를 생성했습니다. ')
    ###

    if crawler(redirect_url, save_folder_path, output, csvname):        
        #print('완료하였습니다. out 폴더를 확인하세요.')
        pass
    else:
        print(save_folder_path + '실패하였습니다.')

if __name__ == '__main__':
    #debug = True 
    debug = False
    if debug is False:
        if len(sys.argv) != 3:
            print('python .\download_naver_blog.py [url of naver blog] [output]')
            print('ex> python .\download_naver_blog.py https://blog.naver.com/chandong83/221951781607 blog.html')
            exit(-1)
        #print(url)
        url = sys.argv[1]
        output = sys.argv[2]
    else:    
        print('디버그 모드')
        url = 'https://blog.naver.com/chandong83/221810614177'
        output = 'parse.html'
        print(url)

    run(url, output)
