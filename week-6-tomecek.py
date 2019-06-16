###########################################################
# Written by Karl Tomecek 06/16/2019                      #
# Program Name: week-6-tomecek.py                         #
# Week 6 Assignment                                       #
# Comments:                                               #
#                                                         #
###########################################################

import logging
import logstash
import datetime
import random


def clearScreen():
    for i in range(15): #clear the screen
        print('\n')
        
        
def main():
    clearScreen()
    test_logger = logging.getLogger('python-logstash-logger-tomecek')
    test_logger.setLevel(logging.INFO)
    test_logger.addHandler(logstash.LogstashHandler('54.92.197.249', 5959, version = 1))

    #test_logger.error('python-logstash: test logstash error message.')
    #test_logger.info('python-logstash: test logstash info message.')
    #test_logger.warning('python-logstash: test logstash warning message.')
    
    for i in range(1,10000):
        pickOne = random.randint(1,4)
        if pickOne == 1:
            print('round', pickOne)
            test_logger.error('index: ' + str(pickOne + random.randint(1,500))) #send output to log
        elif pickOne == 2:
            today = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(today) #send output to screen
            test_logger.info('date: '+ str(today)) #send output to log
        else:
            randnum = random.randint(1,100)
            print('Just some random number:',randnum) #send output to screen
            test_logger.warning('rand num: ' + str(randnum)) #send output to log

main()
    