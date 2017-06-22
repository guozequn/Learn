#-*- coding:utf-8 -*-


import os, time, random
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue

def run_proc(words):
    print('Run child process %s (%s)...' % (words, os.getpid()))


def long_time_task(words):
    print('Run task %s (%s)..' % (words, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %.2f seconds' % (words, end - start))

def write(queue):
    print('Process to write: %s' % os.getpid())
    for x in range(100):
        queue.put(x)
        print('%s has put to the queue' % x)
        time.sleep(random.random())

def read(queue):
    print('Process to read: %s' % os.getpid())
    while True:
        value = queue.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    #print('Parent process %s.' % os.getpid())
    #p = Process(target=run_proc, args=('test',))
    #print('child process start')
    #p.start()
    #p.join()
    #print('child process ended')

    #print('Parent process %s.' % os.getpid())
    #p = Pool(4)
    #for i in range(5):
    #    p.apply_async(long_time_task, args=(i,))
    #print('waiting for all subprocess dons..')
    #p.close()
    #p.join()
    #print('All process done.')

    # normal
    #queue = Queue()
    #pw = Process(target=write, args=(queue,))
    #pr = Process(target=read, args=(queue,))
    #pw.start()
    #pr.start()
    #pw.join()
    #pr.terminate()
    # junior failed 
    #queue = Queue()
    #p = Pool(4, write, (queue,))
    #pr = Process(target=read, args=(queue,))
    #p.apply_async(write)
    #pr.start()
    #p.close()
    #p.join()
    #pr.terminate()
