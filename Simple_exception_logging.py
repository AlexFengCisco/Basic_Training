'''
Created on Mar 3, 2017

@author: AlexFeng
'''
import time
import logging



logging.basicConfig(filename='Simple_exception.log',level=logging.DEBUG)



try: 
    print 'try...' 
    r = 10 / 0 
    print 'result:', r 
except ZeroDivisionError, e: 
    print 'except:', e 
    timer=time.strftime("%A, %d %b %Y %H:%M:%S +0000")
    
    logging.error(timer+"--"+e[0])
    logging.debug(timer+"--"+'Debug detail  message ......')
    time.sleep(2)
    logging.warning(time.strftime("%A, %d %b %Y %H:%M:%S +0000")+"--"+'Warning message too.....')
    
finally: 
    print 'finally...' 
print 'END'
