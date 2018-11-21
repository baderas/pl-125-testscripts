#!/usr/bin/python3

# Tests if data connection to PL-125-T4 works
# Author: Andreas Bader (https://github.com/baderas/pl-125-testscripts)

# If working, the script should output something like this:
# $ python3 emulator.py 
# T1: 17.8 T2: 17.8 T3: 19.3 T4: 19.1
# T1: 17.8 T2: 17.8 T3: 19.3 T4: 19.0
# T1: 17.7 T2: 17.8 T3: 19.3 T4: 19.0

import serial
import logging
import signal
from functools import partial
import os
import time
import struct

def exitGracefully(ser, logger, signum, frame):
    if signum != 0:
        logger.info("Captured SIGTERM or SIGINT (%s)." %(signum))
    logger.info("Begin to stop serial connection.")
    values = bytearray([245, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ser.write(values)
    if ser.is_open:
        ser.close()
    logger.info("Stopped serial connection.")
    logger.debug("Exiting now.")
    os._exit(0)

def hex2int(h1,h2=None):
    if h2 is not None:
        return int(h1*256 + h2)
    else:
        return int(h1)

# Configure Logging
logLevel = logging.INFO
#logLevel = logging.DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(logLevel)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logLevel)
logger.addHandler(handler)

comPort='/dev/thermometer'
ser = serial.Serial(
comPort,
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=1,
bytesize=serial.EIGHTBITS,
timeout=0.5,
)

signal.signal(signal.SIGINT, partial(exitGracefully, ser, logger))
signal.signal(signal.SIGTERM, partial(exitGracefully, ser, logger))

def sPrintln(msg,logger,silent=False):
    ser.write(("%s\n" %(msg)).encode())
    ser.flush()
    if not silent:
        logger.info("Sent the following msg: '%s'." %(msg))

while True:
    values = bytearray([244, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ser.write(values)
    data = ser.readline()
    if data == b'':
        continue
    else:
            T1 = hex2int(data[23],data[22])/10.# select byte 19 and 18
            T2 = hex2int(data[25],data[24])/10.# select byte 21 and 20 
            T3 = hex2int(data[19],data[18])/10.
            T4 = hex2int(data[21],data[20])/10.
            print("T1: %s T2: %s T3: %s T4: %s" % (T1, T2, T3, T4))
values = bytearray([245, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
ser.write(values)
os._exit(0)
