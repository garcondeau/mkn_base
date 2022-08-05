from Services.DbContext import DbContext
import os


class DbService:

    def __init__(self):
        self.sql_create_dir = './SqlScripts/Create'
        self.sql_insert_dir = './SqlScripts/Insert'
        self.sql_select_dir = './SqlScripts/Select'
        self.create_query_list = os.listdir(self.sql_create_dir)

    def initial_create(self):
        context = DbContext()
        print(self.create_query_list)
        for query in self.create_query_list:
            full_path = os.path.join(self.sql_create_dir, query)
            sql_file = open(full_path)
            query_string = sql_file.read()

            print('------')
            print(query)
            print('------')
            print(query_string)

            context.cursor.execute(query_string)
            context.db.commit()
        context.db.close()

    def insert(self, query):
        context = DbContext()

    def select(self, query):
        context = DbContext()

        full_path = os.path.join(self.sql_select_dir, query)
        sql_file = open(full_path)
        query_string = sql_file.read()

        context.cursor.execute(query_string)
        result = context.cursor.fetchall()

        return result