import platform
if platform.system() != "Windows":
  exit()
import requests
import time
import urllib3
import wmi

session = requests.Session()
session.trust_env = False
urllib3.disable_warnings()

try:
  uuid = wmi.WMI().Win32_ComputerSystemProduct()[0].UUID
except:
  exit()

def checar() -> None:
  request = session.get('https://pastebin.com/raw/LINK', verify=False)

  if uuid in request.text:
    print("Authorized HWID, redirecting...")
    time.sleep(2.4)
    menu()
  else:
    print("Unauthorized HWID")
    time.sleep(2.4)
    exit()

def menu() -> None:  
  subprocess.run('cls', shell=True)
  print("hi")

if __name__ == '__main__':
  checar()
