#already made tables
class database:
    def __init__(self, table, **kwargs):
        self.table_name = table 
        ## making a dictionary based on input fields
        self.fields = dict(kwargs)

#a new table un-made, provides a way of setting up constraints and making the table itself in python
class new_database:
    def __init__(self, tbl_name, **kwargs):
        self.table_name = tbl_name
        self.fields = dict(kwargs)
