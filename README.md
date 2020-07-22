# 코알라 해커톤 : 리뷰를 낚는 자들 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

  - 20.07.07 ~ 


# New Features! (20.07.22 수정)

- 네이버 검색어 상세 설정 가능 
  - 특정 키워드 반드시 포함, 제외, 정확히 일치 
- 수집 가능한 데이터 
  - 게시글 주소(num), 텍스트(content), 사진 수(img)
  - 비디오 수(video), 블로그 내 위젯 개수(widget) 
  - 텍스트 내 태그 존재 여부 (tags) 
  - 광고글 판단 여부 (isad)
  
- 검색어 별 수집한 데이터 csv 파일로 저장 

+ 수정
- 터미널 프린트 내용 

- csv 파일 예시

![image](./image/image.png)



You can also:
  - 사진 파일 크롤링 및 저장
  - 페이지 내 full_code 저장 가능


### Tech

* [Python] - 



### Installation

실행 방법 

```sh
$ cd naverblog
$ python3 crawl.py 
```


### Todos

 - 검색 결과에서 페이지가 마지막인 경우 자동으로 프로그램 종료하기 

License
----

네이버 블로그 txt 추출 코드 출처
:: https://github.com/chandong83/download-naver-blog



** 냠 !**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
