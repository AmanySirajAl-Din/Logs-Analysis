# import DB library we are using..
import psycopg2


# Q1. What are the most popular three articles of all time?
def popularArticles():
    # connect to the DB.
    conn = psycopg2.connect("dbname=news")
    
    cursor = conn.cursor()
    
    # excute query to find the answer of the qustion
    cursor.execute("""
        SELECT articles.slug, count(*) as countLog 
        FROM log, articles 
        WHERE '/article/'||articles.slug = log.path 
        GROUP BY articles.slug 
        ORDER BY countLog DESC 
        LIMIT 3;
        """)
    
    # Save results by fetch it all
    popularArticles_results = cursor.fetchall()
    # 5-Print Out results on screen
    print "\n The most popular three articles of all time:\n"
    # Loop to read data from table, row by row
    for article in popularArticles_results:
        # Python function to convert a list to a string for display
        # source : https://www.decalage.info/en/python/print_list
        print '"' + ('" - '.join(map(str, article))) + ' views'
    
    # close the Connection
    conn.close()


# Q2. Who are the most popular article authors of all time?
def popularAuthors():
    
    conn = psycopg2.connect("dbname=news")
   
    cursor = conn.cursor()
   
    cursor.execute("""
        SELECT authors.name, count(*) as countlog 
        from authors, articles, log 
        WHERE articles.author = authors.id 
            AND  '/article/'||articles.slug = log.path 
        GROUP BY authors.name 
        ORDER BY countLog DESC 
        LIMIT 3;
        """)
    popularAuthors_results = cursor.fetchall()
    
    print "\n The most popular article authors of all time:\n"
    for author in popularAuthors_results:
        print(' - '.join(map(str, author))) + ' views'
    
    conn.close()


# Q3. On which days did more than 1% of requests lead to errors?
def requests_lead_errors():
    
    conn = psycopg2.connect("dbname=news")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT errorLogs.date, (100.0*counterror/countlogs) as percent 
        FROM allLogs, errorLogs 
        WHERE allLogs.date = errorLogs.date 
            AND counterror > countLogs/100;
        """)
    logRequest_results = cursor.fetchall()
    
    print "\n Days which has more than 1% of requests lead to errors: \n"
    for logRequest in logRequest_results:
        print(' - '.join(map(str, logRequest))) + ' % errors'
    
    conn.close()


# Call functions to RUN..
if __name__ == "__main__":
    popularArticles()
    popularAuthors()
    requests_lead_errors()