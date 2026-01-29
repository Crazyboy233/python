""""
该文件含有两版线程池。
注：该线程池只为初学者学习使用，在工程项目中，一般使用标准库
"""

""""
========================
    下面为初学者版本
========================
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
# 定义任务
def work(x):
    print(f"处理{x}")
    time.sleep(1)

pool = SimpleThreadPool(3)

for idx in range(6):    # 这里传入6个任务测试
    pool.submit(work, idx)

pool.shutdown()


"""
============================
    下面为使用标准库版本
============================
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging

# 配置日志系统
logging.basicConfig(level=logging.INFO)

# 模拟一个会失败的任务
def task(x):
    if x == 3:
        raise ValueError("此时 x == 3, 模拟错误")
    
    time.sleep(1)
    return x

results = []

# 这里使用 with 自动管理线程池的生命周期，with 结束时会自动执行 shutdown(wait=True)
with ThreadPoolExecutor(max_workers=8, thread_name_prefix="worker") as executor:
    futures = {
        executor.submit(task, i):i 
        for i in range(10)  # 这里是提交10个任务
    }

    # as_completed 会在任务完成时按顺序返回 future
    for future in as_completed(futures):
        i = futures[future]
        try:
            # 尝试执行任务
            result = future.result(timeout=2)
            results.append(result)
        except Exception as e:
            # 统一在这里处理异常
            logging.exception(f"任务 {i} 失败")

logging.info(f"完成结果: {results}")

"""
注：上述代码模拟了x=3报错。由于是10个任务，失败1个，成功9个。所以结果应该是 [0, 1, 2, 4, 5, 6, 7, 8, 9]
"""