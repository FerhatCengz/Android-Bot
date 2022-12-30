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


productTextTitle = {
    "textX": "328.3",
    "textY": "1262.9",
    "text": "Paşabahçe Elysia 6 Lı Çay Bardağı",
}
productTextTitle2 = {
    "textX": "328.3",
    "textY": "1262.9",
    "text": "Ferhat",
}


eventClick(productTextTitle['textX'], productTextTitle['textY'])
device.shell("input text '67'")