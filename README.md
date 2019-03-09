## MNIST Flask
![image](https://github.com/johnli-zr/mnist-flask/blob/master/ezgif-4-97402aa376b6.gif)

Highlights:
1. We use Keras with a TensorFlow backend to train a small 8 layer CNN to recognize handwritten character digits.
2. We then save the model structure to a json file and weights to a h5 file.
3. We use Flask to load the model and to predict the input handwritten character digits.
4. We save all the input data and output data Casandra.
5. We use HTML to help display the whole process.


### How to run the application：
### We Use Docker! :)

1⃣️Install Docker: https://docs.docker.com/install/overview/

2⃣️Use the follwoing Docker command to build a base image

	docker build -t IMAGE_NAME .

3⃣️Use the following Docker command to build a container and run the image

	docker run -d -p 4000:5000 IMAGE_NAME


### 2. Connect to Apache Cassandra database:

1⃣️运行cassandra（见：https://hub.docker.com/_/cassandra/

（🌟🌟🌟如果上述步骤运行失败，建议先走这一步，再运行）

docker run --name some-cassandra -p 9042:9042 -d cassandra:latest

2⃣️将你创建的cassandra容器与程序中创建的容器进行连接并删除（）

docker run -it --link some-cassandra:cassandra --rm cassandra cqlsh cassandra



### 三、查看cassandra中存储的数据

use mnist_database

select * from mnist1


# mnisk-flask
