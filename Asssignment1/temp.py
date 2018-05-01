# pylint: disable=no-member
import cv2
import numpy as np
import matplotlib

key1=cv2.imread(r'..\ML2018_410421230\Asssignment1\keys\key1.png',0)
key2=cv2.imread(r'..\ML2018_410421230\Asssignment1\keys\key2.png',0)


cv2.namedWindow('key1',cv2.WINDOW_AUTOSIZE)
cv2.imshow('key1',key1)

cv2.namedWindow('key2',cv2.WINDOW_AUTOSIZE)
cv2.imshow('key2',key2)

k=cv2.waitKey(0)
cv2.destroyAllWindows()
