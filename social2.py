#!/bin/python3
#import brute_facebook as fb
import brute_email as email
import email_bomber as be
import os
import pas
import brute_vk as vk
import json
import time
import requests
import urllib
import sys
import progressbar
import colorama
from colorama import Fore,Back,Style
from validate_email import validate_email
from os import system
import platform
import os
import time
bar = progressbar.ProgressBar(maxval=30, widgets=[Fore.RESET+'Checking email:',progressbar.Bar(left=Fore.RED+'[', marker=Fore.GREEN+'#', right=Fore.RED+']'),]).start()
key="6bc2663d231ea028c6e6c47debf9151d"
symbols_to_clear=["}","{",",",'"']
colorama.init()
def create_string(output):
 for symbol in symbols_to_clear:
  output=output.replace(symbol,"")
 print(Fore.RED+"////////////////////////////////////////////"+Fore.GREEN+output.upper()+Fore.RED+"////////////////////////////////////////////"+Fore.RESET)
def get_output(num):
 api="http://apilayer.net/api/validate?access_key="+key+"&number=" + num +"&country_code=&format=1"
 return requests.get(api).text
 #return str(requests.get(api)).text()
 #output=information.text
def check_email(email):
 ch=validate_email(email,verify=True)
 if str(ch).lower() == "true":
  return True
 else:
  return False
def check_back(mth):
 print("\n5)Back")
 y=input("<SOCIAL>")
 if y == "5":
  if mth=="info":
   info()
  if mth=="start":
   start()
  if mth=="spam":
   spam() 
 else:
  print(Fore.GREEN+"Ok,Bye...")
  #sys.exit()
def clear():
 system('clear')
def info():
  clear()
  print(banner()+"""\n1) Check mail
2) Verify phone number
3) Generate passwords
4) Get geolocation
5) Back""")
  ask=input("<SOCIAL>")
  if ask == "1":
   clear()
   email=input("Enter email:")
   for x in range(30):
    bar.update(x)
    time.sleep(0.01)
   bar.finish() 
   if check_email(email) == True:
    print(Fore.GREEN+"Email was found!({})".format(email)+Fore.RESET)
    check_back("info")
   else:
    print(Fore.RED+"Email wasn't found!({})".format(email)+Fore.RESET)
    check_back("info")
  elif ask == "2":
   num=input("Enter phone number(with '+'):")
   output=get_output(num)
   create_string(output)
   check_back("info")
  elif ask == "3":
   pas.main()
  elif ask == "4":
   system('./track')
  elif ask == "5":
   start()
  else:
   print(Fore.RED+"Wrong choice"+Fore.RESET)
   time.sleep(0.2)
   info()
def spam():
 clear()
 print(banner()+"""\nStart spamming to:
1) Mobile phone number
2) Email
3) Back""")
 ask=input("<SOCIAL>")
 if ask == "1":
  number=input("Enter phone-number (without Country code number(e.g. +7):")
  th=input("Enter number of threads:")
  country_code=input("Enter country code:")
  system('python3 bomber.py --sms '+th.strip()+' --country '+country_code.strip()+' '+number.strip()) 
 elif ask == "2":
  be.main()
 elif ask == '3':
  clear()
  start()
 else:
  print(Fore.RED+"Wrong choice"+Fore.RESET)
  time.sleep(20)
  spam()
def brute():
 clear()
 print(banner()+"""\n1) Facebook account
2) Instagram account
3) Gmail account
4) VK account 
5) Back""")
 ask=input("<SOCIAL>")
 if ask == "1":
  print("\nSorry, not working anymore")
 elif ask == "2":
  system('./brute_instagram')
 elif ask == "3":
  email.main()
 elif ask == "4":
  vk.main()
 elif ask=="5":
  start()
 else:
  print(Fore.RED+"Wrong choice"+Fore.RESET)
  time.sleep(0.2)
  brute()
def banner():
 banner=Fore.RED+"""                    ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
         ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
        ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
       ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
      ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
     ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
   ▄█ ▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄"""+Fore.RESET
 return banner
def start():
 try:
  clear()
  print(banner()+"""\n
1) Information gathering
2) Spamming
3) Cracking social accounts""")
  ask=input("<SOCIAL>")
  if ask == "1":
   info()
  if ask == "2":
   spam()
  if ask == "3":
   brute()
  else:
   print(Fore.RED+"\nWrong choice"+Fore.RESET)
   time.sleep(0.2)
   start()
 except KeyboardInterrupt:
  print("\nGoodbye...")  
if __name__ == '__main__':
 start()

