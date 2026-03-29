import time
import os
import datetime

while True:
    print("Run at:", datetime.datetime.now())

    result = os.system("python predict.py")

    if result == 0:
        print("Status: SUCCESS")
    else:
        print("Status: FAILED")

    print("------")

    time.sleep(3600)   # 1 hour