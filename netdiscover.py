#!/usr/bin/env python
from scapy.all import srp, ARP, Ether
from subprocess import call
from requests import get 
from termcolor import cprint
from netifaces import gateways, AF_INET

class Scanner():
    def __init__(self):
        call(['clear'])
        self.printLogo()
    
    def setIP(self,ip):
        self.ip = ip
        
    def printLogo(self):
        cprint("""
 
  _   _      _                      _      ____                                  
 | \ | | ___| |___      _____  _ __| | __ / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ / \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |\  |  __/ |_ \ V  V / (_) | |  |   <   ___) | (_| (_| | | | | | | |  __/ |   
 |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\ |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                                 
                                                                                 
               ""","red")
        
    def scan(self):
        try:
            arpRequest = ARP()
            broadcast = Ether()
            arpRequestBroadcast = broadcast / arpRequest
            arpRequestBroadcast.pdst = self.ip
            arpRequestBroadcast.dst = "ff:ff:ff:ff:ff:ff"
            cprint('[*] Scanning Network', 'yellow')
            answeredList = srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
            clientList = []
            for element in answeredList:
                macVendor = self.findVendor(element[1].hwsrc)
                clientDict = {'ip':element[1].psrc,'mac':element[1].hwsrc,'mac_vendor':macVendor}
                clientList.append(clientDict)
            cprint('[+] Network is scanned','green')
            return clientList
        except KeyboardInterrupt:
            cprint("\n\n[-] CTRL + C | Program is disabled",'red')
            exit()
        except PermissionError:
            cprint("\n\n[-] Permission denied",'red')
            exit()
    def findGateway(self):
        try:
            gtw = gateways()
            defaultGateway = gtw['default'][AF_INET][0]
            return defaultGateway
        except KeyboardInterrupt:
            cprint("\n\n[-] CTRL + C | Program is disabled",'red')
    def findVendor(self,mac):
        try:
            baseUrl = 'https://api.macvendors.com/'
            macVendor = get(baseUrl + mac).text
            if 'errors' in macVendor:
                macVendor = 'Not Found'
            return macVendor
        except KeyboardInterrupt:
            cprint("\n\n[-] CTRL + C | Program is disabled",'red')
    
    def printResult(self,resultList):
        try:
            cprint("\n\nIP\t\t\tMAC Address\t\t\tMAC Vendor\n",'yellow',end="")
            print('-'*100)
            for client in resultList:
                print(f"{client['ip']}\t\t{client['mac']}\t\t{client['mac_vendor']}")
        except KeyboardInterrupt:
            cprint("\n\n[-] CTRL + C | Program is disabled",'red')

if __name__ == '__main__':
    try:
        scanner = Scanner()
        defaultGateway  = scanner.findGateway()
        ip = input(f'Enter IP or Network Address you want to scan: [Default network: {defaultGateway}] ')
        if ip == '':
            ip = defaultGateway + '/24'
        scanner.setIP(ip)
        clientList = scanner.scan()
        scanner.printResult(clientList)
    except KeyboardInterrupt:
        cprint("\n\n[-] CTRL + C | Program is disabled",'red')
        
        
                        
        
