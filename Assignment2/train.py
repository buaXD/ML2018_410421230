import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from sklearn.decomposition import PCA

(x_train,y_train),(x_test,y_test)=mnist.load_data()

'''
img=x_train[0]
plt.imshow(img,cmap=plt.cm.gray)
plt.show()
'''

x_train=x_train.reshape(60000,28*28).astype("float32")/255
x_test=x_test.reshape(10000,28*28).astype("float32")/255

x_train/=255    #normalization
x_test/=255

print(x_train.shape)

pca=PCA(200,True,True)
x_train=pca.fit_transform(x_train)
x_test=pca.transform(x_test)

print(x_train.shape)


#print(x_train.shape,x_test.shape)