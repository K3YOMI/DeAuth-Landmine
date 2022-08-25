import os 
import sys
import time
import json
import random
import subprocess as sub
import re
import time
CurrentlyTargted = []

def IsMacAddressInLoop(mac):
    f = open("data.json")
    filejson = json.load(f)
    for x in filejson:
        if x['BSSID'] == mac:
            return True
    return False



def _init():
    global CurrentlyTargted
    p = sub.Popen(('tcpdump','-i','wlan0','-vv'), stdout=sub.PIPE)
    for row in iter(p.stdout.readline, b''):
        if "DeAuthentication" in str(row):
            RegExpMacAddress = re.search("[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}", str(row)) # regex to find mac address
            if RegExpMacAddress != None and IsMacAddressInLoop(RegExpMacAddress[0]) == False:
               read_Daa = open('data.json')
               data = json.load(read_Daa)
               data.append({
                    "BSSID": RegExpMacAddress[0],
                    "Time-Last-Seen": time.time()
               })
               read_Daa.close()
               wrote_Data = open('data.json', 'w')
               json.dump(data,wrote_Data, indent=4)
               wrote_Data.close()
        f = open("data.json")
        filejson = json.load(f)
        for x in filejson:
            subs = time.time() - x['Time-Last-Seen']
            if subs >= 1:
                with open('data.json', 'w') as f:
                    f.write("[]")


_init()
