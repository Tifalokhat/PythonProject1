from multiprocessing import Pool
import os,time

def task(name):
    print(f'子进程的PID:{os.getpid()}，执行的任务：{name}')
    time.sleep(1)

if __name__ == '__main__':
    start=time.time()
    print('父进程开始执行')
    p=Pool(3)
    for i in range(1,11):
        p.apply(func=task,args=(i,))

    p.close()
    p.join()
    print('所有的子进程执行完毕，父进程执行结束')
    print(time.time()-start)