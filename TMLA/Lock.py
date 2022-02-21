from multiprocessing import Semaphore
from threading import Thread, Lock, Semaphore
import time

count = 0
lock = Lock()
semaphore = Semaphore(2)

def inc_count():
    global count
    for _ in range(1000):
        with lock:  # не будет такого что в этот блок кода зайдет два потока
            count += round(sum([1/10000]*10000))   

        #pass
        #lock.acquire()
        #with lock:
            #pass
           # pass  
        #lock.release()
        #pass
        
ths = [Thread(target = inc_count) for _ in range(10)]
[th.start() for th in ths]
[th.join() for th in ths]

print(count)