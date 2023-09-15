import requests
import random
import time
from colorama import Fore
while True:
  user = ""
  r = requests.get(f"https://www.instagram.com/{user}/")
  if {r.status_code == 200}:
    print(Fore.RED + f"[-] :", {user})
  elif {r.status_code == 404}:
    print(Fore.RED + f"[+] or [_] :", {user})
    for charcter in random.choices("abcdefghijklopqrstuwxyz", k=4):
      user = user + charcter
