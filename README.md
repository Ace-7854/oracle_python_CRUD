# Oracle Python CRUD Automation

This project automates CRUD (Create, Read, Update, Delete) operations in an **Oracle Database** using Python. It dynamically retrieves table structures, generates link tables, and performs operations efficiently without manual table definitions.

## Features 🚀
- **Dynamic Table Detection**: Automatically fetches all tables and fields from the database.
- **Automated Link Table Creation**: Generates intermediary tables for many-to-many relationships.
- **CRUD Operations**: Supports inserting, updating, deleting, and retrieving records.
- **Database Management**: Functions for dropping tables and clearing data.
- **Optimized Queries**: Uses parameterized SQL to prevent SQL injection.

---

## Installation & Setup ⚙️
1. **Install Dependencies**
   ```bash
   pip install oracledb
   ```
2. **Ensure Oracle Database Connection**
   - Update `oracle_module.py` with your **Oracle connection details**.
   - The script will prompt for a password at runtime.

---

## Usage 🛠️
### **1. Establish a Connection**
```python
from oracle_module import oracle

oracle_conn = oracle()  # Opens database connection
```

### **2. Retrieve All Tables**
```python
tables = oracle_conn.get_all_tables()
print(tables)  # List of all table names
```

### **3. Fetch Table Fields**
```python
table_name = "employees"
fields = oracle_conn.get_table_fields(table_name)
print(fields)  # Dictionary of field names and data types
```

### **4. Insert a Record**
```python
values = (101, "John Doe", "Software Engineer", 70000)
oracle_conn.insert_rec("employees", values)
```

### **5. Update a Record**
```python
oracle_conn.update_record(
    tbl=table("employees"),
    update_flds=["salary", "job_title"],
    values=[75000, "Lead Engineer"],
    condition_field="employee_id",
    cond_val=101
)
```

### **6. Delete a Record**
```python
oracle_conn.delete_record("employees", "employee_id", 101)
```

### **7. Drop a Table**
```python
oracle_conn.drop_tbl("old_table")
```

### **8. Close the Connection**
```python
oracle_conn.close_connection()
```

---

## Methods in `oracle_module.py`

| Method | Parameters | Description |
|--------|-----------|-------------|
| `get_all_tables()` | None | Retrieves all table names from Oracle. |
| `get_table_fields(table_name)` | `table_name` (str) | Returns a dictionary of field names and data types. |
| `get_data(table)` | `table` (str) | Retrieves all records from a given table. |
| `get_record(table, field, cond)` | `table` (str), `field` (str), `cond` (value) | Fetches a specific record based on a condition. |
| `insert_rec(table, values)` | `table` (str), `values` (tuple) | Inserts a new record into a table. |
| `update_record(tbl, update_flds, values, condition_field, cond_val)` | `tbl` (table object), `update_flds` (list), `values` (list), `condition_field` (str), `cond_val` (value) | Updates records dynamically based on a condition. |
| `delete_record(table, field, cond)` | `table` (str), `field` (str), `cond` (value) | Deletes a record matching the condition. |
| `empty_data(table)` | `table` (table object) | Removes all records from a table. |
| `drop_tbl(table_name)` | `table_name` (str) | Drops (deletes) a table from the database. |
| `create_table(table)` | `table` (table object) | Creates a new table in the database. |
| `create_lnk_tbl(name, fields)` | `name` (str), `fields` (dict) | Creates a dynamic link table for many-to-many relationships. |
| `close_connection()` | None | Closes the database connection. |

---

## Contributing 🤝
Feel free to contribute by improving automation, optimizing queries, or adding new functionality.

---

## License 📜
This project is licensed under the MIT License.

---

## Author
👨‍💻 Developed by **Edison Ford** | Back-end Developer & Database Enthusiast.

