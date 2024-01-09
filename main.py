import schedule
import time
from my_mongo import get_min_price
from my_mongo import set_min_price
from my_crawler import parse_html
from my_mailer import send_mail

def job():
    print("I am working")

product_name = "Nintendo S"
set_min_price(product_name, 60000)

def parse_shop(mim_price=None):
    if not mim_price:
        mim_price = get_min_price(product_name)
    try:
        url = 'https://lukahuang.github.io/simple_pages/amazon_jp.html'
        price = parse_html(url)
        if price < mim_price:
            set_min_price(product_name, price)
            mim_price = price
            send_mail(product_name, price)
    except Exception as e:
        print(e)

schedule.every(1).seconds.do(job)
schedule.every(5).seconds.do(parse_shop)

while True:
    schedule.run_pending()
    time.sleep(1)
