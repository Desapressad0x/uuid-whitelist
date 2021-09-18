import os
import requests
import time
import subprocess
import urllib3

session = requests.Session()
session.trust_env = False
urllib3.disable_warnings()

hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
request = session.get('https://pastebin.com/raw/LINK', verify=False)

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("oi")

if hwid in request.text:
   print("HWID autorizado, redirecionando...")
   time.sleep(2.4)
   menu()
else:
   print("HWID não autorizado")
   time.sleep(2.4)
   quit()

if __name__ == '__main__':
  try:
    menu()
  except Exception:
    pass