import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()

img=x_train[0]

plt.imshow(img,cmap=plt.cm.gray)

plt.show()

#print(x_train.shape,x_test.shape)