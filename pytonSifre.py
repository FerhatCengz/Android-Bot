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


device.shell("input tap 716 1198")
sifreler = ["1313" , "1353" , "1111" ,"1354" , "1334"]

for x in sifreler:
    device.shell("input text '{}'".format(x))
    device.shell("input tap 1115 2041")

