# Item Catalog Project
Project of Full Stack Web Development Udacity Nanodegree.

The task in this project is to develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. 

Registered users will have the ability to post, edit and delete their own items.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

What things you need to install the software and how to install them

- Vagrant 1.8.5. Follow the steps from here: https://howtoprogram.xyz/2016/07/23/install-vagrant-ubuntu-16-04/
- Virtualbox 5.0. Download and install from here: https://www.virtualbox.org/wiki/Download_Old_Builds_5_0

### Installing
1. In command line write **git clone** and the url of the project.
2. Go to the main folder where is the Vagrantfile and write **vagrant up** to start the VM.
3. Once the machine is setted, write **vagrant ssh** and you will be in the **vagrant@vagrant:**


### Configure database

1. To configure and populate the database, **cd /vagrant/Item\ Catalog\ Project/**
2. Run **python database_setup.py**
3. Run **python lotsofcatalogs.py**

### Running application

Once the vagrant machine is up and the database is setted, do the following steps:

1. Run **python project.py**
2. Go to your web browser and enter ***http://localhost:8000/***

