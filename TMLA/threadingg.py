import threading
import time

# def check_notification():
#while True:
    #request(url)
    #time.sleep(1)


def thread_function(name):
    print(f'Thread {name}: starting')
    time.sleep(2)
    print('Pause')
    time.sleep(2)
    print(f'Thread {name}: finishing')

if __name__ == '__main__':
    th1 = threading.Thread(target=thread_function, 
                            args=('thread1',))
    th2 = threading.Thread(target=thread_function, 
                            args=('thread2',))
    print('Before starting')
    th1.start()
    th2.start()
    print('After starting')

    ######
import threading
import time

def process(array):
    for item in array:
        item**item

if __name__ == '__main__':
    huge_list = [10_000] * 4_000
    start_time = time.time()
    process(huge_list)
    print(time.time() - start_time)

   ######
import threading
import time

def process(array):
    for item in array:
        item**item

if __name__ == '__main__':
    huge_list = [10_000] * 4_000
    start_time = time.time()
    #process(huge_list)

    th1 = threading.Thread(target=process, args=huge_list[:2000],)
    th2 = threading.Thread(target=process, args=huge_list[2000:],)
    #th3 = threading.Thread(target=check_notifications, daemon=True)
    #th3.start()
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(time.time() - start_time)