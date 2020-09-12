from bs4 import BeautifulSoup
import requests
import string


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


def convert_kashi(kashi):
    ans = []
    for line in kashi.split('\n'):
        if len(line) == 0:
            ans.append(line)
        elif line in ['Aメロ', 'Bメロ', 'Cメロ', 'サビ', '大サビ', '落ちサビ', 'アウトロ', '間奏', '1番', '2番', 'intro', 'イントロ']:
            ans.append(line)
        else:
            # 非アスキー文字が含まれたら歌詞
            # （一行の各文字の集合からアスキー文字+記号の集合を引いた結果が空集合じゃなければ）
            if set(line) - set(string.printable):
                ans.append(f'<span class="lylic">{line}</span>')
            else:
                ans.append(f'<span class="chord">{line}</span>')
    ans.insert(0, '<pre class="gakuhu">')
    ans.insert(0, '<script>var default_key = "0";</script>')
    ans.insert(0, '<select id="selSpeed" onchange="scrollSpeed(this)"></select>')
    ans.insert(0, '<select id="selStep" onchange="convert(this);"></select>')
    ans.append('</pre>')
    res = '\n'.join(ans)
    return res

