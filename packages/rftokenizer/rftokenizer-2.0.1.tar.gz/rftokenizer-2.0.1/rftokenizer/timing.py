#!/usr/bin/python
# -*- coding: utf-8 -*-
# Based on code by Paul McGuire

import atexit
import sys
try:
    from time import clock
except:
    from time import time as clock
from functools import reduce

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(s, elapsed=None):
    #print line
    #print secondsToStr(clock()), '-', s
    if elapsed:
        sys.stderr.write("Elapsed time: " + str(elapsed) + "\n")
    sys.stderr.write(line +"\n")

def endlog():
    end = clock()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

def now():
    return secondsToStr(clock())

start = clock()

atexit.register(endlog)
