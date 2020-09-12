from bs4 import BeautifulSoup
import requests


def scraping_utanet(soup):
    kashi_area_str = str(soup.find('div', id='kashi_area'))
    kashi = kashi_area_str.replace('<div id="kashi_area" itemprop="text">', '')
    kashi = kashi.replace('</div>', '')
    return kashi


def scraping_jlyric(soup):
    kashi_area_str = str(soup.find('p', id='Lyric'))
    kashi = kashi_area_str.replace('<p id="Lyric">', '')
    kashi = kashi.replace('</p>', '')
    return kashi


def scraping_utamap(soup):
    kashi_area_str = str(soup.find('td', class_='noprint kasi_honbun'))
    kashi = kashi_area_str.replace('<td class="noprint kasi_honbun" style="padding-left:30px;">', '')
    kashi = kashi.replace('<!-- 歌詞 end -->', '')
    kashi = kashi.replace('</td>', '')
    return kashi


def scraping(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    if 'uta-net' in url:
        kashi = scraping_utanet(soup)
    elif 'j-lyric' in url:
        kashi = scraping_jlyric(soup)
    elif 'utamap' in url:
        kashi = scraping_utamap(soup)
    # 改行タグを改行に変換
    kashi = kashi.replace('<br>', '\n')
    kashi = kashi.replace('</br>', '\n')
    kashi = kashi.replace('<br/>', '\n')
    return kashi