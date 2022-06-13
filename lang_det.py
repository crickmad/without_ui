from langdetect import *
#DetectorFactory.seed = 0
def det():

    print("start")
    j=detect("War doesn't show who's right, just who's left.")
    #h=detect_langs("War doesn't show who's right, just who's left.")
    print(j)
det()