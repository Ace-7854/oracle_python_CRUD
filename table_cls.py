class database:
    def __init__(self, table, **kwargs):
        self.table_name = table 
        ## making a dictionary based on input fields
        self.fields = dict(kwargs)
        