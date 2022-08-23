import os 
import sys
import time
import json
import random
import subprocess as sub
import re
import time
Logo = """
 _______   _______      ___       __    __  .___________. __    __      __           ___      .__   __.  _______  .___  ___.  __  .__   __.  _______ 
|       \ |   ____|    /   \     |  |  |  | |           ||  |  |  |    |  |         /   \     |  \ |  | |       \ |   \/   | |  | |  \ |  | |   ____|
|  .--.  ||  |__      /  ^  \    |  |  |  | `---|  |----`|  |__|  |    |  |        /  ^  \    |   \|  | |  .--.  ||  \  /  | |  | |   \|  | |  |__   
|  |  |  ||   __|    /  /_\  \   |  |  |  |     |  |     |   __   |    |  |       /  /_\  \   |  . `  | |  |  |  ||  |\/|  | |  | |  . `  | |   __|  
|  '--'  ||  |____  /  _____  \  |  `--'  |     |  |     |  |  |  |    |  `----. /  _____  \  |  |\   | |  '--'  ||  |  |  | |  | |  |\   | |  |____ 
|_______/ |_______|/__/     \__\  \______/      |__|     |__|  |__|    |_______|/__/     \__\ |__| \__| |_______/ |__|  |__| |__| |__| \__| |_______|
                                                                                                                                                     

"""
Attacked = []
def LoadFile():
    f = open("data.json")
    filejson = json.load(f)
    for x in filejson:
        Data = x['BSSID']
        Attacked.append(Data)
os.system("cls || clear")
print(Logo)
if os.geteuid() != 0:
    print("[Err] You must be root/sudo user to execute this python script.\nAlso make sure you have monitor/promiscuous mode ENABLED!!!")
    exit()
p = sub.Popen(('sudo','python','__dump.py'), stdout=sub.PIPE)
while True:
    time.sleep(1)
    os.system('cls || clear')
    print(Logo)
    print(f"Active DeAuthentication Targets: " + str(Attacked), end="\r")
    Attacked = []
    LoadFile()
    

