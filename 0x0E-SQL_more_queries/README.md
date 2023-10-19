# 0x0E-SQL_more_queries

## Task 0: My privileges!
### Description:
- Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

### SQL Query:
```sql
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

## Task 1: Root user
### Description:
- Write a script that creates the MySQL server user `user_0d_1`.
- `user_0d_1` should have all privileges on your MySQL server.
- The password for `user_0d_1` should be set to `user_0d_1_pwd`.
- If the user `user_0d_1` already exists, your script should not fail.

### SQL Query:
```sql
cat 1-create_user.sql | mysql -hlocalhost -uroot -p
```

## Task 2: Read user
### Description:
- Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
- `user_0d_2` should have only `SELECT` privilege in the database `hbtn_0d_2`.
- The password for `user_0d_2` should be set to `user_0d_2_pwd`.
- If the database `hbtn_0d_2` and the user `user_0d_2` already exist, your script should not fail.

### SQL Query:
```sql
cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
```

## Task 3: Always a name
### Description:
- Write a script that creates the table `force_name` on your MySQL server.
- `force_name` description:
  - `id INT`
  - `name VARCHAR(256)` can't be null.
- The database name will be passed as an argument of the `mysql` command.
- If the table `force_name` already exists, your script should not fail.

### SQL Query:
```sql
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

## Task 4: ID can't be null
### Description:
- Write a script that creates the table `id_not_null` on your MySQL server.
- `id_not_null` description:
  - `id INT` with the default value 1.
  - `name VARCHAR(256)`.
- The database name will be passed as an argument of the `mysql` command.
- If the table `id_not_null` already exists, your script should not fail.

### SQL Query:
```sql
cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

## Task 5: Unique ID
### Description:
- Write a script that creates the table `unique_id` on your MySQL server.
- `unique_id` description:
  - `id INT` with the default value 1 and must be unique.
  - `name VARCHAR(256)`.
- The database name will be passed as an argument of the `mysql` command.
- If the table `unique_id` already exists, your script should not fail.

### SQL Query:
```sql
cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

## Task 6: States table
### Description:
- Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.
- `states` description:
  - `id INT` unique, auto-generated, can't be null, and is a primary key.
  - `name VARCHAR(256)` can't be null.
- If the database `hbtn_0d_usa` or the table `states` already exists, your script should not fail.

### SQL Query:
```sql
cat 6-states.sql | mysql -hlocalhost -uroot -p
```

## Task 7: Cities table
### Description:
- Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.
- `cities` description:
  - `id INT` unique, auto-generated, can't be null, and is a primary key.
  - `state_id INT`, can't be null and must be a FOREIGN KEY that references to `id` of the `states` table.
  - `name VARCHAR(256)` can't be null.
- If the database `hbtn

_0d_usa` or the table `cities` already exists, your script should not fail.

### SQL Query:
```sql
cat 7-cities.sql | mysql -hlocalhost -uroot -p
```

## Task 8: First state
### Description:
- Write a script that inserts a new state with `id = 1` and `name = 'California'` in the table `states`.

### SQL Query:
```sql
cat 8-first_state.sql | mysql -hlocalhost -uroot -p
```

## Task 9: 10 more states
### Description:
- Write a script that inserts 10 new states in the table `states`.

### SQL Query:
```sql
cat 9-states.sql | mysql -hlocalhost -uroot -p
```

## Task 10: Cities of California
### Description:
- Write a script that inserts 10 new cities with `name = 'San Francisco'` and `state_id = 1` in the table `cities`.

### SQL Query:
```sql
cat 10-cities_of_california.sql | mysql -hlocalhost -uroot -p
```

## Task 11: Change the name
### Description:
- Write a script that changes the name of `California` to `California2` in the table `states`.

### SQL Query:
```sql
cat 11-change_name.sql | mysql -hlocalhost -uroot -p
```

## Task 12: 10 new cities
### Description:
- Write a script that inserts 10 new cities with `name = 'San Francisco'` and `state_id = 1` in the table `cities`.

### SQL Query:
```sql
cat 12-more_cities_of_california.sql | mysql -hlocalhost -uroot -p
```

## Task 13: Pop cities
### Description:
- Write a script that deletes all cities of `California` in the table `cities`.

### SQL Query:
```sql
cat 13-pop_cities.sql | mysql -hlocalhost -uroot -p
```

## Task 14: Delete by ID
### Description:
- Write a script that deletes a state from `states` by `id`.

### SQL Query:
```sql
cat 14-delete_state.sql | mysql -hlocalhost -uroot -p
```

## Task 15: City or state
### Description:
- Write a script that lists all cities from the database `hbtn_0d_usa`.

### SQL Query:
```sql
cat 15-list_cities.sql | mysql -hlocalhost -uroot -p
```

## Task 16: Full description
### Description:
- Write a script that lists all cities with their corresponding state (if available) from the database `hbtn_0d_usa`.

### SQL Query:
```sql
cat 16-full_description.sql | mysql -hlocalhost -uroot -p
```

## Task 17: Number by state
### Description:
- Write a script that lists all states with the number of cities (if available) from the database `hbtn_0d_usa`.

### SQL Query:
```sql
cat 17-number_by_state.sql | mysql -hlocalhost -uroot -p
```

## Task 18: Cities by state
### Description:
- Write a script that lists all states with the number of cities (if available) ordered by the number of cities in a descending order from the database `hbtn_0d_usa`.

### SQL Query:
```sql
cat 18-cities_by_state.sql | mysql -hlocalhost -uroot -p
```

## Task 19: States with cities
### Description:
- Write a script that lists all states with the number of cities (if available) where the city name is `San Francisco` from the database `hbtn_0d_usa`.

### SQL Query:
```sql
cat 19-states_with_cities.sql | mysql -hlocalhost -uroot -p
```

## Task 20: Best places to go
### Description:
- Write a script that lists all cities in the database `hbtn_0d_usa` where the state is `California` ordered by the number of cities then by city name.

### SQL Query:
```sql
cat 20-best_places.sql | mysql -hlocalhost -uroot -p
```

This repository contains SQL scripts for various tasks related to managing a MySQL database. You can execute these SQL scripts using the `mysql` command-line tool. Simply run the provided commands in your terminal to perform each task. Please make sure to replace any placeholders like database names or passwords as needed.
