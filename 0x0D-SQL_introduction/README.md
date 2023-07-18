Sure! Here's the updated README with descriptions for each task and emojis:

# SQL Introduction Tasks

This repository contains SQL scripts for various tasks related to MySQL server. Each task has a corresponding script file.

✨ **Task 0: List databases**
File: [0-list_databases.sql](./0x0D-SQL_introduction/0-list_databases.sql)

This task involves writing a script that lists all databases of your MySQL server. Execute the script to see the list of databases.

✨ **Task 1: Create a database**
File: [1-create_database_if_missing.sql](./0x0D-SQL_introduction/1-create_database_if_missing.sql)

In this task, you will create a script that creates the database `hbtn_0c_0` in your MySQL server. If the database already exists, the script will not fail.

✨ **Task 2: Delete a database**
File: [2-remove_database.sql](./0x0D-SQL_introduction/2-remove_database.sql)

Write a script to delete the database `hbtn_0c_0` from your MySQL server. If the database doesn't exist, the script will not fail.

✨ **Task 3: List tables**
File: [3-list_tables.sql](./0x0D-SQL_introduction/3-list_tables.sql)

This task involves writing a script that lists all the tables of a specified database in your MySQL server.

✨ **Task 4: First table**
File: [4-first_table.sql](./0x0D-SQL_introduction/4-first_table.sql)

In this task, you will create a script that creates a table called `first_table` in the current database in your MySQL server.

✨ **Task 5: Full description**
File: [5-full_table.sql](./0x0D-SQL_introduction/5-full_table.sql)

Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

✨ **Task 6: List all in table**
File: [6-list_values.sql](./0x0D-SQL_introduction/6-list_values.sql)

Create a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

✨ **Task 7: First add**
File: [7-insert_value.sql](./0x0D-SQL_introduction/7-insert_value.sql)

In this task, you will create a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

✨ **Task 8: Count 89**
File: [8-count_89.sql](./0x0D-SQL_introduction/8-count_89.sql)

Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

✨ **Task 9: Full creation**
File: [9-full_creation.sql](./0x0D-SQL_introduction/9-full_creation.sql)

Create a script that creates a table called `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiple rows.

✨ **Task 10: List by best**
File: [10-top_score.sql](./0x0D-SQL_introduction/10-top_score.sql)

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server, ordered by score (top first).

✨ **Task 11: Select the best**
File: [11-best_score.sql](./0x0D-SQL_introduction/11-best_score.sql)

Write a script that lists all records with a score >= 10 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server, ordered by score (top first).

✨ **Task 12: Cheating is bad**
File: [12-no_cheating.sql](./0x0D-SQL_introduction/12-no_cheating.sql)

Write a script that updates the score of a specific record in the table `second_table` without using its `id` value, only the `name` field.

✨ **Task 13: Score too low**
File: [13-change_class.sql](./0x0D-SQL_introduction/13-change_class.sql)

Write a script that removes all records with a score <= 5 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

✨ **Task 14: Average**
File: [14-average.sql](./0x0D-SQL_introduction/14-average.sql)

Write a script that computes the average score of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

✨ **Task 15: Number by score**
File: [15-groups.sql](./0x0D-SQL

_introduction/15-groups.sql)

Create a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server, ordered by the number of records (descending).

✨ **Task 16: Say my name**
File: [16-no_link.sql](./0x0D-SQL_introduction/16-no_link.sql)

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. Don't list rows without a `name` value. Results should display the score and the name, ordered by descending score.

✨ **Task 17: Go to UTF8 (Advanced)**
File: [100-move_to_utf8.sql](./0x0D-SQL_introduction/100-move_to_utf8.sql)

Convert the database `hbtn_0c_0`, table `first_table`, and the `name` field in `first_table` to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

✨ **Task 18: Temperatures #0 (Advanced)**
File: [101-avg_temperatures.sql](./0x0D-SQL_introduction/101-avg_temperatures.sql)

Import the provided table dump and write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

✨ **Task 19: Temperatures #1 (Advanced)**
File: [102-top_city.sql](./0x0D-SQL_introduction/102-top_city.sql)

Import the provided table dump and write a script that displays the top 3 cities' temperature during July and August, ordered by temperature (descending).

✨ **Task 20: Temperatures #2 (Advanced)**
File: [103-max_state.sql](./0x0D-SQL_introduction/103-max_state.sql)

Import the provided table dump and write a script that displays the max temperature of each state, ordered by the state name.

---

Feel free to check the corresponding script files for each task. Good luck with your SQL learning! 💻🔍📚