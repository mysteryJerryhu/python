#!/usr/bin/ env python3
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL='https://movie.douban.com/top250'

def download_page(url):

    data = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}).content
    return data


def parse_html(html):
    soup=BeautifulSoup(html)

    movie_list_soup=soup.find('ol',attrs={'class':'grid_view'})

    movie_name_list=[]

    for movie_li in movie_list_soup.find_all('li'):

        detail=movie_li.find('div',attrs={'class':'hd'})
        movie_name=movie_li.find('span',attrs={'class':'title'}).getText()

        movie_name_list.append(movie_name)

    next_page=soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        return movie_name_list,DOWNLOAD_URL +next_page['href']
    return movie_name_list,None
def main():
    url=DOWNLOAD_URL

    with codecs.open('movie','wb',encoding='utf-8')as fp:
        while url:
            html=download_page(url)
            movies,url=parse_html(html)
            fp.write(u'{movie}\n'.format(movie='\n'.join(movies)))

if __name__ == '__main__':
    main()
