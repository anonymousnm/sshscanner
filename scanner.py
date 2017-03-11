print ("ssh bot net scanner")

type = raw_input("""
1. scan random ips
>>""")
from colorama import Fore, Back, Style
import colorama
import datetime
import netaddr
import os
import pexpect
import random
import re
import socket
import sys
import time
import threading
from threading import Thread
from colorama import init
from time import sleep
init()
if type == "1":
 timeout = input("enter your time out:: ")
 def scann ():
  
  import random
  while 1:
   ip = ".".join(map(str, (random.randint(0, 255) 
                          for _ in range(4))))

   sock = socket.socket()
   sock.settimeout(timeout)
   try:
       sock.connect((ip, 22))	  
   except socket.error:
         pass
   else:
    print(ip)
 thread = Thread(target = scann) 
 thread1 = Thread(target = scann) 
 thread2 = Thread(target = scann) 
 thread3 = Thread(target = scann) 
 thread.start()
 time.sleep(1)
 thread1.start()
 time.sleep(.1)
 thread2.start()
 time.sleep(.3)
 thread3.start()
 for i in range(300):
    threads = []
    t = threading.Thread(target=scann)
    threads.append(t)
    t.start()
 
	 
 
     

   
 