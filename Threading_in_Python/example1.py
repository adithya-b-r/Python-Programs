import threading
from time import sleep

def countNum(n):
  while(n<=10):
    print(n)
    n += 1
    sleep(1)

def tableNum(n):
  count = 1
  while(count<=10):
    print(f"{n} x {count} = {n*count}")
    count += 1
    sleep(1)

t1 = threading.Thread(target=countNum, args=(1,))
t2 = threading.Thread(target=tableNum, args=(4,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done")
