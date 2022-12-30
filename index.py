import time

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('Cihaz Gözükmüyor')
        quit()

    device = devices[0]

    print(f'Cihaz Bağlı => {device}')

    return device, client



device, client = connect()



# tıklama olayları
kordinat = '1296 2304' #x , y 
##menü aç
device.shell('input tap {}'.format(kordinat))
# hesap makinasına girsin
hesapmakinaKordinat = "735 1314"
device.shell('input tap {}'.format(hesapmakinaKordinat))

time.sleep(1)
device.shell(f'input text 9')


# device.shell("input keyevent 66")







# # open up camera app
# device.shell('input keyevent 26')
# # wait 5 seconds
# # time.sleep(1)
# # # take a photo with volume up
# # device.shell('input keyevent 24')
# # print('Fotoğraf Çekildi !')


# search_bar = '290 256' # x y
# query = input('')
# search_query = f'what is the definition of {query}'

# device.shell('input keyevent 64')
# time.sleep(0.25) 
# device.shell(f'input tap {search_bar}')


# device.shell(f'input text "{search_query}"') # make sure you have the quotation marks around your text
# device.shell('input keyevent 66')

# time.sleep(3) # wait for results to load



