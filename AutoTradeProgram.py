import requests
from bs4 import BeautifulSoup
import re
import time
import threading
import pyautogui as pag

buy_refresh = [105,72]
sell_refresh = [728,70]
all_sell = [997,657]
go_to_sell = [1071,285]
all_buy = [573,389]
buy = [528,589]
sell_question = [1020,695]
buy_question = [409,687]
market_price = [555,466]
ok_buy = [417,689]
ok_sell = [1043,686]
market = [1180,498]
pag.PAUSE = 0.35
print("[BTC] auto PROGRAM")


def check_price():
    pattern = re.compile(r'\s+')
    url = requests.get("https://m.bithumb.com/wallet/P102")
    soup = BeautifulSoup(url.text, 'html.parser')
    PriceTag = soup.find(id='tableAsset')
    Price = PriceTag.find(id="realAssetLAMB")
    Price = Price.string
    Price = re.sub(pattern, '', Price)
    Price = Price.replace(",","")

    print("[LAMB] : " + Price + "  " + time.ctime())
    if int(Price) >= 280:
        print("현 시간 부로 매도를 시작합니다.")
        print("매도 시작 시간 : " + time.ctime())
        pag.moveTo(x= all_sell[0], y=all_sell[1], duration=0.0)
        pag.mouseDown()
        pag.mouseUp()

        pag.moveTo(x= sell_question[0], y= sell_question[1], duration=0.0)
        pag.mouseDown()
        pag.mouseUp()
        pag.moveTo(x=ok_sell[0], y=ok_sell[1], duration=0.0)
        pag.mouseDown()
        pag.mouseUp()
    elif int(Price) <= 278:
        print("현 시간 부로 매수를 시작합니다.")
        print("매수 시작 시간 : " + time.ctime())
        pag.moveTo(x=all_buy[0], y=all_buy[1], duration=0.0)
        pag.mouseDown()
        pag.mouseUp()
        pag.mouseDown()
        pag.mouseUp()

        pag.moveTo(x = buy[0], y=buy[1], duration=0.0)
        pag.mouseDown()
        pag.mouseUp()
        pag.moveTo(x=buy_question[0], y=buy_question[1], duration=0.0)
        pag.mouseDown()
        pag.mouseUp()
        pag.moveTo(x=ok_buy[0], y=ok_buy[1], duration=0.0)
        pag.mouseDown()
        pag.mouseUp()
    threading.Timer(3.0,check_price).start()

def refresh_page():
    print("REFRESH SELL_PAGE")
    #매도 페이지 새로고침
    pag.moveTo(x = sell_refresh[0],y=sell_refresh[1],duration=0.0)
    pag.mouseDown()
    pag.mouseUp()
    #매수 페이지 새로 고침
    pag.moveTo(x = buy_refresh[0], y=buy_refresh[1], duration=0.0)
    pag.mouseDown()
    pag.mouseUp()
    pag.moveTo()
    # 새로고침 하면 매수 페이지 인데 다시 매도 페이지로 이동
    pag.moveTo(x=go_to_sell[0], y=go_to_sell[1], duration=0.0)
    pag.mouseDown()
    pag.mouseUp()
    pag.moveTo(x=market_price[0], y=market_price[1], duration=0.0)
    pag.mouseDown()
    pag.mouseUp()
    pag.moveTo(x=market[0], y=market[1], duration=0.0)
    pag.mouseDown()
    pag.mouseUp()
    #최대로 살수 있게 준비

    threading.Timer(23.0, refresh_page).start()

# check_price()
refresh_page()


