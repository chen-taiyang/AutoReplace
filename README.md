# 自动修改GNS3中Cisco配置文件中的IP地址

## 设计初衷

由于考虑到我朋友们“平时忙于各种事情”，没时间配置设备（点名袁某、冯某、程某）。但是作业要求“设备的IP地址有自己的痕迹”，所以我写了一个小玩意。🌹



## 主要功能

自动将所有配置文件中所有配置文件加上“你的痕迹“。



## 如何使用

1. 你需要根据模板拓扑图构建自己的拓扑图（包括接口、设备名）
2. 选择一种模式对config.txt进行修改
3. 运行AutoReplace.exe
4. 将配置文件导入相应的设备中



## 两种修改模式

1. 只修改原配置文件中IP地址的第二位

   这时候你需要在config.txt中输入一个整数（千万不要输自己的**学号**啊！！！）

   ![image-20220901182018595](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901182018595.png)

   > 必须按照这样输入（代码半天赶出来的，有时间慢慢优化，这算训练用户吗？）

   然后运行exe文件你就会发现配置文件中IP地址发生了改变

   假设原本：10.4.1.100 

   ​		修改后：10.2.1.100

   具体有什么用，看你自己悟性了

   

2. 完全修改IP地址

   > 这种模式有点繁琐，建议第一种

   这时候你需要在config.txt中输入以下格式的内容：

   原IP地址->修改后的IP地址   如图所示：

   ![image-20220901182456036](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901182456036.png)

   > 必须按照这样输入（代码一天赶出来的，有时间慢慢优化，这算训练用户吗？）

   注意事项：

   - 修改后的IP需自己规划好
   - 不仅只有接口的地址需要更换还有**路由协议中的网段也需要更换**

   ​      如图所示：红框中为路由协议中的网段

![image-20220901182756512](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901182756512.png)



## 演示

使用GNS3模拟静态路由

#### 拓扑图

![拓扑图模板](https://user-images.githubusercontent.com/107973104/188042039-39d00788-1472-4313-b6b4-64f9c9e8bf1d.png)


> 注意自己将拓扑时结构需和参考拓扑完全一样，包括接口、路由器名称
>
> 路由器名称可以在导入配置后再修改



#### 修改前各设备配置

- PC-1
- ![image-20220901212112672](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901212112672.png)



- PC-2![image-20220901212705735](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901212705735.png)



- R1接口![image-20220901212814358](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901212814358.png)



- R1路由<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901212857640.png" alt="image-20220901212857640" style="zoom:70%;" />



- R2接口<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901213028982.png" alt="image-20220901213028982" style="zoom:70%;" />



- R2路由![image-20220901213111000](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901213111000.png)



- 测试静态路由![image-20220901213252142](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901213252142.png)

------

#### 使用第1种模式（只修改IP地址第二位）

修改config.txt文件![image-20220901213633547](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901213633547.png)

运行AutoReplace.exe，然后将配置文件导入相应的设备

各设备配置情况：

- PC-1![image-20220901214043638](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901214043638.png)



- PC-2![image-20220901214122062](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901214122062.png)



- R1接口<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901214216174.png" alt="image-20220901214216174" style="zoom:70%;" />



- R1路由<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901214258248.png" alt="image-20220901214258248" style="zoom:70%;" />



- R2接口<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901214357534.png" alt="image-20220901214357534" style="zoom:70%;" />



- R2路由<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901214503320.png" alt="image-20220901214503320" style="zoom:70%;" />



- 测试静态路由![image-20220901214604350](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901214604350.png)

------

#### 使用第2种模式（完全修改IP地址）

修改config.txt文件![image-20220901215225662](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901215225662.png)

> 这种模式不是只有接口地址需要替换，还有路由协议中的网段，其中红框部分就是静态路由中的目的网段
>
> 因此建议第1种模式

运行AutoReplace.exe，然后将配置文件导入相应的设备

各设备配置情况：

- PC-1![image-20220901215604071](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901215604071.png)



- PC-2![image-20220901215637327](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901215637327.png)



- R1接口<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901215802807.png" alt="image-20220901215802807" style="zoom:70%;" />



- R1路由<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901215845744.png" alt="image-20220901215845744" style="zoom:70%;" />



- R2接口<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901215936103.png" alt="image-20220901215936103" style="zoom:70%;" />



- R2路由<img src="https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901220015200.png" alt="image-20220901220015200" style="zoom:70%;" />



- 测试静态路由![image-20220901220130142](https://taiyang-pictures-1308391752.cos.ap-nanjing.myqcloud.com/PicGoimage-20220901220130142.png)

------



## 写在最后

- 由于该代码是一下午赶出来的，里面还有很多不足。比如判断用户修改config.txt的内容是否合法

- 每次有新的配置，我都会更新在Github中，目录结构为：

  ```c
  AutoReplace
  │  │  AutoReplace.exe	// 可执行程序
  │  │  AutoReplace.py	// 源码
  │  │
  │  └─staric-router           // 配置名称
  │          config.txt
  │          PC-1_startup.vpc
  │          PC-2_startup.vpc
  │          R1_configs_i1_startup-config.cfg
  │          R2_configs_i2_startup-config.cfg
  │          拓扑图模板.png
  ```

- 你只需要按需修改config.txt文件，然后将AutoReplace.exe拖入到对应配置名称的文件夹中，双击运行即可
- 如果有时间的话，还是希望大家能自己手动敲一敲命令，自己配置一下🌹
