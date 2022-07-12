from apscheduler.schedulers.blocking import BlockingScheduler

aps = BlockingScheduler(timezone='Asia/Shanghai')


def task(str):
    print(str)


# 特定时间
def date_trigger():
    aps.add_job(func=task, trigger="date", run_date="2022-06-09 15:27:20", args=['张三丰1'])
    aps.start()


# 固定时间
def interval_trigger():
    aps.add_job(func=task, trigger="interval", seconds=20, args=['张三丰1'])
    aps.start()


# cron 表达式
def cron_trigger():
    aps.add_job(func=task, trigger="cron", minute='19-23', second=10, args=['张三丰1'])
    aps.start()


if __name__ == '__main__':
    cron_trigger()
