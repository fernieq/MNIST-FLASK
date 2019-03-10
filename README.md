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

1. Install and run Cassandra(download page: https://hub.docker.com/_/cassandra)

	docker run --name some-cassandra -p 9042:9042 -d cassandra:latest

2⃣️ Connect the Cassandra with the Flask container

	docker run -it --link some-cassandra:cassandra --rm cassandra cqlsh cassandra



### 3. Read data from Cassandra

use mnist_database

select * from mnist1

## mnisk-flask
