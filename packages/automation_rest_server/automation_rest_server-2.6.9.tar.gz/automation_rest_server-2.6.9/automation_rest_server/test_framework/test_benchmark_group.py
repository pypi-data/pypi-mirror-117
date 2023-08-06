# coding=utf-8
# pylint: disable=unused-variable
import yaml
import time
import random
import string
from multiprocessing import Queue
from tool.fio.fio import Fio
from utils.process import MyProcess
from utils.system import decorate_exception
from test_framework.state import State


class TestBenchmarkGroup(object):

    def __init__(self):
        self.process_run_ = None
        self.results = list()

    @staticmethod
    def generate_group_key():
        time_string = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        key = "{}_{}".format(time_string, code)
        return key

    def _run(self, test_name, test_parameters, queue):
        try:
            ret = State.PASS
            fio = Fio()
            group_key = self.generate_group_key()
            for item in test_parameters:
                item["group_key"] = group_key
                status, out_put, result = fio.run_benchmark(item)
                ret = State.PASS if status == 0 else State.FAIL
            result = {"name": test_name, "result": ret, "msg": "out_put", "benchmark_result": ""}
            queue.put(result)
        except Exception as e:
            print(e)
            result = None
        return result

    def run(self, test_name, test_parameters):
        queue = Queue()
        self.process_run_ = MyProcess(target=self._run, args=(test_name, test_parameters, queue, ))
        self.process_run_.start()
        self.process_run_.join()
        value = queue.get(True)
        self.results.append(value)
        return self.results

    def stop(self):
        print("TestBenchmark runner . stop")
        if self.process_run_ is not None:
            ret = self.process_run_.stop()
        else:
            ret = -1
        return ret


if __name__ == '__main__':
    a = TestGroupBenchmark()
    queue = Queue()
    a._run("test", queue)
