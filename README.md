## MNIST Flask Demo:

Highlights:
1. We use Keras with a TensorFlow backend to train a small 8 layer CNN to recognize handwritten character digits.
2. We then save the model structure to a json file and weights to a h5 file.
3. We use Flask to load the model and to predict the input handwritten character digits.
4. We save all the input data and output data Casandra.
5. We use HTML to help display the whole process.


### 1. How to run the application：
### We Use Docker! :)

1⃣️Install Docker: https://docs.docker.com/install/overview/

2⃣️Use the following Docker command to build a base image

	docker build -t IMAGE_NAME .

3⃣️Use the following Docker command to build a container and run the image

	docker run -d -p 4000:5000 IMAGE_NAME


### 2. Connect to Apache Cassandra database:

1⃣️Install and run Cassandra(download page: https://hub.docker.com/_/cassandra)

	docker run --name some-cassandra -p 9042:9042 -d cassandra:latest

Note: Pay special attention to that we need to connect port 9042 from the container to a port from our local machine. In this case, we choose 9042 as well.

2⃣️ Connect to Cassandra from cqlsh

	docker run -it --link some-cassandra:cassandra --rm cassandra cqlsh cassandra

Note: It is possible than when you run the above command, your terminal will tell you the following error: (Unable to connect to any servers). The reason is that the Cassandra container has not fully started yet. In order to solve the problem, you just simply re-type the same command and you should be able to connect to Cassandra from cqlsh.


### 3. Read data from Cassandra

use mnist_database

select * from mnist1

## mnisk-flask
