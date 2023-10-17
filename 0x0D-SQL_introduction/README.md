# 0x0D-SQL_introduction
## Commands and SQL Files

### Comments for your SQL file:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS:
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

### Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
...
mysql> quit
Bye
```

### Use “container-on-demand” to run MySQL:
- Instructions for running MySQL in a container.

##  Tasks
List databases: Write a script that lists all databases in your MySQL server.

Create a database: Write a script that creates the database hbtn_0c_0 in your MySQL server.

Delete a database: Write a script that deletes the database hbtn_0c_0 in your MySQL server.

List tables: Write a script that lists all tables of a given database in your MySQL server.

First table: Write a script that creates a table first_table in your MySQL server.

Full description: Write a script that prints the full description of the table first_table in your MySQL server.

List all in table: Write a script that lists all rows of the table first_table in your MySQL server.

First add: Write a script that inserts a new row in the table first_table in your MySQL server.

Count 89: Write a script that displays the number of records with id = 89 in the table first_table of your MySQL server.

Full creation: Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and adds multiple rows.

List by best: Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server, ordered by score.

Select the best: Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

Cheating is bad: Write a script that updates the score of Bob to 10 in the table second_table, without using Bob’s id value, only the name field.

Score too low: Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

Average: Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

Number by score: Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server, ordered by the number of records.

Say my name: Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server, but don’t list rows without a name value, and order the records by descending score.

Go to UTF8: Write a script that converts the hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server, including converting the table and field name in first_table.

Temperatures #0: Import a table dump and write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

Temperatures #1: Import a table dump and write a script that displays the top 3 cities' temperature during July and August ordered by temperature (descending).
