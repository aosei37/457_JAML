import os.path
import time

monologue = "I need to tell you about all of these top secret things im doing through this covert channel"
message = monologue.split()

for m in message :
    n = open(m, 'x')
    n.close()
    n = open("send", 'x')
    n.close()
    while(os.path.isfile("send")) :
        time.sleep(1)