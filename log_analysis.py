#!/usr/bin/env python

# Source code for logs analysis project
# Author: Andrew Bageant
# Updated 2019-02-17


import psycopg2

# define queries for each question

# find the top 3 most viewed articles
q1 = '''SELECT count, title
    FROM articles INNER JOIN
    (SELECT path, COUNT(path) AS count
    FROM log
    GROUP BY path) AS log
    ON log.path = '/article/' || articles.slug
    ORDER BY count DESC
    LIMIT 3;'''

# order authors by number of views on their articles
q2 = '''SELECT SUM(count) AS count, name
    FROM (SELECT title, slug, name
    FROM articles LEFT JOIN authors
    ON articles.author = authors.id) t2
    INNER JOIN
    (SELECT path, COUNT(path) AS count
    FROM log
    GROUP BY path) t1
    ON t1.path = '/article/' || t2.slug
    GROUP BY name
    ORDER BY count DESC;'''

# find days where the 404 Error response rate exceed
# 1% of total HTTP responses sent
q3 = '''
    SELECT ROUND(sum(bstatus)/(sum(gstatus)+sum(bstatus)),4) AS error_rate,
    TO_CHAR(date,'FMMonth dd, yyyy')
    FROM
    (SELECT time::date AS date, count(status) AS gstatus, NULL AS bstatus
    FROM log
    WHERE status = '200 OK'
    GROUP BY date
    UNION ALL
    SELECT time::date AS date, NULL AS gstatus, count(status) as bstatus
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY date) t1
    GROUP BY date
    HAVING sum(bstatus)/(sum(gstatus)+sum(bstatus)) > 0.01;
    '''

# open connection to "news" database
conn = psycopg2.connect(database="news")
cursor = conn.cursor()

# execute q1 and store it in r1
cursor.execute(q1)
r1 = cursor.fetchall()

# execute q2 and store it in r2
cursor.execute(q2)
r2 = cursor.fetchall()

# execute q3 and store it in r3
cursor.execute(q3)
r3 = cursor.fetchall()

conn.close()


# compose output string for each query
s1 = ""
for row in r1:
    s1 += "{} --- {:,} views\n".format(row[1],row[0])

s2 = ""
for row in r2:
    s2 += "{} --- {:,} views\n".format(row[1],row[0])

s3 = ""
for row in r3:
    s3 += "{} --- {:.2%} error rate\n".format(row[3],row[2])

# print output to output.txt file
output = open("Output.txt", "w")
output.write(s1)
output.write("\n")
output.write(s2)
output.write("\n")
output.write(s3)
output.close()
