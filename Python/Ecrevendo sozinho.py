#import libs
import time
 #function whe write alone
def writeAlone(message):
    for letter in message:
        print(letter,end='')
        time.sleep(0.4)

#call function
msg = 'Helo World'
writeAlone(msg)