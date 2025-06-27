#%%
import numpy as np
import pandas as pd
from tqdm import tqdm
import schedule
import datetime as dt
import time
# import hankook_api
# import db_control
# import ml_model
# import krx_update
# import portfolio
import telegram_api
telegram_api.get_messages()
import chatgpt


import importlib as imp
imp.reload(telegram_api)


def add_time(t, timedelta):
    return (dt.datetime.combine(dt.datetime(2000, 1, 1).date(), t) + timedelta).time()

def add_minutes(t, mins=0):
    return add_time(t, dt.timedelta(minutes=mins))

trading_end_time = dt.datetime.now().replace(hour=15, minute=0, second=0, microsecond=0).time()
all_end_time = dt.datetime.now().replace(hour=15, minute=30, second=0).time()

#%%



#%%
# hankook_api.get_mins_range("397880", -1, 389)

# #%%
# ticker_names = krx_update.update_ticker_names()
# tickers = sorted(ticker_names)
# #%%
# ticker_names = krx_update.update_ticker_names()
# tickers = sorted(ticker_names)

# for ticker in tqdm(tickers):   
#     for tindex in range(0, 390, 30):
#         clip = hankook_api.get_mins(ticker, open_times[tindex + 29])
#         db_control.update_min_clip(clip)



#%%
#3초마다 해야될 일
#비상정지
#telegram에서 메시지를 받은 경우에 비상정지.
quit = False
def telegram_routine():
    messages = telegram_api.get_messages()
    for m in messages:
        m = m.strip()
        #init
        #모든 스케쥴을 멈추고 포트폴리오도 전부 날린다.
      
        if m == 'ping':
            telegram_api.send('ping done.')
        elif m == 'break':
            telegram_api.send('got break....')
            global quit
            quit = True
        elif m == 'clr' or m == 'clear':
            chatgpt.qas = []
            telegram_api.send('chat clear done.')
        else:
            res = chatgpt.talk(m)
            telegram_api.send(res)


schedules = []





schedule.clear()
# schedule.every().day.at("09:03:00").do(morning_routine)
# schedule.every().day.at("15:40:00").do(evening_routine)
schedule.every(0.5).seconds.do(telegram_routine)
telegram_api.get_messages()# must run once to clear all messages
telegram_api.send('NEW PROCESS - ' + dt.datetime.now().strftime("%m-%d %H:%M:%S"))
print("started.")

today = dt.datetime.now().date()
now = dt.datetime.now().time().replace(microsecond=0)

while not quit:
    schedule.run_pending()
    time.sleep(2)

telegram_api.send('STOP')
