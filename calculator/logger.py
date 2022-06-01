from datetime import datetime as dt
from time import strftime

def data_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.py', 'a') as file:
        file.write('{}; result ;{}\n'
                    .format(time, data))
