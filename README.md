# app.mySQL

Photographer's Database
Photographer's Database is a Python application that allows you to manage a database of photographers.

Installation
Before you can run this project, you'll need to install Python and some dependencies.

Prerequisites
Make sure you have Python 3.10 installed on your system. 

Clone the repository
Start by cloning the repository to your local machine:

bash

git clone https://github.com/nlavdaki/app.mySQL.git

Install dependencies
Navigate into the cloned project's directory:

bash

cd app.mySQL
Install the necessary Python dependencies:

pip install flask
pip install flask-mysqldb


Database Setup
This app uses MySQL for the database. You need to setup a MySQL server and create a database that will be used by the app.


After setting up the database, modify the config.py file with your database details.
table of the database:
CREATE TABLE `Photographers` (  `id` int(8) NOT NULL AUTO_INCREMENT,  `name` varchar(15) NOT NULL,  `surname` varchar(30) NOT NULL,  `birthday` date NOT NULL,  `deathday` date NOT NULL,  `cv` varchar(200) NOT NULL,  `created` datetime NOT NULL DEFAULT current_timestamp(),  `updated` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE current_timestamp(),  PRIMARY KEY (`id`),  UNIQUE KEY `id` (`id`) ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci 


To run the application:

python app.py


Once the server is running, you can navigate to http://localhost:5000 in your web browser to access the application's user interface.

