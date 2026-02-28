from queue import Queue
from threading import Thread
import time

class Producer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for i in range(1,6):
            print(f'{self.name}正在生产第{i}个产品')
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的存放')

class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for i in range(5):
            val=self.queue.get()
            print(f'{self.name}正在消费第{val}个产品')
            time.sleep(1)
        print('消费者完成了所有数据的消费')

if __name__ == '__main__':
    queue=Queue()
    p=Producer('Producer',queue)
    c=Consumer('Consumer',queue)
    p.start()
    c.start()
    p.join()
    c.join()
    print('主线程执行完毕')
