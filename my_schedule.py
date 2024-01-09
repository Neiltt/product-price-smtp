import schedule
import time
import my_crawler
def job():
    print("I'm working")
def parse_shop():
    url = "https://lukahuang.github.io/simple_pages/amazon_jp.html"
    try:
        my_crawler.parse_html(url)
    except Exception as e:
        print('exception!')

schedule.clear()
schedule.every(1).seconds.do(job)
schedule.every(3).seconds.do(parse_shop)
# schedule.every().wednesday.at("07:00").do(parse_shop)

while True:
    schedule.run_pending() #閒置
    time.sleep(1)