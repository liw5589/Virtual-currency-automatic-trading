import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QComboBox,QLineEdit
import pyautogui as pag
import requests
from bs4 import BeautifulSoup
import re
import time
import threading
#660,520

class MyApp(QWidget):



    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('가상화폐 자동 매수.매도 프로그램', self)
        title.move(110, 20)
        font = title.font()
        font.setPointSize(20)
        font.setFamily('Droid Sans Fallback')
        title.setFont(font)

        coinName = QLabel('가상화폐',self)
        coinName.move(150,110)
        otherfont = coinName.font()
        otherfont.setPointSize(16)
        otherfont.setFamily("Droid Sans Fallback")
        coinName.setFont(otherfont)

        refreshTime = QLabel('가격 갱신 주기 (초)',self)
        refreshTime.move(100,180)
        refreshTime.setFont(otherfont)

        currentPrice = QLabel('현재가',self)
        currentPrice.move(160,250)
        currentPrice.setFont(otherfont)

        buyPrice = QLabel('매수가',self)
        buyPrice.move(160,320)
        buyPrice.setFont(otherfont)

        sellPrice = QLabel('매도가',self)
        sellPrice.move(160,390)
        sellPrice.setFont(otherfont)

        okBtn = QPushButton('실행', self)
        okBtn.resize(160,40)
        okBtn.move(320,450)
        btnFont = okBtn.font()
        btnFont.setPointSize(12)
        btnFont.setFamily('Droid Sans Fallback')
        okBtn.setFont(btnFont)
        okBtn.setCheckable(True)

        clsBtn = QPushButton('닫기',self)
        clsBtn.resize(160,40)
        clsBtn.move(490,450)
        clsBtn.setFont(btnFont)
        clsBtn.setCheckable(True)

        cbCoinName = QComboBox(self)
        cbCoinName.addItem('비트코인[BTC]')
        cbCoinName.addItem('리플[RIP]')
        cbCoinName.addItem('람다[LAMB]')
        cbCoinName.addItem('이더리움[ETD]')
        cbCoinName.resize(200,40)
        cbCoinName.move(400, 110)
        cbCoinName.setFont(otherfont)

        leSecond = QLineEdit(self)
        leSecond.resize(200,40)
        leSecond.move(400, 180)
        leSecond.setFont(otherfont)


        lbcurrent = QLabel(' '+'원', self)
        lbcurrent.move(400, 250)
        lbcurrent.setFont(otherfont)

        leBuyPrice = QLineEdit(self)
        leBuyPrice.resize(200, 40)
        leBuyPrice.move(400, 320)
        leBuyPrice.setFont(otherfont)


        leSellPrice = QLineEdit(self)
        leSellPrice.resize(200, 40)
        leSellPrice.move(400, 390)
        leSellPrice.setFont(otherfont)


        okBtn.clicked.connect(self.okBtnClicked)

        self.setWindowTitle('My First Application')
        self.move(1250, 470)
        self.resize(660, 520)
        self.show()

    def okBtnClicked(self):
        pattern = re.compile(r'\s+')
        url = requests.get("https://m.bithumb.com/wallet/P102")
        soup = BeautifulSoup(url.text, 'html.parser')
        PriceTag = soup.find(id='tableAsset')
        Price = PriceTag.find(id="realAssetLAMB")
        Price = Price.string
        Price = re.sub(pattern, '', Price)
        print("[LAMB] : " + Price + "  " + time.ctime())
        MyApp.lbcurrent.setText("qqq")
        threading.Timer(3.0, self.okBtnClicked).start()






app = QApplication(sys.argv)
ex = MyApp()

sys.exit(app.exec_())

