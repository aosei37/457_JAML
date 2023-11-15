import os.path
import time

i = 0

while (i < 18) :
    while (not os.path.isfile("send")) :
        time.sleep(1)
    lis = os.listdir()
    for u in lis :
        if (u != 'coverta.py' and u != 'covertb.py' and u != 'send') :
            os.remove(u)
    os.remove("send")
    i += 1