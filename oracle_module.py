import oracledb
import getpass

class oracle:
    def __init__(self):
        # Establish connection once during initialization
        connection = {
            "user": "s5718375",
            "password": "",
            "host_name": "foston.bournemouth.ac.uk",
            "port": "1968",
            "service_name": "student_accts.bournemouth.ac.uk"
        }
        connection["password"] = getpass.getpass("Enter the password: ")
        conn_str = f'{connection["user"]}/{connection["password"]}@{connection["host_name"]}:{connection["port"]}/{connection["service_name"]}'
        self.__conn = oracledb.connect(conn_str)
        print("✅ Database connection established.")

    def get_data(self, table):
        lst_of_rec = []
        query = f"SELECT * FROM {table}"
        cursor = self.__conn.cursor()  # Keep cursor open across function calls
        try:
            cursor.execute(query)
            for rec in cursor:
                lst_of_rec.append(rec)
        except Exception as e:
            print(f"❌ Error in get_data: {e}")
        finally:
            return lst_of_rec

    def get_record(self, table, field, cond):
        query = f"SELECT * FROM {table} WHERE {field} = '{cond}'"
        cursor = self.__conn.cursor()
        temp = ""
        try:
            cursor.execute(query)
            for rec in cursor:
                temp = rec
        except Exception as e:
            print(f"❌ Error in get_record: {e}")
        finally: 
            return temp


    def delete_record(self, table, field, cond):
        query = f"DELETE FROM {table} WHERE {field} = '{cond}'"
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()  # Committing the delete
        except Exception as e:
            print(f"❌ Error in DELETE: {e}")
            self.__conn.rollback()  # Rollback if error occurs
        finally:
            cursor.close()
    
    def empty_data(self, table):
        query = f"DELETE FROM {table.table_name}"
        cursor = self.__conn.cursor()

        try:
            cursor.execute(query)
            self.__conn.commit()
        except Exception as e:
            print(f"❌ Error in DELETE: {e}")
            self.__conn.rollback()
        finally:
            cursor.close()

    def insert_rec(self, table, values):
        query = self.__create_insertion_query(table, values)
        print("Executing query:", query)
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()  # Committing the insert
            print("✅ Record inserted successfully.")
        except Exception as e:
            print(f"❌ Error in INSERT: {e}")
            self.__conn.rollback()  # Rollback if error occurs
        finally:
            cursor.close()

    def create_table(self, table):
        ddl_create = f"CREATE TABLE {table.table_name} ("

        for field, field_type in table.fields.items():
            ddl_create += f"{field} {field_type}, "
    
        # Remove last comma and add closing parenthesis
        ddl_create = ddl_create.rstrip(', ') + ")"
        print(ddl_create)
        cursor = self.__conn.cursor()
        try:
            cursor.execute(ddl_create)
            self.__conn.commit()
            print("✅ Table created successfully")
        except Exception as e:
            print(f"❌ Error in DDL table creation: {e}")
            self.__conn.rollback()
        finally:
            cursor.close()

    def __create_insertion_query(self, table, values):
        query = f"INSERT INTO {table.table_name} ("

        # Get the keys as a list to identify the last key
        fields = list(table.fields.keys())

        for i, key in enumerate(fields):
            if i == len(fields) - 1:
                # Last field - no comma
                query += table.fields[key] + ")"
            else:
                # Add a comma after each field except the last
                query += table.fields[key] + ", "

        query = query + " VALUES ("

        for i in range(len(values)):
            if i == len(values) - 1:
                # Check if value is a string, and handle accordingly
                if isinstance(values[i], str):
                    query += f"'{values[i]}')"
                else:
                    query += str(values[i]) + ")"
            else:
                if isinstance(values[i], str):
                    query += f"'{values[i]}', "
                else:
                    query += str(values[i]) + ", "

        return query

    def close_connection(self):
        # Manually close the connection when done
        if self.__conn:
            self.__conn.close()
            print("❌ Database connection closed.")

    def create_lnk_tbl():
        pass

    def get_all_tables(self):
        query = """
        SELECT table_name FROM user_tables
        """
        cursor = self.__conn.cursor()
        tables = []
        try:
            cursor.execute(query)
            tables = [row[0] for row in cursor.fetchall()]  # Get table names
        except Exception as e:
            print(f"❌ Error retrieving tables: {e}")
        finally:
            cursor.close()
        return tables

    def get_table_fields(self, table_name):
        query = f"""
        SELECT column_name, data_type 
        FROM user_tab_columns 
        WHERE table_name = UPPER('{table_name}')
        """
        cursor = self.__conn.cursor()
        fields = {}
        try:
            cursor.execute(query)
            for column, dtype in cursor.fetchall():
                fields[column.lower()] = column  # Store as {python_field: sql_field}
        except Exception as e:
            print(f"❌ Error retrieving fields for {table_name}: {e}")
        finally:
            cursor.close()
        return fields

    def drop_tbl(self, table_name):
        query = f"DROP TABLE {table_name}"
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print(f"✅ Successfully dropped {table_name}")
        except Exception as e:
            print(f"❌ Error dropping table {table_name}: {e}")
        finally:
            cursor.close()