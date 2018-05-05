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

* 相關參數
```
epoch limit = 10
learning rate = 1e-7 
ε = 1e-5

經過2個epoch訓練出來的w = [0.2500256045159418, 0.6600628707118442, 0.0900589693848977]
```
## 用訓練出的W解密相關圖片
| E'              |E'(Decrypted)  |
  | :-------------: |:-----------: |
| ![e']           | ![out]           |


## 心得
因為上學期沒修到人工智慧再加上自己懶惰所以很多基礎相關知識都沒有，像是Gradient Descent，loss是在幹嘛之類的，為了理解那些雖然花了些時間但是仍難尚未完全理解(~~我太廢了~~)。而光是要看懂題目也花了快1小時，還不包刮提示的pseudo code，而看懂虛擬碼則是花了快6小時才看懂什麼轉置過來又再轉回去又要再乘1個有轉置的 (而且還是有句想問: ‖𝐰𝑬𝒑𝒐𝒄𝒉−𝐰𝐸𝑝𝑜𝑐ℎ−1‖>𝜖 的外面那兩槓到底是要算矩陣w的行列式還是什麼呢? 經過相關查詢1x1,2x2...的方陣矩陣才可做行列式不是嗎? 可能有什麼相關知識未學到，求指點)。
* 遭遇問題  
而之後進度一路順暢直到要看看儲存圖片的時候一直會出現黑點如下圖
![img](https://github.com/buaXD/ML2018_410421230/blob/master/Asssignment1/dots.png)  
而花費將近2天的時間尋找問題所在，畢竟若是在解碼的函式出問題出來的圖片一定會是另類的方式像斜線或是什麼的，因此去嘗試其他的儲存方式從opencv改成PIL或scipy之類的但仍然未解決此現象，所以開始參考同學的程式碼，但仍未有果，直到想放棄，嘗試最後一種方式便不再嘗試了，將原本輸出的圖片從將原本加密後的圖片複製給自己再做運算改成直接把自己變成歸零並用int編碼的array再做運算，沒想到問題竟然解決了。原來一切都是編碼問題，opencv開啟圖片的nparray預設編碼是uint8(0-255)而這次解密的運算要用int比較適合(目前想法)。
* 總結
這次花費的時間總長大約一周算蠻短的，但能然有學到蠻多新東西
