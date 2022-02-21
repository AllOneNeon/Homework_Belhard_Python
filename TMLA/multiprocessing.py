from multiprocessing import Process #что-то тут не так выдает ошибкун а этой линии
import time

def process(array):
    for item in array:
        item**item

if __name__ == '__main__':
    huge_list = [10_000] * 4_000
    start_time = time.time()
    #process(huge_list)

    th1 = Process(target=process, args=huge_list[:2000],)
    th2 = Process(target=process, args=huge_list[2000:],)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(time.time() - start_time)