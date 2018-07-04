import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()

'''
img=x_train[0]
plt.imshow(img,cmap=plt.cm.gray)
plt.show()
'''

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train/=255    #normalization
x_test/=255




#print(x_train.shape,x_test.shape)