# PL-125-T2/PL-125-T4 Testscripts
This repository contains testscripts for Voltcraft PL-125-T2 and PL-125-T4 devices.
These were created during development of the connection between both devices and Artisan.
The scripts can be used to determine if the connection to PL-125-T2/T4 devices works or not.

## Usage
```
# If working, the script should output something like this:
# 5000.0 means that there is no sensor connected to T2
$ python3 pl-125-t2/emulator.py 
T1: 23.0 T2: 5000.0
T1: 23.0 T2: 5000.0
...
$ python3 pl-125-t4/emulator.py 
T1: 17.8 T2: 17.8 T3: 19.3 T4: 19.1
T1: 17.8 T2: 17.8 T3: 19.3 T4: 19.0
T1: 17.7 T2: 17.8 T3: 19.3 T4: 19.0
...
```

## Related Projects
* [Artisan](https://github.com/artisan-roaster-scope/artisan)

