import requests
from desktop_notifier import DesktopNotifier #DN working better than notify
import time
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

sg = 'SafeGasPrice'
pg = 'ProposeGasPrice'
fg = 'FastGasPrice'

while(1):

    hourlyPrices = []
    i = 0

    while(1):#i < 8):
        #i+=1

        response = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=MFPDKXM1QN5MN5S8ZSZWZ5P7NKNMWB2W7B')
        try:
            print(response.status_code)
            json = response.json()

            safe = int(json['result'][sg])
            propose = int(json['result'][pg])
            fast = int(json['result'][fg])

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            hourlyPrices.append([safe, propose, fast, current_time])

            notify = DesktopNotifier()
            print(fast)

            if fast < 80:
                notify.send_sync(title="GO BUY RIGHT NOW!", message="Fast price is at " + str(fast) + "gwei")
                print(fast)
            """
            elif propose < 110:
                notify.send_sync(title="Buy now!", message="Network not cluttered and prices are low! " + str(propose) + "gwei")
            elif safe < 120:
                notify.send_sync(title="Go Buy!", message="Prices are looking good! " + str(safe) + "gwei")
            """
            time.sleep(10)  # 2hours
            # time.sleep(2)
        except:
            print(response.status_code)
            if response.status_code >= 300 and response.status_code < 400:
                print("300 error")
            elif  response.status_code >= 400 and response.status_code < 500:
                print("400 error")
            else:
                print("server error")




"""
    min = 10000
    minTime = None
    max = 0
    maxTime = None
    #max = max(hourlyPrices)
    #min = min(hourlyPrices)

    for prices in hourlyPrices:
        for n in range(2):
            if prices[n] < min:
                min = n
                minTime = prices[3]
            if prices[n] > max:
                max = n
                maxTime = prices[3]

    x = np.array([j for j in range(1, len(hourlyPrices)+1)])
    y = np.array([k[0] for k in hourlyPrices])

    plt.plot(x,y)
    plt.xlabel("Reading Number")
    plt.ylabel("Price (Gwei)")

    plt.show()

    print("Highest of the day was " + str(max) + " at " + str(maxTime))
    print("Lowest of the day was " + str(min) + " at " + str(minTime))

    today = date.today()
    file = open("prices.txt", "a")
    file.write(str(today) + "\nHigh: " + str(max) + "\nLow: " + str(min) + "\n\n")
"""
