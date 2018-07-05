import keras
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.datasets import mnist
from sklearn.decomposition import PCA
from keras.models import Sequential
from keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten
from keras.layers.advanced_activations import LeakyReLU
from keras.optimizers import Nadam

import win_unicode_console
win_unicode_console.enable()

(x_train,y_train),(x_test,y_test)=mnist.load_data()

#print(type(x_train))

def showimg(img):   #img=x_train[0]
    print(img.shape)
    if(img.shape[0]==200):
        img=img.reshape(10,20)
        print(img.shape)
    plt.imshow(img,cmap=plt.cm.gray)
    plt.show()

#x_train=x_train.reshape(60000,28*28).astype("float32")/255 #normalization
#x_test=x_test.reshape(10000,28*28).astype("float32")/255

x_train=x_train.reshape(60000,784).astype("float32")/255 #normalization
x_test=x_test.reshape(10000,784).astype("float32")/255


pca=PCA(256,True,True)
x_train=pca.fit_transform(x_train)
x_test=pca.transform(x_test)

x_train=x_train.reshape((60000,256,1,1))
x_test=x_test.reshape(10000,256,1,1)

print(x_train.shape,x_test.shape)

#showimg(x_train[0])

y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)

# 自動增長 GPU 記憶體用量
gpu_options=tf.GPUOptions(allow_growth=True)
sess=tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
# 設定 Keras 使用的 Session
tf.keras.backend.set_session(sess)

model=Sequential()
model.add(Conv2D(16, kernel_size=(5,5), activation='relu',input_shape=(256,1,1),padding='same'))
model.add(LeakyReLU(alpha=.3))
model.add(Dropout(0.25))
#model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=Nadam(),
              metrics=['accuracy'])

train_history = model.fit(x_train, y_train,
                    batch_size=128,
                    epochs=15,
                    verbose=1,
                    validation_data=(x_test, y_test))
score=model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
