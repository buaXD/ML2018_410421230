# pylint: disable=no-member
import cv2
import random
import numpy as np

key1=cv2.imread(r'..\ML2018_410421230\Asssignment1\keys\key1.png',0)
key2=cv2.imread(r'..\ML2018_410421230\Asssignment1\keys\key2.png',0)
inp=cv2.imread(r'..\ML2018_410421230\Asssignment1\I.png',0)
E=cv2.imread(r'..\ML2018_410421230\Asssignment1\E.png',0)
Eprime=cv2.imread(r'..\ML2018_410421230\Asssignment1\Eprime.png',0)

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

'''
print(key1.shape)   #[h,w]
print(key1[0,1])    #[h,w]
'''
epoch,limit=1,10
epsilon=1e-5
lrate=1e-7

'''start training'''
w=[random.random(),random.random(),random.random()]
store=[]
store.append(w[:])

def checkdet(after,before):             #check(store[epoch-1],store[epoch-2])>epsilon)
    print(after)
    t=np.array([])
    for i in range(len(after)):
        np.append(t,after[i]-before[i])
    return abs(np.linalg.det(t))

def check(after,before):
    temp=0
    for i in range(len(after)):
        if abs(after[i]-before[i])>epsilon:
            temp+=1
    if temp==len(after):
        return 1
    else:
        return 0

print('Original weight is',store)

counting=0

#put w into training
#while epoch<=limit: (testing)
while epoch==1 or (epoch<limit and (epoch>=2 and check(store[epoch-1],store[epoch-2]))):   
    
    for i in range(key1.shape[0]):  #height
        for j in range(key1.shape[1]):  #width
            temp=E[i,j]-(w[0]*key1[i,j]+w[1]*key2[i,j]+w[2]*inp[i,j])
            w[0]+=lrate*temp*key1[i,j]
            w[1]+=lrate*temp*key2[i,j]
            w[2]+=lrate*temp*inp[i,j]
    store.append([w[0],w[1],w[2]])
    epoch+=1
    counting+=1
print('Totally count',counting,'epoch(s)')
ans=[]
ans.append(store[len(store)-1])
print('Best weight is',ans)    #answer w

#out=Eprime.copy()   <-(this will cause encoding problem)
out=np.zeros((300,400),int)

def decryptimg(inpimg,outimg):
    for i in range(Eprime.shape[0]):  #height
        for j in range(Eprime.shape[1]):  #width
            outimg[i,j]=(inpimg[i,j]-ans[0][0]*key1[i,j]-ans[0][1]*key2[i,j])/ans[0][2]
    return outimg

out=decryptimg(Eprime,out)


cv2.imwrite(r'..\ML2018_410421230\Asssignment1\output.png',out,[0])     #store image
out=cv2.imread(r'..\ML2018_410421230\Asssignment1\output.png',0)
cv2.namedWindow('out',cv2.WINDOW_AUTOSIZE)
cv2.imshow('out',out)
cv2.waitKey(0)
cv2.destroyAllWindows()