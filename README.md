# Logs Analysis Project
Udacity Full Stack Nanodegree .. 
Part 3: The Backend: Databases & Applications

## Description:

In this project, used a PostgreSQL database, interacting with a live database both from the command line and from code, explore a large database with over a million rows, and build and refine complex queries and use them to draw business conclusions from data.

Report generation:
Building an informative summary from logs is a real task that comes up very often in software engineering.

The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

#### To open this project:
You have to use a virtual machine 
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

The virtual machine:

1- This project makes use of the Linux-based virtual machine (VM).
2- If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
    
Download the data:

Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
    
Explore the data:

Once you have the data loaded into your database, connect to your database using ```psql -d news``` and explore the tables using the ```\dt``` and ```\d``` table commands and select statements.

>```\dt``` — display tables — lists the tables that are available in the database.

>``` \d table``` — (replace table with the name of a table) — shows the database schema for that particular table.

DB includes three Tables:

> The ```authors``` table includes information about the authors of articles.

> The ```articles``` table includes the articles themselves.

>The ```log``` table includes one entry for each time a user has accessed the site.

#### After doing what we note above, you can deal with the DB.

## So what are we reporting, anyway?
Here are the questions the reporting tool should answer.

#### 1. What are the most popular three articles of all time? 
Q1. Which articles have been accessed the most? 
    
Present this information as a sorted list with the most popular article at the top.

Q2. Who are the most popular article authors of all time? 
    
That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Q3. On which days did more than 1% of requests lead to errors? 

The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

## Before Answering these questions:
#### You need to create these views in your database:

1- allLogs view:

news=# ```CREATE VIEW allLogs 
AS SELECT to_char(time,'month dd,yyyy') as date, count(*) as countLogs 
FROM log GROUP BY date;```
    
then you can display this view data by this query:
    
news=# ```SELECT * FROM allLogs;```

you will get 31 rows as output

 |      date        | countlogs|
 |------------------|----------|
 |july      01,2016 |     38705|
 |july      02,2016 |     55200|
 |july      03,2016 |     54866|
 |july      04,2016 |     54903|
 |july      05,2016 |     54585|
 |july      06,2016 |     54774|
 |july      07,2016 |     54740|
 |july      08,2016 |     55084|
 |july      09,2016 |     55236|
 |july      10,2016 |     54489|
 |july      11,2016 |     54497|
 |july      12,2016 |     54839|
 |july      13,2016 |     55180|
 |july      14,2016 |     55196|
 |july      15,2016 |     54962|
 |july      16,2016 |     54498|
 |july      17,2016 |     55907|
 |july      18,2016 |     55589|
 |july      19,2016 |     55341|
 |july      20,2016 |     54557|
 |july      21,2016 |     55241|
 |july      22,2016 |     55206|
 |july      23,2016 |     54894|
 |july      24,2016 |     55100|
 |july      25,2016 |     54613|
 |july      26,2016 |     54378|
 |july      27,2016 |     54489|
 |july      28,2016 |     54797|
 |july      29,2016 |     54951|
 |july      30,2016 |     55073|
 |july      31,2016 |     45845|
(31 rows)

2- errorLogs view:

news=# ```CREATE VIEW errorLogs AS 
SELECT to_char(time,'month dd,yyyy') as date, count(*) as countError 
FROM log WHERE status= '404 NOT FOUND' GROUP BY date;```
    
then you can display this view data by this query:
    
news=# ```SELECT * FROM errorLogs;```

you will get 31 rows as output

 |      date        | counterror|
 |------------------|-----------|
 |july      05,2016 |        423|
 |july      20,2016 |        383|
 |july      13,2016 |        383|
 |july      16,2016 |        374|
 |july      22,2016 |        406|
 |july      28,2016 |        393|
 |july      08,2016 |        418|
 |july      07,2016 |        360|
 |july      24,2016 |        431|
 |july      14,2016 |        383|
 |july      10,2016 |        371|
 |july      30,2016 |        397|
 |july      21,2016 |        418|
 |july      09,2016 |        410|
 |july      03,2016 |        401|
 |july      06,2016 |        420|
 |july      27,2016 |        367|
 |july      11,2016 |        403|
 |july      23,2016 |        373|
 |july      29,2016 |        382|
 |july      26,2016 |        396|
 |july      15,2016 |        408|
 |july      18,2016 |        374|
 |july      19,2016 |        433|
 |july      04,2016 |        380|
 |july      31,2016 |        329|
 |july      01,2016 |        274|
 |july      12,2016 |        373|
 |july      17,2016 |       1265|
 |july      25,2016 |        391|
 july      02,2016 |        389
(31 rows)

#### Now you can run ```LogsAnalysis.py``` on you virtual machine
    
    vagrant@vagrant:/vagrant$ python LogsAnalysis.py


## Author

#### Amany Siraj Al-Din
