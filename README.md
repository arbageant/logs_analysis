# Logs Analysis
# Author: Andrew Bageant
# Last Updated: 2019-02-16

This script analyzes the data in the news.sql database and provides answers to
three specific questions.

The following three questions are answered in the ouptput of log_analysis.py:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Upon the execution of log_analysis.py, the answers to these questions
(in this order) are written to the file output.txt.


This script is designed to be run in Python 2.7, and uses the following packages:
psycopg2
