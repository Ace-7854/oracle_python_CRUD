import oracledb
import getpass

class oracle:
    def __init__(self):
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
    
    def get_data(self, table):
        lst_of_rec = []
        query = f"SELECT * FROM {table.table_name}"
        with self.__conn as connection:
            with connection.cursor() as cursor:
                for rec in cursor.execute(query):
                    lst_of_rec.append(rec)
        return lst_of_rec

    def delete_record(self, table, field, cond):
        query = f"DELETE FROM {table} WHERE {field} == {cond}"
        with self.__conn as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)

    def insert_rec(self, table, values):
        # query = f"INSERT INTO {table} ("
        # for i in fields:
        #     query = query + i + ", "
        pass