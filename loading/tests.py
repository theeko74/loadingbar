# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
TESTS FILE
----------
Run a number of tests to verify (visually) that
everything is working well.
"""

import time

import loading_bar
import background
import indicator


#-----------------------------------------------------

print("---- TEST 1 ----")
print("Standard loading bar, low number")

SIZE = 10**5 # 100KB
STEP = 10**4 # 10KB

lb = loading_bar.LoadingBar(SIZE)
for i in range(0, SIZE, STEP):
    lb.update(STEP)
    time.sleep(0.5)
lb.done()

#-----------------------------------------------------

print("---- TEST 2 ----")
print("Standard loading bar, high number")

SIZE = 10**7 # 10MB
STEP = 10**6 # 1MB

lb = loading_bar.LoadingBar(SIZE)
for i in range(0, SIZE, STEP):
    lb.update(STEP)
    time.sleep(0.5)
lb.done()

#-----------------------------------------------------

print("---- TEST 3 ----")
print("Info loading bar, low number")

SIZE = 10**5 # 100KB
STEP = 10**4 # 10KB

lb = loading_bar.InfoLoadingBar(SIZE)
for i in range(0, SIZE, STEP):
    lb.update(STEP)
    time.sleep(0.5)
lb.done()

#-----------------------------------------------------

print("---- TEST 4 ----")
print("Info loading bar, high number")

SIZE = 10**7 # 100KB
STEP = 10**6 # 10KB

lb = loading_bar.InfoLoadingBar(SIZE)
for i in range(0, SIZE, STEP):
    lb.update(STEP)
    time.sleep(0.5)
lb.done()

#-----------------------------------------------------

print("---- TEST 5 ----")
print("Verbose loading bar, low number")

SIZE = 10**5 # 100KB
STEP = 10**4 # 10KB

lb = loading_bar.VerboseLoadingBar(SIZE)
for i in range(0, SIZE, STEP):
    lb.update(STEP, "/temp/usr/{}".format(i))
    time.sleep(0.5)
lb.done()

#-----------------------------------------------------

print("---- TEST 6 ----")
print("Verbose loading bar, low number")

SIZE = 10**7 # 10MB
STEP = 10**5 # 100KB

lb = loading_bar.VerboseLoadingBar(SIZE)
for i in range(0, SIZE, STEP):
    lb.update(STEP, "/temp/usr/{}".format(i))
    time.sleep(0.5)
lb.done()
