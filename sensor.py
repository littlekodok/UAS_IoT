import serial
import time
import requests
import json

arduino = serial.Serial ('COM4', 9600)

def ledControl (cmd):
arduino.write (cmd.encode())

while True:
    rawArd = arduino.readline()
    data = rawArd [0:len(rawArd) -2 ] . decode ("utf-8")
    resp = requests.get ("http://localhost/minapadi/login/dashboardikannila/ikan_nila.php" + data)
    dataWeb = json.loads (resp.text)
    if dataWeb['1'] == '1':
        ledControl ('A')
    elif dataWeb['1'] == '0':
        ledControl ('B')
    if dataWeb['2'] == '1':
        ledControl ('C')
    elif dataWeb['2'] == '0':
        ledControl ('D')
    if dataWeb['3'] == '1':
        ledControl ('E')
    elif dataWeb['3'] == '0':
        ledControl ('F')
    if dataWeb['4']  == '1':
        ledControl ('G')
    elif dataWeb['4'] == '0':
        ledControl ('H')
    time.sleep (1)
