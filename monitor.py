from threading import Thread

import urllib3
import inst
from apscheduler.schedulers.blocking import BlockingScheduler

# 禁止告警
urllib3.disable_warnings()
aps = BlockingScheduler()


def task1():
    # list1 = [inst.get_cbh_monitor_data(), inst.get_las_monitor_data()]
    obj = __import__("inst")
    for item in dir(inst):
        if item.startswith('get'):
            print(item)
            func = getattr(obj, item)
            t = Thread(target=func)
            t.start()


def run_monitor():
    aps.add_job(task1, 'interval', seconds=20)
    aps.start()


if __name__ == '__main__':
    run_monitor()
