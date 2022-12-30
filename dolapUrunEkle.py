# encoding:utf-8
import time

from ppadb.client import Client as AdbClient


def connect():
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)

    devices = client.devices()

    if len(devices) == 0:
        print('Cihaz Gözükmüyor')
        quit()

    device = devices[0]

    print(f'Cihaz Bağlı => {device}')

    return device, client


device, client = connect()


def backButton():
    device.shell('input keyevent 4')  # geri düğmesi


def productAdd():
    device.shell("input tap 726 2174")


def photoAdd():
    device.shell("input tap 227 747")  # Fotoğraf Ekle Buttonuna Tıklar
    time.sleep(1.5)
    device.shell("input tap 115 1954")  # Fotoğraf Galersine Tıklar
    time.sleep(0.250)
    # Fotoğraf Albümüne Gelir (Seçme İşlemi Yapılması İçin) 12
    device.shell("input tap 767 204")  # 12
    time.sleep(0.250)
    device.shell("input tap 601 435")  # Gold Lokumluk Albümünü Açar
    time.sleep(0.250)
    device.shell("input tap 506 2026")  # Gold Lokumluk Fotoğrafını Seçer
    time.sleep(0.250)
    device.shell("input tap 1310 217")  # Devam Buttonuna Tıklar
    time.sleep(0.250)
    device.shell("input tap 1310 217")  # Devam Buttonuna Tıklar


def prodcutTitle():
    device.shell("input tap 536 1444")
    time.sleep(1)
    device.shell("input text '6 Li Ayna Motifli Gold Lokumluk'")
    backButton()


def prodcutContent():
    device.shell("input tap 112 1903")
    device.shell(f"input text 'Urun Sifirdir 2.El Degildir !'")
    backButton()
    time.sleep(0.400)
    Scroll()


def categoryAdd():
    device.shell("input tap 407 1669")
    device.shell("input tap 159 1370")
    device.shell("input tap 601 1716")
    device.shell("input tap 509 2012")
    # Scroll() gerekmiyor Altın GOLD İÇİN


def brandSelect():
    device.shell("input tap 346 1914")
    device.shell("input tap 319 737")


def colorSelect():
    device.shell("input tap 366 2104")
    device.shell("input tap 217 493")
    Scroll()


def Scroll():
    device.shell("input swipe 500 1000 300 300 ")


def cargoSelect():
    device.shell("input tap 546 1618")
    device.shell("input tap 529 1040")
    device.shell("input tap 1005 2056")
    Scroll()


def cargoPaymentType():
    device.shell("input tap 557 2135")
    Scroll()


def prodcutPrice(buying, selling):
    device.shell("input tap 1151 1723")  # alış fiyatı
    device.shell("input text '{}'".format(buying))
    # ileri geç ve satış fiyatına focusla
    device.shell("input tap 1239.5 1917.5")
    device.shell("input text '{}'".format(selling))
    device.shell("input tap 1239.5 1917.5")  # tamama tıkla ve bitir.


def finshButton():
    device.shell("input tap 675 2407")  # onaylama buttonu


def enterNewProduct():
    device.shell("input tap 991.7 1577.5")




for x in range(0, 5):
    photoAdd()
    prodcutTitle()
    prodcutContent()
    categoryAdd()
    brandSelect()
    colorSelect()
    cargoSelect()
    cargoPaymentType()
    prodcutPrice(buying="115", selling="90")
    time.sleep(10)
    finshButton()


# # device.shell("input swipe 300 300 500 1000") # Yukarı
# device.shell("input swipe 500 1000 300 300 ") # Aşağı
