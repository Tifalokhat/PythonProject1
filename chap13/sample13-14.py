from threading import Thread

a=100
def add():
    print('加线程开始执行')
    global a
    a+=30
    print(f'a的值为：{a}')
    print('加线程执行完毕')

def sub():
    print('减线程开始执行')
    global a
    a-=50
    print(f'a的值为：{a}')
    print('减线程执行完毕')

if __name__ == '__main__':
    print('主线程开始执行')
    print(f'----------a的值为：{a}')
    t1=Thread(target=add)
    t2=Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'a的值为：{a}')
    print('主线程执行完毕')