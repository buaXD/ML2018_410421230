[perf]:https://github.com/buaXD/ML2018_410421230/blob/master/Assignment2/Pic/giveup.jpg

# Handwritten Character Recognition

* 一些較特殊的使用：LeakyReLU, Nadam

# 遭遇問題
### 降維的使用
* 大致概念不是很清楚
* PCA的套用問題
### 處理維度的輸入
* Conv2D的輸入處理很久
* MaxPooling2D的問題弄很久後時間到了只好先暫時放棄
```
Negative dimension size caused by subtracting 2 from 1 for 'max_pooling2d_1/MaxPool' (op: 'MaxPool') with input shapes: [?,256,1,128]
```
# 最後結果
![perf]


