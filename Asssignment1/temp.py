# pylint: disable=no-member
import cv2
import random
import numpy as np
import matplotlib

key1=cv2.imread(r'..\ML2018_410421230\Asssignment1\keys\key1.png',0)
key2=cv2.imread(r'..\ML2018_410421230\Asssignment1\keys\key2.png',0)
inp=cv2.imread(r'..\ML2018_410421230\Asssignment1\I.png',0)
E=cv2.imread(r'..\ML2018_410421230\Asssignment1\E.png',0)

def printbasic():
    cv2.namedWindow('key1',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('key1',key1)
    cv2.namedWindow('key2',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('key2',key2)
    cv2.namedWindow('I',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('I',inp)
    cv2.namedWindow('E',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('E',E)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''start training'''
epoch,limit=1,10
lrate=1e-6

w=[random.random(),random.random(),random.random()]

print(key1.shape)   #[h,w]
print(key1[0,1])    #[h,w]

while epoch<limit:
    for i in range(key1.shape[0]):  #height
        for j in range(key1.shape[1]):  #width
            pass
            temp=E[j,i]-(w[0]*key1[j,i]+w[1]*key2[j,i]+w[2]*inp[j,i])
            


    epoch+=1
    pass

