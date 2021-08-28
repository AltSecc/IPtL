
#Basics
import os,requests
from time import sleep
Exit = ("os.exit")
Quit = ("quit()")



#Update System (DONT DELEATE)
Version = 1.0
r = requests.get('https://raw.githubusercontent.com/AltSecc/IPtL/main/Version.txt')
if '1.0' in r.text:
    print (f'Version {Version}')
else:
    print ('Update needed (https://github.com/AltSecc/IPtL)')
    quit('Killing Process')


#Script
print(" 1=Port Scanner|2= Pinger|3=Ip Info|4= ")
Q=input('What Script: ')

if Q == '0':
  print('Really?')
else:
  if Q == '1':
    os.system ("cd Scripts/ && python3 PScan.py")
    Exit
  else:
    if Q == '2':
      os.system ("cd Scripts/ && python3 Ping.py")
    Exit
    if Q == '3':
      os.system ("cd Scripts/ && python3 ip2info.py")
    Exit
    if Q == '4':
      os.system ("cd Scripts/ && python3 ")
    Exit
