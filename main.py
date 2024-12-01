import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

districts = ['dongcheng', 'xicheng', 'haidian', 'chaoyang']
base_url = "https://bj.lianjia.com/ershoufang/{}/pg{}/"

cookies = {
    'SECKEY_ABVK': 'KxEoPi5dfoK9cA+HKu3oU1Qf4UNIcoCH2CnIrX5jpP0%3D',
    'select_city': '110000',
    'lianjia_ssid': '05e728cd-f266-4319-a6db-b936588dd91a',
    'lianjia_uuid': 'c05722e9-7ee2-436b-b861-abc593f2d345',
    'Hm_lvt_46bf127ac9b856df503ec2dbf942b67e': '1733032579',
    'HMACCOUNT': '2F8F7E6C1A4514E1',
    '_jzqc': '1',
    '_jzqckmp': '1',
    '_qzjc': '1',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219380ca90d38d4-0f1a9bb1633849-4c657b58-1327104-19380ca90d41918%22%2C%22%24device_id%22%3A%2219380ca90d38d4-0f1a9bb1633849-4c657b58-1327104-19380ca90d41918%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    '_ga': 'GA1.2.893090346.1733032590',
    '_gid': 'GA1.2.1564072178.1733032590',
    'crosSdkDT2019DeviceId': '3rlvdr-8pbec2-n6gmijqp2hdvxy2-ri5sv0ucr',
    'login_ucid': '2000000006668913',
    'lianjia_token': '2.00107cb5856a981a1801d19cb4f363c593',
    'lianjia_token_secure': '2.00107cb5856a981a1801d19cb4f363c593',
    'security_ticket': 'N96Ze/HpwkLRXUxJg3T483HaWnuXLMzo2osev+NHl8KeRC8iuWpunoZnWhES9HJDlX5D6FMI3+MDLXzvT6skfz7bgJDSsqgbDFDiomTkygx6ki0GdBIKEv72/lPTwohPGHGc1ejQfl2WOe+Y/gNEdkunS80SsmWZiJfbDttEwwc=',
    'ftkrc_': '09ed7e4c-8e7b-468b-a21f-08fd4854ff81',
    'lfrc_': '53f6a21a-a180-48f1-b313-551cf98307cf',
    'Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e': '1733033935',
    '_ga_QJN1VP0CMS': 'GS1.2.1733032590.1.1.1733033941.0.0.0',
    '_ga_KJTRWRHDL1': 'GS1.2.1733032590.1.1.1733033941.0.0.0',
    '_qzja': '1.182761032.1733032579279.1733032579279.1733041289096.1733035807560.1733041289096.0.0.0.11.2',
    '_qzjb': '1.1733041289096.1.0.1.0',
    '_qzjto': '11.2.0',
    '_jzqa': '1.3606453018518002700.1733032579.1733032579.1733041289.2',
    '_jzqx': '1.1733041289.1733041289.1.jzqsr=bj%2Elianjia%2Ecom|jzqct=/ershoufang/dongcheng/.-',
    '_jzqb': '1.1.10.1733041289.0',
    'srcid': 'eyJ0Ijoie1wiZGF0YVwiOlwiMGFkOTgyZmQ0OGNmNjI1N2JiOTdmMTU5YzRkYzFjOWE5ZTk5OTA5NzRlNWEzOTEwMDg2Y2MwNmU3YjQ2OWNmZjVhNTZjOTIyMzVlMjA2MTQ0NGM1YzJhNzk1NDVmODU0MWNkZGEzNTY5OWM3MDk0ZWJiZjRlMzNkMGZkMzY4MWM3MjQ5MmNiZjVlM2ZhZTdjNmRhZDNmNzkxYTkzM2ExYTA4MWM4MTdiMmU5ZTcwZTE1OTkxYTUwMmJiNzljOTlhOTg1NWJlNGZmZTYxZDc1NWUwOTA2ZDk2YTA3OWQyZmIxZDVmMjY2ZDcyNDE0NjUzMTY2Y2E3MDE3NDg1OTcxNVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI3ODEzNGMzZVwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcveGljaGVuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
}

data = []

for district in districts:
    for page in range(1, 4):
        url = base_url.format(district, page)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
        }

        response = requests.get(url, headers=headers, cookies=cookies)
        response.encoding = 'utf-8'

        print(f"Fetching URL: {url}, Status Code: {response.status_code}")
        if response.status_code != 200:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        listings = soup.find_all('div', class_='info clear')

        for listing in listings:
            try:
                position_info = listing.find('div', class_='positionInfo').find_all('a')
                community_name = position_info[0].text.strip()
                region_name = position_info[1].text.strip()

                size_info = listing.find('div', class_='houseInfo').text
                size = size_info.split('|')[1].strip()

                total_price = listing.find('div', class_='totalPrice').find('span').text.strip() + "万"

                unit_price = listing.find('div', class_='unitPrice').find('span').text.strip()

                data.append([district, community_name, region_name, size, total_price, unit_price])
            except AttributeError:
                continue

        delay = random.uniform(1, 3)  # 随机延时1到3秒
        print(f"Sleeping for {delay:.2f} seconds to reduce request frequency.")
        time.sleep(delay)

df = pd.DataFrame(data, columns=['城区', '小区名称', '区域名称', '平米数', '总价', '单价'])

df.to_csv('ershoufang.csv', index=False, encoding='utf-8')
print("成功保存数据至 ershoufang.csv")
