from multiprocessing import Process
import os,time

def sub_process(name):
    print(f'子进程PID:{os.getpid()}，父进程PID:{os.getppid()}，------------{name}')
    time.sleep(1)

if __name__ == '__main__':
    print('父进程开始执行')
    for i in range(5):
        p1=Process(target=sub_process,args=('ysj',))
        p2=Process(target=sub_process,args=(18,))
        p1.start()
        p2.start()

        p1.terminate()
        p2.terminate()

    print('父进程执行完毕')