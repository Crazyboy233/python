""""
该文件含有两版线程池。
注：该线程池只为初学者学习使用，在工程项目中，一般使用标准库
"""

"""
下面为初学者版本
"""
import threading
import queue
import time

class SimpleThreadPool:
    def __init__(self, theadnums):
        self.threads = []           # 用于存放每个worker
        self.tasks = queue.Queue()  # 用于存放任务的队列,任务应该是 func，args
        self.stop_signal = object() # 哨兵信号

        for i in range(theadnums):
            t = threading.Thread(target=self.worker, name=f"worker-{i}")
            t.start()
            self.threads.append(t)

    def worker(self):
        while True:
            task = self.tasks.get()
            if task is self.stop_signal:
                break
            
            func, args = task
            try:
                func(*args)
            except Exception as e:
                print("任务异常", e)
            finally:
                self.tasks.task_done()

    # 将任务加到任务队列
    def submit(self, func, *args):
        self.tasks.put((func, args))    # 这里不关心谁来执行任务，只负责将任务入队

    def shutdown(self):
        for _ in self.threads:
            self.tasks.put(self.stop_signal)    # 像每个线程投递一个停止信号

        # 等待所有线程执行完毕
        for t in self.threads:
            t.join()

# 使用示例
def work(x):
    print(f"处理{x}")
    time.sleep(1)

pool = SimpleThreadPool(3)

for idx in range(6):    # 这里传入6个任务测试
    pool.submit(work, idx)

pool.shutdown()


"""
下面为使用标准库版本
"""

