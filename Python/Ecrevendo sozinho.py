#import libs
import time
import sys
 #function whe write alone
def writeAlone(message):
    for letter in message:
        sys.stdout.write(letter)
        time.sleep(0.5)

#call function
msg = 'Helo World'
writeAlone(msg)