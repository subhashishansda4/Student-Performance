import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = '[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

'''
x = 1000
print([n for n in range(2,x+1) if all(n%i != 0 for i in range(2,n))])

n = 6
print('Prime' if n>1 and all(n%i != 0 for i in range(2, int(n**0.5)+1)) else 'Not Prime')

def prime(n): return not any(n%i == 0 for i in range(2,n))
prime(6)
'''