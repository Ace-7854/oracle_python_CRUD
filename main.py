"""
This file is purely for demonstration as to how the other file can work
"""
from oracle_module import oracle, table, new_table

def define_all_objects(oracle_conn):
    tables = oracle_conn.get_all_tables()
    table_objects = []

    for tbl_name in tables:
        fields = oracle_conn.get_table_fields(tbl_name)
        table_objects.append(table(tbl_name.lower(), **fields))

    return table_objects

def make_new_table():
    pass

def define_link_tbls(lst):
    pass

def display_all_tables(lst):
    for table in lst:
        print(f"{table.table_name} with fields {table.fields}")

def find_tbl_frm_lst(lst, looking_for):
    for table in lst:
        if table.table_name == looking_for:
            return table

"""Provide the connection"""
def remove_data_from_tbles(oracle_conn, lst_tbl):
        lst_of_data = []
        for table in lst_tbl:
            oracle_conn.empty_data(table)

def display_all_data(lst_of_data, lst_table):
    for i,table in lst_of_data:
            print(f"{lst_table[i].table_name}")
            for record in table:
                print(f"{record}")

def drop_all_tbls(tbls, oracle_conn):     
    while len(tbls) != 0:
        for table in tbls:
            if oracle_conn.drop_tbl(table.table_name):
                tbls.remove(table)


def main():
    oracle_conn = oracle() ##OPENS CONNECTION

    tbls = define_all_objects(oracle_conn)

    for table in tbls: 
        #print(f"{table.table_name} with fields {table.fields}")
        print(f"{oracle_conn.get_data(table.table_name)}")
    
    oracle_conn.close_connection() #CLOSES THE CONNECTION

if __name__ == "__main__":
    main()
