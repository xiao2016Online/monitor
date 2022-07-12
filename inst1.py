import json
from datetime import datetime

import requests


class Inst(object):

    def get_cbh_monitor_data(self):
        print(datetime.now(), "  do  task")
        url = "https://dc27fbe5db49ae18.mgt-cn-north-3.inspurcloud.cn/3.0/authService/config"
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/54.0.2840.99 Safari/537.36",
            "Content-Type": "application/json",
            "Referer": "https://dc27fbe5db49ae18.mgt-cn-north-3.inspurcloud.cn/"
        }
        data = '{"c":{},"b":{}}'
        response = requests.post(url=url, headers=headers1, data=data, verify=False)
        if response.status_code == 200:
            json1 = json.loads(response.text)
            msg = json1.get("msg")
            if msg == '成功':
                print(json1.get("data"))
            else:
                raise Exception('CBH数据异常')
        else:
            raise Exception('CBH数据异常')

    def get_las_monitor_data(self):
        print(datetime.now(), "  do  task")
        url = "https://d653ce8b1d70541e.mgt-jinan-lab.inspurcloud.cn/api/system/health_status"
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/54.0.2840.99 Safari/537.36",
            "Content-Type": "application/json",
        }
        response = requests.get(url=url, headers=headers1, verify=False)
        if response.status_code == 200:
            if response.text == 'success':
                print('success')
            else:
                raise Exception('LAS数据异常')
        else:
            raise Exception('LAS数据异常')
