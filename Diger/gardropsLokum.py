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


def eventClick(x, y):
    device.shell("input tap {} {}".format(x, y))


def eventText(title):
    device.shell("input text '{}'".format(title))


def Scroll():
    device.shell("input swipe 500 1000 300 300 ")  # Aşağıa kaydır


def backButton():
    device.shell('input keyevent 4')  # geri düğmesi


# Ürün giriş fonksiyonları




# ürün fotoğrafları seç
def photoAdd(props):
    eventClick("738.7", "585.2")  # Fotoğraf ekle buttonuna tıklar
    time.sleep(1)
    eventClick("171", "2396.6")  # Galeriye girer
    time.sleep(1)
    eventClick("711.4", "201.8")  # Tüm Fotoğraflara Tıklar
    time.sleep(1)
    # Albüm seçmek için dinamik kordinatlar aşağıdadır...

    # Albümün Kordinatına göre tıklayacak.
    eventClick(props['albumCordinatX'], props['albumCordinatY'])

    # Resim adetine göre seçim yapılır...
    photoSelect(props)

    #Bitti Buttonuna Tıklar
    eventClick("1279.1","195.1")
    time.sleep(0.500)
    #İleri Buttonuna Tıklar
    eventClick("1279.1","195.1")


# Resimleri Adete Göre Seçer
def photoSelect(props):
    if props['photoCount'] <= 10:
        photoX = 236
        photoY = 756.4
        for i in range(1, props['photoCount'] + 1):
            eventClick(photoX , photoY)

            photoX = photoX + 500

            if i % 3 == 0:
                photoY = photoY+500
                photoX = 0
    else:
        print("En Fazla 10 Adet Fotoğraf Seçebilirsiniz...")


# ürün başlığı
def productTitle():
    eventClick("328.3", "1262.9")
    #Copy Paste Yapımı
    lokumlukContent()


#ürün açıklaması
def productContent():
    eventClick('280.5', '910.4')
    #Copy Paste Yapımı
    lokumlukTitle()


def category(props):
    #Kategori Seçim Buttonuna Tıklar
    eventClick("253.1" , "1327.9")
    #Kategori Arama kutusuna tıklar
    eventClick("345.5" , "390.2")
    time.sleep(0.500)
    eventText(props['categoryName'])
    time.sleep(0.500)
    #gelenDegeri seç
    eventClick(props["getCategoryX"] , props['getCategoryY'])


def brandSelect(props):
     #Buttonun X , Y Kordinatları
    eventClick("263.3" , "1564")
    time.sleep(0.500)
    #Kategori Arama kutusuna tıklar
    eventClick("345.5" , "390.2")
    time.sleep(0.500)
    eventText(props['brandName'])
    time.sleep(0.500)
    eventClick(props["getBrandNameX"] , props['getBrandNameY'])





colorObject = {
    # 348.3
    "siyah" : {
        "X" : 543.7,
        "Y" : 527,
    },
     "beyaz" : {
        "X" : 891.3,
        "Y" : 527,
    },
    "mavi" : {
        "X" : 1239.6,
        "Y" : 527,
    }
}

  


def statuSelect(props):
    #Durum buttonun tıklar
    eventClick("591.7" , "1813.9")
    time.sleep(0.500)
    eventClick(props['selectStatuX'] , props['selectStatuY'])

def colorSelect(props , colorName):
    #Renk buttonuna tıklar
    eventClick("431.0" , "2039.8")

    #Renk Seçer 
    eventClick(props[colorName]["X"] , props[colorName]["Y"] )


def prodcutPrice(price):
    #Renk buttona tıklar
    eventClick("478.8","2347.8")
    time.sleep(0.500)
    #Renk fiyat kutusuna tıklar
    eventClick("301","544.2")
    time.sleep(0.500)
    eventText(price)
    eventClick("1296.3","184.8")


def finshButton():
    eventClick("704.5","2234.8")
    time.sleep(1.5)
    eventClick('728.5' , '1889.1')


def lokumlukTitle():
    # device.shell("input touchscreen swipe 75 1611 170 187 2000")
    eventClick("699.5" , "1635.3")
    time.sleep(0.250)
    eventClick("995" , "1903.9")


def lokumlukContent():
    # device.shell("input touchscreen swipe 75 1611 170 187 2000")
    eventClick("699.5" , "1635.3")
    time.sleep(0.250)
    eventClick("278.5" , "1988.8")




photoAddObject = {
    'albumCordinatX': 331,
    'albumCordinatY': 826,
    'photoCount': 3
}


categoryObject = {
 "categoryName"  : "canta",
 "getCategoryX": "417.2",
 "getCategoryY": "766.5",
}

brandSelectObject={
    "brandName" : "mango",
    "getBrandNameX": "665.4",
    "getBrandNameY": "641.7",
}

statuSelectObject = {
   "selectStatuX" : "540.4",
   "selectStatuY" : "451.7",
}



colorObject = {
    # 348.3
    "siyah" : {
        "X" : 543.7,
        "Y" : 527,
    },
     "beyaz" : {
        "X" : 891.3,
        "Y" : 527,
    },
    "mavi" : {
        "X" : 1239.6,
        "Y" : 527,
    },
    "gold" : {
        "X" : 1265.5,
        "Y" : 1718,

    },
    "cesitli":{
        "X":"197.8",
        "Y":"484.7"
    }
}

for x in range(0,20):
    photoAdd(photoAddObject)
    time.sleep(2) #Bekleme Süreleri

    productTitle()

    time.sleep(2) #Bekleme Süreleri
    backButton() 

    time.sleep(2) #Bekleme Süreleri
    productContent()

    backButton() 
    time.sleep(2) #Bekleme Süreleri

    category(categoryObject)
    time.sleep(2) #Bekleme Süreleri

    brandSelect(brandSelectObject)
    time.sleep(2)

    statuSelect(statuSelectObject)
    time.sleep(2) #Bekleme Süreleri

    colorSelect(colorObject , "cesitli")
    time.sleep(2) #Bekleme Süreleri

    prodcutPrice("75")
    time.sleep(2) #Bekleme Süreleri

    Scroll()
    time.sleep(2) #Bekleme Süreleri

    Scroll()
    time.sleep(2) #Bekleme Süreleri

    finshButton()
    print('{} . Ürün Eklendi !'.format(x + 1))
    time.sleep(2) #Bekleme Süreleri

    

