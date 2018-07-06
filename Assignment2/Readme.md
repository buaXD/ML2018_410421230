[perf]:https://github.com/buaXD/ML2018_410421230/blob/master/Assignment2/Pic/giveup.jpg

# Handwritten Character Recognition

* 一些較特殊的使用：LeakyReLU, Nadam

# 大致流程
* 下載檔案
* resize成適合大小
* 透過PCA降維
* 開始套用sequential model
** 涵蓋


# 遭遇問題
### Data下載
* 不知道為什麼用
```
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')
```
都會跳出
```
ConnectionResetError: [WinError 10054] 遠端主機已強制關閉一個現存的連線。
```
所以嘗試了很多次依然無法成功只好用keras的MNIST Data
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

# 感想
看樣子這個暑假真的要好好搞懂，很多東西都只了解大概，輸入輸出多少都不懂，造成只能硬試看合不合，不過完整靠自己(專案有組員)寫一遍才知道其實自己理解的非常不完全，是個很棒的經驗
