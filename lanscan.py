#!/usr/bin/env python

#this program shows the host IP, available network interfaces and scans a target network

import socket
import os
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni


def check(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, 80))
    except socket.error:
        return 0
    else:
        return 1
    sock.close()


class bcolors:
    FAIL = '\033[93m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    ERROR = '\033[31m'
    WHITE = '\033[37m'


interf=raw_input("wlan0(wifi) or eth0(ethernet)?\n")
print("\n")
if interf == "":
    print(bcolors.OKBLUE + "Using wlan0 as default\n" + bcolors.ENDC)
    interf = "wlan0"        #se usuario apenas aperta enter, usa o wlan0

interfaces = ni.interfaces()

if interf in interfaces:    #ve se a interface digitada esta presente
    print(bcolors.OKBLUE + "[*]"+bcolors.ENDC+interf+" available\n")
else:
    print(bcolors.ERROR + "[-]" + bcolors.ENDC + interf +" not available")
    print(bcolors.FAIL + "[*]"+ bcolors.ENDC + "Available interfaces: "),  #se nao, retorn as interfaces disponiveis e sai do programa
    print(interfaces)
    exit()

ip = ni.ifaddresses(interf)[AF_INET][0]['addr']     #ip = ip na interface
print(bcolors.OKGREEN+"[+]"+bcolors.ENDC+"IP address: "+ ip + "\n\n")


ip = ip[0:10]

x=99
for x in xrange(1,255):
        if check(ip+str(x)) == 1:
            print(bcolors.OKGREEN +"[+]"+bcolors.ENDC + "host "+ ip+str(x)+ " online")
        #else:
            #print(bcolors.ERROR +"[-]"+bcolors.ENDC + "host "+ ip+str(x)+ " offline")
#os.system("ping -c 1")
