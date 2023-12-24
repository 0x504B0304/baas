import logging
import multiprocessing
import os
import threading
import time

import requests
from flask import Flask
from common import process, app, config
from web.baas import baas
from web.configs import configs


def run_flask():
    f = Flask(__name__, static_folder='web/static', static_url_path='/static')
    f.register_blueprint(baas)
    f.register_blueprint(configs)
    ac = config.get_app_config()
    f.run(debug=False, port=ac['port'], host='0.0.0.0')


def check_flask_startup():
    ac = config.get_app_config()
    url = f"http://127.0.0.1:{ac['port']}/ping"
    for i in range(3):
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print("【Baas】启动成功\n请点击打开Baas进入配置页面...")
                break
            print(f"Baas启动失败...当前运行端口为:{ac['port']}")
            print("如果端口冲突可以打开configs/app.txt 修改port 为 7111 或 7112依次类推")
        except Exception as e:
            print(f"Baas启动失败...当前运行端口为:{ac['port']}")
            print("如果端口冲突可以打开configs/app.txt 修改port 为 7111 或 7112依次类推")
            print(e)
        time.sleep(1)


if __name__ == '__main__':
    main_process_pid = os.getpid()
    multiprocessing.freeze_support()

    process.manager = multiprocessing.Manager()
    process.processes_task = process.manager.dict()

    if os.getpid() == main_process_pid:
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        flask_thread = threading.Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()

        check_thread = threading.Thread(target=check_flask_startup)
        check_thread.daemon = True
        check_thread.start()

        app.start()
