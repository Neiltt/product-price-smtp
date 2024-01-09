import re
import requests
from bs4 import BeautifulSoup

def parse_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    product_name = soup.find('span', id="productTitle").getText().strip()
    price_text = soup.find('span', id="priceblock_ourprice").getText()
    print(f"product_name: {product_name[:10]}, price_text: {parse_price(price_text)}")
    return parse_price(price_text)

def parse_price(text):
    pattern = r'[\d,]+'
    result = re.search(pattern, text).group(0).replace(",", "")
    return int(result)
    # print(int(result))

url = 'https://lukahuang.github.io/simple_pages/amazon_jp.html'
# 測試
# parse_html(url)