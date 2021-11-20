import os
from dotenv import load_dotenv
import pymysql


# Controls the database and provides functions to retrieve data
class Database:
    load_dotenv()
    cursor = None
    database = None

    def __init__(self):
        # Initialize database
        data = pymysql.connect(host=os.environ['HOST'],
                               user=os.environ['USER'],
                               passwd=os.environ['PASSWD'],
                               db=os.environ['DATAB'])
        self.cursor = data.cursor()
        self.database = data

    # Disconnect the databse
    def disconnect(self):
        try:
            self.cursor.close()
            self.database.close()
        except pymysql.Error as err:
            print(err)

    # Gets all data in an array
    def get_all_apps(self):
        sql = "SELECT * FROM app_list"
        app_list = []

        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            i = 0
            for row in results:
                app_list.insert(i, row)
                i += 1
        except pymysql.Error as err:
            print(err)

        self.disconnect()
        return app_list

    # Gets only one app by its id
    def get_app_by_id(self, app_id):
        sql = "SELECT * FROM app_list WHERE main_key = " + str(app_id)
        results = None
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
        except pymysql.Error as err:
            print(err)
        self.disconnect()
        return results

    def insert_suggestion(self, username, appname, applink):
        sql = "INSERT INTO suggestions (sug_key, app_name, user_name, app_link) VALUES (NULL, %s, %s, %s)"
        val = (appname, username, applink)
        try:
            self.cursor.execute(sql, val)
            self.database.commit()
        except pymysql.Error as err:
            print(err)

        self.disconnect()
