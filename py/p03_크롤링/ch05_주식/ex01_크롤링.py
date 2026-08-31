from urllib.request import urlopen
from bs4 import BeautifulSoup

def crawl_stock_data():

    # 주식 데이터 웹 크롤링과 데이터베이스 다루기
    # 주식 사이트에 접속하기
    # http://comp.fnguide.com

    # 주식 데이터 크롤링
    # 기본 정보 웹 크롤링

    url = 'https://wcomp.fnguide.com/?c_id=AA&menu_type=01&cmp_cd=005930'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    # 1. 날짜
    date1 = soup.find('span', {'class':'date'})
    print(date1.text)

    # 날짜의 형식 변경
    # [2026/08/14] -> 2026-08-14
    date2 = date1.text
    # replace(이전텍스트, 새텍스트)
    date = date2.replace('[','').replace(']','').replace('/','-')
    print(date)


    # 2. 종목 이름
    corp_name1 = soup.find('h1', {'id':'giName'})
    print(corp_name1)
    # <h1 id="giName">삼성전자</h1>
    corp_name = corp_name1.text
    print(corp_name)


    # 3. 종목 코드
    code = soup.find_all('h2')[0].text
    print(code)
    """ 
    005930
    """


    # 4. 주가: 방법1
    stock_price1 = soup.find_all('td', {'class':'cle r'})
    stock_price = int(stock_price1[5].text.replace(',',''))
    print(stock_price)
    # 274500

    # 4. 주가: 방법2
    stock_price1 = soup.find("tr", {"class":"rwf"})
    # 1. r 클래스를 가진 td 태그를 먼저 찾습니다.
    td_tag = stock_price1.find("td", {"class": "r"})

    # 2. td 태그 바로 아래에 있는 첫 번째 텍스트 노드를 추출하고, 공백(&nbsp;)과 ',', '/'를 제거합니다.
    stock_price1 = td_tag.find(string=True).replace('/', '').replace(',', '').strip()
    stock_price = int(stock_price1)
    print(stock_price)  # 출력: 279500


    # 5. 외국인 보유 비중
    fgn_own_ratio1 = soup.find_all('td', {'class':'cle r'})
    # print(fgn_own_ratio1)
    """ 
    [<td class="cle r">21,669,476</td>, <td class="cle r">58,745</td>, <td class="cle r">46.71</td>, <td class="cle r">1.25203</td>, <td class="cle r">100</td>, <td class="cle r">274,500</td>, <td class="cle r">
                                17,393,427/ 
                                47,453
                            </td>, <td class="cle r">7.39</td>, <td class="cle r">5.59</td>, <td class="cle r">5.22</td>, <td class="cle r">6.43</td>, <td class="cle r">2.76</td>, <td class="cle r">2.19</td>, <tdclass="cle r">6.74</td>, <td class="cle r">3.97</td>, <td class="cle r">3.10</td>, <td class="cle r">2.60</td>]
    """
    fgn_own_ratio = float(fgn_own_ratio1[2].text)
    print(fgn_own_ratio)
    # 46.71


    # 6. 1Y 수익률
    rel_return1 = soup.find_all('span', {'class':'tcr'})
    rel_return2 = rel_return1[2].text.replace('+','')
    rel_return = float(rel_return2)
    print(rel_return)
    # 283.38


    # 상단 테이블 웹 크롤링
    up_list = soup.find('div', {'class':'corp_group2'})
    # print(up_list)

    dd = up_list.find_all('dd')
    # print(dd)

    # 7. PER(Price Earning Ratio: 주가수익비율)
    per = float(up_list.find_all('li')[1].text)
    print(per)
    # 41.82

    # 8. 12M PER (12개월 뒤의 예상 주가수익비율)
    per_12m = float(up_list.find_all('li')[3].text)
    print(per_12m)
    # 4.57

    # 9. 업종 PER
    raw_text = up_list.find_all('li')[5].text.strip()

    if raw_text and raw_text != '-':
        per_ind = float(up_list.find_all('li')[5].text)
    else:
        per_ind = 0.0

    print(per_ind)
    # 31.68

    # 10. PBR(Price to Book Ratio: 주가순자산비율)
    # PBR = 주가 / 주당순자산
    pbr = float(up_list.find_all('li')[7].text)
    print(pbr)
    # 4.29

    # 11. 배당수익률(Dividend Yield)
    div_yid1 = up_list.find_all('li')[9].text
    div_yid2 = div_yid1.replace('%','')
    div_yid = float(div_yid2)
    print(div_yid)
    # 0.61


    # 시세현황 테이블 웹 크롤링
    table1 = soup.find('div', {'id':'div1'})
    table2 = table1.find_all('td')
    # print(table2)

    """ 
    <td class="r">
                                274,500/ 
                                <span class="tcr">
                                    +6,500
                                </span>/ 
                                <span class="tcr">
                                    +2.43
                                </span>
    </td>, <td class="cle r">21,669,476</td>, <td class="r">
                                374,500/ 
                                67,500
                            </td>, <td class="cle r">58,745</td>, <td class="r">
    <span class="tcr">+4.37</span>/ 
                                <span class="tcb">-7.26</span>/ 
                                <span class="tcr">+51.49</span>/ 
                                <span class="tcr">+283.38</span>
    </td>, <td class="cle r">46.71</td>, <td class="r">17,617,473</td>, <td class="cle r">1.25203</td>, <td class="r">16,048,035</td>, <td class="cle r">100</td>, <td class="r">
                                5,846,278,608/ 
                                802,371,203
                            </td>, <td class="cle r">274,500</td>, <td class="r">
                                4,424,152,717/ 
                                75.67
                            </td>, <td class="cle r">
                                17,393,427/ 
                                47,453
                            </td>]
    """

    # 12. 거래량
    volume1 = table2[1].text
    volume = int(volume1.replace(',','').strip())
    print(volume)
    # 21669476

    # 13. 거래대금
    trans_price1 = table2[3].text
    trans_price = int(trans_price1.replace(',','').strip())
    print(trans_price)

    # 58745

    # 14. 시가총액(우선주 포함, Market Capitalization Preferred)
    mk_cpt_pfr1 = table2[6].text
    mk_cpt_pfr = int(mk_cpt_pfr1.replace(',','').strip())
    print(mk_cpt_pfr)

    # 17617473	

    # 15. 시가총액(보통주, Market Capitalization Common)
    mk_cpt_cm1 = table2[8].text
    mk_cpt_cm = int(mk_cpt_cm1.replace(',','').strip())
    print(mk_cpt_cm)

    # 16048035	

    # 결과 모음
    res = [
        date,
        corp_name,
        code,
        stock_price,
        fgn_own_ratio,
        rel_return,
        per,
        per_12m,
        per_ind,
        pbr,
        div_yid,
        volume,
        trans_price,
        mk_cpt_pfr,
        mk_cpt_cm
    ]

    # print(res)
    # print(len(res))
    print('크롤링 완료! 결과를 res에 담았습니다.')

    return res

