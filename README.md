# Oracle Python CRUD

## Overview

This project provides a Python-based solution for automating the creation and management of Oracle databases. It comprises three main components:

- **`oracle_module.py`**: Handles Oracle database operations such as creating tables, inserting records, retrieving data, and deleting records.
- **`table_cls.py`** classes to represent and dynamically create database tables.
- **`main.py`**: Demonstrates how the `oracle_module` and `table_cls` work together.

This setup is ideal for developers who need to create and populate Oracle databases without writing raw SQL scripts, especially useful in software projects requiring rapid database prototyping.

## File Structure

### 1. oracle\_module.py

This file contains the `oracle` class responsible for interacting with an Oracle database.

#### Key Features

- **Open and Close Connection**: Opens a connection upon instantiation and closes it when `close_connection()` is called.
- **Data Retrieval**:
  - `get_data(table)` - Retrieves all records from a table.
  - `get_record(table, field, cond)` - Retrieves a specific record from a table based on a condition.
- **Data Manipulation**:
  - `insert_rec(table, values)` - Inserts a new record into a table.
  - `delete_record(table, field, cond)` - Deletes a record from a table.
- **Table Creation**:
  - `create_table(table)` - Dynamically generates a DDL (Data Definition Language) statement to create a table.

#### Example Usage

```python
from oracle_module import oracle
from table_cls import database

# Instantiate Oracle connection
oracle_conn = oracle()

# Define a table
song_table = database("song_tbl", id="song_id", title="song_title")

# Insert a record
oracle_conn.insert_rec(song_table, ["S13", "Song Name"])

# Retrieve the inserted record
record = oracle_conn.get_record(song_table.table_name, song_table.fields["id"], "S13")
print(record)

# Close the connection
oracle_conn.close_connection()
```

This example shows a complete flow of inserting and retrieving a record, showcasing how the `oracle_module` works in practice.

---

### 2. table\_cls.py

This file contains two classes:

#### **database** class

- Represents an existing table structure.
- Takes dynamic parameters as fields and stores them in a dictionary.
- Example:

```python
song = database("song_tbl", id="song_id", title="song_title")
print(song.fields)
# Output: {'id': 'song_id', 'title': 'song_title'}
```

#### **new\_database** class

- Represents a new table not yet created.
- Accepts fields and their constraints as parameters.
- Example:

```python
from oracle_module import oracle
from table_cls import new_database

# Instantiate Oracle connection
oracle_conn = oracle()

# Define a new table with constraints
new_song_table = new_database("new_song_tbl", 
                              id="VARCHAR2(10)", 
                              title="VARCHAR2(50)", 
                              release_date="DATE", 
                              length="NUMBER")

# Create the table in Oracle
oracle_conn.create_table(new_song_table)

# Close the connection
oracle_conn.close_connection()
```

This approach allows rapid prototyping of new tables by simply defining fields and their constraints without manually writing SQL.

---

### 3. main.py

This file demonstrates how both `oracle_module` and `table_cls` work together.

#### Example Flow

1. Define your tables using `database` class.
2. Instantiate an Oracle connection.
3. Retrieve data, insert records, or create tables using the Oracle connection.
4. Close the connection once done.

#### Code Example

```python
oracle_conn = oracle()
lst_of_tbls = define_all_objects()
temp = find_tbl_frm_lst(lst_of_tbls,"song_tbl")
rec = oracle_conn.get_record(temp.table_name, temp.fields["id"], "S13")
print(rec)
oracle_conn.close_connection()
```

---

## Setup

### Prerequisites

Ensure you have the `oracledb` library installed:

```shell
pip install oracledb
```

### Oracle Database Connection

Update the `oracle_module.py` file with your database credentials:

```python
connection = {
    "user": "your_username",
    "password": "your_password",
    "host_name": "your_host",
    "port": "your_port",
    "service_name": "your_service"
}
```

The script will prompt for your password during runtime.

---

## Future Improvements

- Add an `update_record()` method to modify existing records.
- Extend the `get_record()` method to support comparison operators like `>`, `<`, and `!=`.
- Introduce a table relationship builder for foreign key constraints.

## License

This project is open-source and can be modified or distributed as per your needs.

## Author

This project was developed by [Your Name] as part of an Oracle database automation project.

