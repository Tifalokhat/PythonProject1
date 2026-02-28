from multiprocessing import Queue

if __name__ == '__main__':
    q=Queue(3)
    print('队列是否为空：',q.empty())
    print('队列是否已满：',q.full())
    q.put('hello')
    q.put('world')
    print('队列是否为空：',q.empty())
    print('队列是否已满：',q.full())
    q.put('python')
    print('队列是否为空：',q.empty())
    print('队列是否已满：',q.full())
    print('队列当中信息的个数：',q.qsize())

    print(q.get())
    print('队列当中信息的个数：',q.qsize())

    q.put_nowait('html')
    # q.put_nowait('sql')
    # q.put('sql')

    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())

    print('队列是否为空：',q.empty())
    print('队列是否已满：',q.full())
    print('队列当中信息的个数：',q.qsize())