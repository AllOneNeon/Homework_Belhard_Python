from threading import Thread
import time

count = 0

def inc_count():
    global count
    for _ in range(1000):
        #tmp = count
        #time.sleep(0)
        #count += int(sum([1/1000]*1000))
        count += round(sum([1/10000]*10000))   
        #tmp += 1
        #count = tmp

ths = [Thread(target = inc_count) for _ in range(10)]
[th.start() for th in ths]
[th.join() for th in ths]

#for th in ths:
 #   th.start() 
#for th in ths:
 #   th.join()

print(count)
