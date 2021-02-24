import json
import os
import re

import nltk
import requests
from requests.exceptions import SSLError
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_soup(url: str):
    ua = UserAgent()
    session = requests.Session()

    headers = {'User-Agent': ua.random}
    response = session.get(url, headers=headers)
    html = response.text.strip()

    return BeautifulSoup(html, 'html.parser')


def web_scraping_function(domain: str, url: str):
    if domain in ['realestate.daum.net']:
        soup = get_soup(url)
        for s in soup.find_all('div', id='dmcfContents'):
            s = s.find('p')
            if not s:
                continue
            return s.get_text()

    if domain in ['flipboard.com', 'amp.flipboard.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_='post post--card post--article-view'):
            return s.get_text()

    if domain in ['news.zum.com', 'cnbc.sbs.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(id='article_body'):
            return s.get_text()

    if domain in ['www3.edaily.co.kr', 'www.edaily.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_='news_body'):
            return s.get_text()

    if domain in ['m.news.zum.com', 'www.inews24.com', 'www4.edaily.co.kr', 'theqoo.net', 'www.inews24.com',
                  'm.edaily.co.kr', 'www.asiae.co.kr', 'm.newspim.com', 'www.youthdaily.co.kr', 'm.joseilbo.com',
                  'www.futurekorea.co.kr', 'www.insightkorea.co.kr', 'www.dailysmart.co.kr', 'www.m-i.kr',
                  'www.zdnet.co.kr', 'news.mt.co.kr', 'news.joins.com', 'www.ttlnews.com', 'www.infostockdaily.co.kr',
                  'www.etoday.kr', 'www2.edaily.co.kr', 'moneys.mt.co.kr', 'web.etoday.co.kr', 'zum.com',
                  'news.heraldcorp.com', 'stage1.edaily.co.kr', 'www.instiz.net', 'mbiz.heraldcorp.com',
                  'm.moneys.mt.co.kr',
                  'www.jgnews.co.kr', 'v2.m.edaily.co.kr', ]:
        soup = get_soup(url)
        for s in soup.find_all(itemprop="articleBody"):
            return s.get_text()

    if domain == 'www.paxnet.co.kr':
        soup = get_soup(url)
        for s in soup.find_all(id='span_article_content'):
            s = s.find('p')
            if not s:
                continue
            return s.get_text()

    if domain in ['www.mediapen.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_='view_r'):
            return s.get_text()

    if domain in ['kr.investing.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_='WYSIWYG articlePage'):
            return s.get_text()

    if domain in ['blog.naver.com']:
        soup = get_soup(url)
        for s in soup.find_all('div', id='postViewArea'):
            return s.get_text()

    if domain in ['www.mimint.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_='board_content'):
            return s.get_text()

    if domain in ['heraldk.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_="entry-content"):
            return s.get_text()

    if domain in ['m.newspic.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="article_view"):
            return s.get_text()

    if domain in ['m.stock.naver.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_="newsct_body"):
            return s.get_text()

    if domain in ['www.hankyung.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="articletxt"):
            return s.get_text()

    if domain in ['biz.heraldcorp.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="articleText"):
            return s.get_text()

    if domain in ['www.yna.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="story-news article"):
            return s.get_text()

    if domain in ['m.ceoscoredaily.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="news_body_area"):
            return s.get_text()

    if domain in ['m.dnews.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="articleContent va_cont"):
            return s.get_text()

    if domain in ['biz.newdaily.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="nd-news-body smartOutput"):
            return s.get_text()

    if domain in ['inthenews.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="post-content"):
            return s.get_text()

    if domain in ['www.newswire.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="release-story"):
            return s.get_text()

    if domain in ['newsum.zum.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_="article_text"):
            return s.get_text()

    if domain in ['www.paxetv.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="article-view-content-div"):
            return s.get_text()

    if domain in ['sgsg.hankyung.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="contents"):
            return s.get_text()

    if domain in ['marketinsight.hankyung.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="newsView"):
            return s.get_text()

    if domain in ['www.philgo.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_="post_view_content"):
            return s.get_text()

    if domain in ['www.nfa.go.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="board_content"):
            return s.get_text()

    if domain in ['mrealfoods.heraldcorp.com', 'www.etoland.co.kr', 'realfoods.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(id="view_content"):
            return s.get_text()

    if domain in ['mlbpark.donga.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="contentDetail"):
            return s.get_text()

    if domain in ['ppomppu.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="board-contents"):
            return s.get_text()

    if domain in ['www.joongboo.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="article-view-content-div"):
            return s.get_text()

    if domain in ['www.itooza.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="article-body"):
            return s.get_text()

    if domain in ['newslabit.hankyung.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="articletxt"):
            return s.get_text()

    if domain in ['goch.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="brdView"):
            return s.get_text()

    if domain in ['m.wowtv.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(id="divNewsContent"):
            return s.get_text()

    if domain in ['m.newsprime.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(id="cnt_veiw"):
            return s.get_text()

    if domain in ['www.dmitory.com']:
        soup = get_soup(url)
        for s in soup.find_all(id="rd_body_content"):
            return s.get_text()

    if domain in ['hisoft-investment.tistory.com']:
        soup = get_soup(url)
        for s in soup.find_all(class_="article_cont"):
            return s.get_text()

    if domain in ['www.ebn.co.kr']:
        soup = get_soup(url)
        for s in soup.find_all(class_="article"):
            return s.get_text()

    if domain in ['m.gurinet.org']:
        soup = get_soup(url)
        for s in soup.find_all(id="MRead_b"):
            return s.get_text()


if __name__ == '__main__':
    # download NLT kit model
    nltk.download('punkt')

    # if the file is 1links.json, then replace links.json with 1links.json
    base_path = os.path.abspath('')
    links_json_name = '2links.json'
    links_path = os.path.join(base_path, links_json_name)
    with open(links_path, encoding='utf-8') as fh:
        data = json.load(fh)

    # json file structure
    # key = domain of each new site
    # value = [ ["news title1", "news link1"] , ["news title2", "news link2"] ]
    # so it is a list of lists where the inner list contains title of the news and the link
    result = {}
    count = 0
    for domain, link_infos in data.items():
        print(f"Scraping: {domain}")

        for info in link_infos:
            # get info needed
            news_title = info[0]
            news_url = info[1]

            valid_subject_list = []
            try:
                current_news_subject = web_scraping_function(domain, news_url)
            except SSLError:
                continue

            if not current_news_subject:
                continue

            try:
                # tokenize and extract sentences using NLT
                tokens = nltk.sent_tokenize(current_news_subject)
            except TypeError:
                continue

            for token in tokens:
                # strip trailing whitespaces
                token: str = token.strip()

                # skip if any newline characters exist in subject
                if any(x in token for x in ['\n', '\r', '\t']):
                    continue
                token = " ".join(token.split())

                token.encode('utf-8')
                # trim
                trimmed = re.split('[?!.]', token)

                # iterate regex trimmed list of sentences and filter
                for t in trimmed:
                    if t == '':
                        continue
                    if len(t) < 15:  # likely to be spam infos
                        continue
                    valid_subject_list.append(t)

            result[news_title] = valid_subject_list

    # dump to json
    result_path = os.path.join(base_path, 'scraped_result.json')
    with open(result_path, 'w', encoding='utf8') as fp:
        json.dump(result, fp, ensure_ascii=False)
