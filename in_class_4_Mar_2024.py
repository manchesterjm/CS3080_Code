import logging
logging.basicConfig(filename='errorlog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def looper(n):
    for i in range(n+1) :
        print(i)
        
        
looper(20)