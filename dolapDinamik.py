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


def photoAdd(prodcut):
    device.shell("input tap 227 747")  # Fotoğraf Ekle Buttonuna Tıklar
    time.sleep(1.5)
    device.shell("input tap 115 1954")  # Fotoğraf Galersine Tıklar
    time.sleep(0.250)
    # Fotoğraf Albümüne Gelir (Seçme İşlemi Yapılması İçin) 12
    device.shell("input tap 767 204")  # 12
    time.sleep(0.250)

    # Buralar dinamik olmalı
    if prodcut == "lokumluk":
        device.shell("input tap 528 488")  # Gold Lokumluk Albümünü Açar
        time.sleep(0.250)
        device.shell("input tap 539 2341")  # Gold Lokumluk Fotoğrafını Seçer
        time.sleep(0.250)
        device.shell("input tap 958 2054")  # İkinci Foto
        time.sleep(0.250)
        device.shell("input tap 1286 2092")  # Üç Foto
        time.sleep(0.250)
        device.shell("input tap 426 1918")  # Dört Foto
        time.sleep(0.250)

    if prodcut == "pasabahce bardak":
        device.shell("input tap 539 819")  # Paşabahçe Bardak  albümünü açar
        time.sleep(0.250)
        device.shell("input tap 839 2058")  # İlk fotoyu seçer
        time.sleep(0.250)
        device.shell("input tap 506 2026")  # İkinci Foto
        time.sleep(0.250)
        device.shell("input tap 1238 2010")  # Üç Foto
        time.sleep(0.250)
        device.shell("input tap 167 2396")  # Dört Foto
        time.sleep(0.250)
    # Değişmeyecek !
    device.shell("input tap 1310 217")  # Devam Buttonuna Tıklar
    time.sleep(0.250)
    device.shell("input tap 1310 217")  # Devam Buttonuna Tıklar


def prodcutTitle(title):
    device.shell("input tap 536 1444")
    time.sleep(1)
    pasabahceYaz()
    device.shell("input text '{}'".format(title))
    backButton()


def prodcutContent(content):
    device.shell("input tap 112 1903")
    device.shell(f"input text '{content}'".format(content))
    backButton()
    time.sleep(0.400)
    Scroll()


def categoryAdd(categoryName):
    device.shell("input tap 407 1669")
    device.shell("input tap 159 1370")
    device.shell("input tap 601 1716")

    if categoryName == 'tepsi':
        Scroll()
        Scroll()
        Scroll()
        Scroll()
        device.shell("input tap 498 1222")

    if categoryName == 'saklama kapları':
        device.shell("input tap 509 2012")

    if categoryName == 'bardak':
        Scroll()
        Scroll()
        Scroll()
        device.shell("input tap 907 1990")


def brandSelect(brand=''):
    device.shell("input tap 505 1884")
    if brand == 'paşabahçe':
        device.shell("input tap 290 450")
        time.sleep(0.250)
        device.shell("input touchscreen swipe 75 1611 170 187 2000")
        device.shell("input tap 1337 2218")
        device.shell("input tap 334 750")
        backButton()

    else:
        device.shell("input tap 47 665")


def colorSelect(color):
    device.shell("input tap 354 2116")
    if color == 'gold':
        device.shell("input tap 366 2104")
    if color == 'seffaf':
        print("renk seçimi seffef !")
        Scroll()
        Scroll()
        Scroll()
        Scroll()
        device.shell("input tap 880 2341")

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
    # device.shell("input tap 557 2135") #satıcıya ait tıkla
    Scroll()


def prodcutPrice(buying, selling):
    device.shell("input tap 1151 1723")  # alış fiyatı
    device.shell("input text '{}'".format(buying))
    # ileri geç ve satış fiyatına focusla
    time.sleep(0.250)
    device.shell("input tap 1239 1917")
    device.shell("input text '{}'".format(selling))
    device.shell("input tap 1239 1917")  # tamama tıkla ve bitir.




buttonaBasmaSayisi = 0
def finshButton():
    time.sleep(0.250)
    device.shell("input tap 675 2407")  # onaylama buttonu
    
    print("Girilen {} . Ürün" .format(buttonaBasmaSayisi))


def enterNewProduct():
    device.shell("input tap 991.7 1577.5")


def pasabahceYaz():
    device.shell("input touchscreen swipe 75 1611 170 187 2000")


for x in range(0, 50):
    photoAdd(prodcut="pasabahce bardak")  # Resim ekler
    time.sleep(1)

    prodcutTitle(title='Elysia Bardak 6 Li')  # başlık kısmı
    time.sleep(1)

    prodcutContent(content='Urun Sifirdir 2.El Degildir !')  # açıklama kısmı
    time.sleep(1)

    categoryAdd(categoryName='bardak')
    time.sleep(1)

    brandSelect(brand='paşabahçe')
    time.sleep(1)

    colorSelect(color='seffaf')
    time.sleep(1)

    cargoSelect()
    time.sleep(1)

    cargoPaymentType()  # Kategori alıcı türünü seçiyor
    time.sleep(0.499)

    prodcutPrice(buying="130", selling="99")
    time.sleep(0.499)
    finshButton()
    time.sleep(10)
    enterNewProduct()
    time.sleep(0.850)

# # device.shell("input swipe 300 300 5009898 1000") # Yukarı
# device.shell("input swipe 500 1000 300 300 ") # Aşağı
