import threading
from time import sleep

stopAllThread = False

def printSomething(txt):
  while not stopAllThread:
    print(txt)
    sleep(1)

def main():
  global stopAllThread

  t1 = threading.Thread(target=printSomething, args=("Hello World",))
  t2 = threading.Thread(target=printSomething, args=("Hello Meow",))

  t1.start()
  t2.start()

  while not stopAllThread:
    user_input = input("Do you want to stop the thread [y/n] : ")
    if user_input == "y":
      stopAllThread = True

  t1.join()
  t2.join()
      
main()
print("Stopped all threads!")