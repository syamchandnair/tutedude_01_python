# Assignment 7:
# Module 12: Building Database Apps with PostgreSQL & Python

import psycopg2
import re

def get_connection():
    conn_local = None
    try:
        conn_local = psycopg2.connect(host="localhost", port ="5432", dbname="demo", user="postgres", password="Demo123")
        print ('Connected successfully')
    except (Exception, psycopg2.Error) as error:
        print("Error: {}".format(error))
        exit(1)

    return conn_local

def close_connection(con1):
    try:
        con1.close()
        print ('Connection closed!')
    except (Exception, psycopg2.Error) as error:
        print(error)

def execute_ddl(con1, sql):
    res = None
    try:
        cursor = con1.cursor()
        cursor.execute(sql)
        res = "Done"
    except (Exception, psycopg2.Error) as error:
        res = "Error: {}".format(error)
    return res

def query_database(con1, sql):
    res = None
    try:
        cursor = con1.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        res = "Error: {}".format(error)

    return res
##
# opening connection
conn = get_connection()

# Creating table
result = execute_ddl(conn, "CREATE TABLE employees (ID int, NAME varchar (100), Age int);")
if re.match("Error:", result):
    print("Error, hence rolling back")
    conn.rollback()
elif re.match("Done", result):
        print ("Table created successfully")

# inserting records
records_to_be_inserted = [
    {"Id": 1, "Name": "Ross Geller", "Age": "23"},
    {"Id": 2, "Name": "Rachel Green", "Age": "21"},
    {"Id": 3, "Name": "Chandler Bing", "Age": "20"},
    {"Id": 4, "Name": "Walter White", "Age": "52"},
    {"Id": 5, "Name": "Jesse Pinkman", "Age": "38"},
    {"Id": 6, "Name": "Skyler White", "Age": "42"}
]

for row in records_to_be_inserted:
    sql = "INSERT INTO employees (Id, Name,Age) VALUES (%s,'%s',%s);" % (row['Id'], row['Name'], row['Age'])
    result = execute_ddl(conn, sql)
    if re.match("Error:", result):
        print("Error, hence rolling back")
    elif re.match("Done", result):
        print ("Record with ID {} inserted successfully ".format(row['Id']))

# accept data from user and insert
print("Accepting employee records...")

t_id=input("Enter ID: ")
t_name=input("Enter name: ")
t_age=input("Enter age: ")

t_id=int(t_id)
t_age=int(t_age)

if not isinstance(t_id, int):
    print ('ID must be an integer')
    conn.rollback()
    exit(1)

if not isinstance(t_age, int):
    print ('Age must be an integer')
    conn.rollback()
    exit(1)

sql = "INSERT INTO employees (Id, Name,Age) VALUES (%s,'%s',%s);" % (t_id, t_name, t_age)
result = execute_ddl(conn, sql)
if re.match("Error:", result):
    print("Error, hence rolling back")
    conn.rollback()
    exit(1)
elif re.match("Done", result):
    print ("Record with ID {} inserted successfully ".format(t_id))

conn.commit()

# Extracting records from table and printing in console
result = query_database(conn, "SELECT * FROM employees;")

if not result:
    print("No results found")
elif re.match("Error:", str(result), flags=0):
    print("Error encountered")
    conn.rollback()
else:
    print("\nExtracted below records from database:\n\n{}\t{}\t{}".format("Id", "Name", "Age"))
    for row in result:
        print("{}\t{}\t{}".format(row[0], row[1], row[2]))

# closing connection
close_connection(conn)