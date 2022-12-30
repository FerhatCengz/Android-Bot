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


def Scroll():
    device.shell("input swipe 1000 1000 250  250  ")


def takipEt(x, y):
    device.shell("input tap {} {}".format(x, y))





y = 464
for x in range(1, 82):
    takipEt(1272, y)
    y += 250
    if x % 9 == 0:
        Scroll()
        Scroll()
        Scroll()
