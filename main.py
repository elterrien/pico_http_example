import network
from time import sleep
import ujson
from config import SSID, PASSWORD, DEVICE_TOKEN

ssid = SSID
password = PASSWORD
device_token = DEVICE_TOKEN

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect(ssid, password)
while not sta_if.isconnected():
    sleep(1)
print('Connection successful')
print(sta_if.ifconfig())
try:
    import urequests
except:
    import upip
    upip.install('micropython-urequests')
    import urequests


data = {"value": 1.0, "token": device_token}
response = urequests.post("https://rutilusdata.fr/api/timeseries/", data=ujson.dumps(data), headers={'content-type': 'application/json'})
json_response = response.json()
print(json_response)
