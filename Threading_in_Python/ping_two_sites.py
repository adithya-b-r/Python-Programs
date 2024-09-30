import threading
import requests
from time import sleep

def sitePing(url):
  site_response = requests.get(f"https://{url}")
  print(f"Status code of {url} website : {site_response.status_code}\n")
  sleep(1)

## Normal Method would take long time.
# sitePing('google.com')
# sitePing('facebook.com')

t1 = threading.Thread(target=sitePing, args=('google.com',))
t2 = threading.Thread(target=sitePing, args=('facebook.com',))
t3 = threading.Thread(target=sitePing, args=('instagram.com',))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Done Scanning...")