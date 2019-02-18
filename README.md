Logs Analysis\
Author: Andrew Bageant\
Last Updated: 2019-02-17\

# Introduction

This script is designed to be run in Python 2.7 on a virtual machine running
Ubuntu 16.04. The preferred setup is a VirtualBox VM, managed via Vagrant.
To learn more about the specific Vagrant/VirtualBox setup used here, you
can look at the following repo from Udacity's GitHub:
https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile

This script uses the following Python packages:
psycopg2

# Database Setup
This script analyzes the data in the news SQL database and provides answers to
three specific questions.

The news.sql database can be found here:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
Prior to running this file, it will need to be composed in psql with
the following command:
psql -d news -f newsdata.sql

A brief summary of the data:
The authors table has a row for each of the article authors. It also contains
some basic information about each author, including his or her id number.

The articles table contains a row for every article, as well as some core
information about that article. This includes the author id and the articles
path on the website (as 'slug').

The log table contains a row for each time a viewer attempted to access the
website. It includes the path they attempted to access, as well as the
status code they received in response (indicating whether an error
occurred).

To learn more about each of these tables, you can use the \d "table name"
command in psql.

# Running the Code
To run the code, first use Vagrant to SSH into a virtual machine like the
one described in the introduction. Then, run the following:
$ python log_analysis.py

Alternatively, you can run
$ chmod +x log_analysis.py
and then run the script with
./log_analysis.py

# Output
The following three questions are answered in the ouptput of log_analysis.py:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Upon the execution of log_analysis.py, the answers to these questions
(in this order) are written to the file output.txt.
