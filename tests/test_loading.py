# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
TESTS FILE
----------
Run a number of tests to verify (visually) that
everything is working well.
"""

import time

from loading import loadingbar
from loading import background
from loading import indicator


#-----------------------------------------------------
def test_1():
    print("\n")
    print("---- TEST 1 ----")
    print("Standard loading bar, low number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = loadingbar.LoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_2():
    print("\n")
    print("---- TEST 2 ----")
    print("Standard loading bar, high number")

    SIZE = 10**7 # 10MB
    STEP = 10**6 # 1MB

    lb = loadingbar.LoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_3():
    print("\n")
    print("---- TEST 3 ----")
    print("Info loading bar, low number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = loadingbar.InfoLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_4():
    print("\n")
    print("---- TEST 4 ----")
    print("Info loading bar, high number")

    SIZE = 10**7 # 100KB
    STEP = 10**6 # 10KB

    lb = loadingbar.InfoLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_5():
    print("\n")
    print("---- TEST 5 ----")
    print("Verbose loading bar, low number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = loadingbar.VerboseLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP, "/temp/usr/{}".format(i))
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_6():
    print("\n")
    print("---- TEST 6 ----")
    print("Message loading bar, low number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = loadingbar.MessageLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP, "/temp/usr/{}".format(i))
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_7():
    print("\n")
    print("---- TEST 7 ----")
    print("Message loading bar, very low number")

    SIZE = 3
    STEP = 1

    lb = loadingbar.MessageLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP, "/temp/usr/{}".format(i))
        time.sleep(0.5)
    lb.done()
