## MNIST Flask
![image](https://github.com/johnli-zr/mnist-flask/blob/master/ezgif-4-97402aa376b6.gif)

Highlights:
1. We use Keras with a TensorFlow backend to train a small 8 layer CNN to recognize handwritten character digits.
2. We then save the model structure to a json file and weights to a h5 file.
3. We use Flask to load the model and to predict the input handwritten character digits.
4. We save all the input data and output data Casandra.


### 运行方式：
#### 一、运行app.py
 1.本地运行
 
 1⃣️安装必要的环境：
 
 sudo pip install -r requirements.txt
 
 2⃣️运行：
 
 python app.py
 
 2.虚拟环境

1⃣️下载virtualenv，并构建虚拟环境，见：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000

2⃣️进入虚拟环境后按照本地安装的步骤

3.使用docker

1⃣️安装docker，docker入门见：https://docs.docker.com/install/overview/

2⃣️使用docker创建一个image

docker build -t IMAGE_NAME .

3⃣️运行该image

docker run -d -p 4000:5000 IMAGE_NAME


### 二、连接cassandra

1⃣️运行cassandra（见：https://hub.docker.com/_/cassandra/

（🌟🌟🌟如果上述步骤运行失败，建议先走这一步，再运行）

docker run --name some-cassandra -p 9042:9042 -d cassandra:latest

2⃣️将你创建的cassandra容器与程序中创建的容器进行连接并删除（）

docker run -it --link some-cassandra:cassandra --rm cassandra cqlsh cassandra



### 三、查看cassandra中存储的数据

use mnist_database

select * from mnist1


# mnisk-flask
