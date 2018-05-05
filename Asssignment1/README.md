## 訓練用圖片
[k1]: https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/keys/key1.png
[k2]: https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/keys/key2.png
[e]:  https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/E.png
[i]:  https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/I.png
[e']:  https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/Eprime.png
[out]:  https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/output.png


***
| K1              | K2              |
| :-------------: | :-------------: |
| ![k1]           | ![k2]           |
 
| I               | E               |
| :------------:  |:--------------: |
| ![i]            | ![e]            |


* epoch limit = 10
* learning rate = 1e-7
* ε = 1e-5

* 經過2個epoch訓練出來的w = [0.2500256045159418, 0.6600628707118442, 0.0900589693848977]

## 用訓練出的W解密相關圖片
| E'              |E'(Decrypted)  |
  | ------------- |------------ |
| ![e']           | ![out]           |


## 心得
因為上學期沒修到人工智慧再加上自己懶惰所以很多基礎相關知識都沒有，像是Gradient Descent，loss是在幹嘛之類的，為了理解那些雖然花了些時間但是仍難尚未完全理解(我太廢了)。而光是要看懂題目也花了快1小時，還不包刮下面的pseudo code，而看懂虛擬碼則是花了快6小時才看懂什麼轉置過來又再轉回去又要再乘1個有轉置的 (而且還是有句想問: ‖𝐰𝑬𝒑𝒐𝒄𝒉−𝐰𝐸𝑝𝑜𝑐ℎ−1‖>𝜖 的外面那兩槓到底是要算矩陣w的行列式還是什麼呢? 經過相關查詢1x1,2x2...的方陣矩陣才可做行列式不是嗎? 可能有什麼相關知識未學到，求指點)。
而之後進度一路順暢直到要看看儲存圖片的時候一直會出現黑點如下圖
![img](https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/dots.png)
