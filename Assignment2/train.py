import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from sklearn.decomposition import PCA

(x_train,y_train),(x_test,y_test)=mnist.load_data()

#print(type(x_train))

def showimg(img):   #img=x_train[0]
    print(img.shape)
    if(img.shape[0]==200):
        img=img.reshape(10,20)
        print(img.shape)
    plt.imshow(img,cmap=plt.cm.gray)
    plt.show()

x_train=x_train.reshape((60000,28*28)).astype("float32")/255 #normalization
x_test=x_test.reshape(10000,28*28).astype("float32")/255

pca=PCA(200,True,True)
x_train=pca.fit_transform(x_train)
x_test=pca.transform(x_test)

print(x_train.shape,x_test.shape)

#showimg(x_train[0])


y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)