# Copyright S.CARLIOZ - 2018
# MIT licence. Use, share, improve, cheers !

"""
TESTS FILE
----------
Run a number of tests to verify (visually) that
everything is working well.
"""

import time

from loadingbar import bars
from loadingbar import background
from loadingbar import indicator


#-----------------------------------------------------
def test_1():
    print("\n")
    print("---- TEST 1 ----")
    print("Standard loading bar, low number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = bars.LoadingBar(SIZE)
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

    lb = bars.LoadingBar(SIZE)
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

    lb = bars.InfoLoadingBar(SIZE)
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

    lb = bars.InfoLoadingBar(SIZE)
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

    lb = bars.VerboseLoadingBar(SIZE)
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

    lb = bars.MessageLoadingBar(SIZE)
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

    lb = bars.MessageLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP, "/temp/usr/{}".format(i))
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_8():
    print("\n")
    print("---- TEST 8 ----")
    print("Percentage loading bar, very low number")

    SIZE = 3
    STEP = 1

    lb = bars.PercentageLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_9():
    print("\n")
    print("---- TEST 9 ----")
    print("Percentage loading bar,  high number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = bars.PercentageLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_10():
    print("\n")
    print("---- TEST 10 ----")
    print("Percentage and info loading bar, very low number")

    SIZE = 3
    STEP = 1

    lb = bars.PercentageInfoLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_11():
    print("\n")
    print("---- TEST 11 ----")
    print("Percentage and info loading bar,  high number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = bars.PercentageInfoLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_12():
    print("\n")
    print("---- TEST 12 ----")
    print("Percentage before loading bar, very low number")

    SIZE = 3
    STEP = 1

    lb = bars.PercentageBeforeLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_13():
    print("\n")
    print("---- TEST 13 ----")
    print("Percentage before loading bar, high number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = bars.PercentageBeforeLoadingBar(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_14():
    print("\n")
    print("---- TEST 14 ----")
    print("Percentage before loading bar + infos, very low number")

    SIZE = 3
    STEP = 1

    lb = bars.PercentageBeforeLoadingBarAndInfo(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()

#-----------------------------------------------------
def test_15():
    print("\n")
    print("---- TEST 15 ----")
    print("Percentage before loading bar + infos, high number")

    SIZE = 10**5 # 100KB
    STEP = 10**4 # 10KB

    lb = bars.PercentageBeforeLoadingBarAndInfo(SIZE)
    for i in range(0, SIZE, STEP):
        lb.update(STEP)
        time.sleep(0.5)
    lb.done()
