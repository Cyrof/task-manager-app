from dataclasses import dataclass
import sqlite3

sql_task_table = """ CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    urgent_lvl CHAR NOT NULL,
    date_created VARCHAR NOT NULL,
    due_date VARCHAR NOT NULL,
    task_desc VARCHAR,
    status VARCHAR NOT NULL
    ); """


class Task:
    def __init__(self):
        self.__task = None
        self.__db_path = r"tasks.db"
        self.__conn = self.create_connection(self.__db_path)
        if self.__conn is not None:
            self.create_table(self.__conn, sql_task_table)
        else:
            print("Error! cannot create a database connection.")

    def insertVariableIntoTable(self, task, lvl, date_created, due_date, desc=None, status="Incomplete"):
        """ Inserts variable into SQLite table with specific param
        :param task: user inputted task
        :param lvl: urgency level chosen by user
        :param datetime: store the date and time of when task is created
        :return:
        """
        try:
            cur = self.__conn.cursor()

            insert_data_with_param = """ INSERT INTO tasks (
                task_name, urgent_lvl, date_created, due_date, task_desc, status)
                VALUES (?, ?, ?, ?, ?, ?); """
            
            data_tuple = (task, lvl, date_created, due_date, desc, status)
            cur.execute(insert_data_with_param, data_tuple)
            self.__conn.commit()
            print("Data added")
        except sqlite3.Error as e:
            print("Failed to insert Python variable into sqlite table", e)


    def addTask(self, task_name, lvl, date_created, duedate, desc, status):
        self.__task = task_name
        self.insertVariableIntoTable(self.__task, lvl, date_created, duedate, desc, status)

    def create_connection(self, db_path):
        """ create a database connection to the SQLite database
            specified by the db_path
        :param db_path: database file path 
        :return: Connection object or None 
        """

        conn = None
        try:
            conn = sqlite3.connect(db_path)
            return conn
        except Exception as e:
            print(e)
        
        return conn
    
    def create_table(self, conn, create_sql_table):
        """ create a table from the create_sql_table param
        :param conn: Connection object
        :param create_sql_table: CREATE TABLE statement
        :return:
        """

        try:
            cur = conn.cursor()
            cur.execute(create_sql_table)
        except Exception as e:
            print(e)
        
    def delete_task(self, id):
        """
        Delete a task by task id
        :param id: id of the task
        :return:
        """
        try:
            sql = 'DELETE FROM tasks WHERE id=?'
            cur = self.__conn.cursor()
            cur.execute(sql, (id,))
            self.__conn.commit()
            print("Task deleted.")
        except Exception as e:
            print(e)
    
    def delete_all_task(self):
        """
        Delete all tasks in the tasks table
        :return:
        """
        try:
            sql = 'DELETE FROM tasks'
            sql2 = 'UPDATE sqlite_sequence SET SEQ=0 WHERE NAME="tasks";'
            cur = self.__conn.cursor()
            cur.execute(sql)
            cur.execute(sql2)
            self.__conn.commit()
            print("All Tasks deleted")
        except Exception as e:
            print(e)
    
    def delete_table(self):
        """ Delete table from db file
        :return:
        """
        try:
            sql = 'DROP TABLE tasks;'
            cur = self.__conn.cursor()
            cur.execute(sql)
            self.__conn.commit()
            print("Table deleted")
        except Exception as e:
            print(e)
    
    def get_all_data(self):
        """ Get all data from db
        :param:
        :return data as a 2d list:
        """
        try:
            sql = 'SELECT * FROM tasks'
            cur = self.__conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()

            data = [[d for d in row] for row in rows]
            return data
        except Exception as e:
            print(e)
    
    def get_data_by_id(self, id):
        """ Get date by id
        :param id: id of data 
        :return data:
        """
        try:
            get_by_id = """ SELECT * FROM tasks WHERE id=?"""

            cur = self.__conn.cursor()
            cur.execute(get_by_id, (id,))
            data = cur.fetchall()
            return data
        except sqlite3.Error as e:
            print("Failed to read data from table", e)
            return None
        
    def check_table(self):
        """ Check if table is empty
        :param:
        :if table has data:
        :return False:
        :else:
        :return True:
        :return bool:
        """
        try:
            sql = """SELECT COUNT(*) FROM tasks"""

            cur = self.__conn.cursor()
            cur.execute(sql)

            data = cur.fetchall()
            
            if int(data[0][0]) == 0:
                return False
            else:
                return True

        except Exception as e:
            print(e)
        
    def update_status(self, status, id):
        """ Update status 
        :param status: new status to update
        :return:
        """
        try:
            update_stat = """ UPDATE tasks SET status=? WHERE id=?"""
            data_tuple = (status, id)
            cur = self.__conn.cursor()
            cur.execute(update_stat, data_tuple)
            self.__conn.commit()
            print("Status Updated")
        except Exception as e:
            print(e)

    def update_task(self, id , taskname, priority, duedate, desc):
        """ Update task
        :param id: id of task
        :param updated_task: tuple of data to update
        :return:
        """
        try:
            update_sql = """ UPDATE tasks SET 
            task_name=?, urgent_lvl=?, due_date=?, task_desc=? WHERE id=?"""
            data_tuple = (taskname, priority, duedate, desc, id)
            cur = self.__conn.cursor()
            cur.execute(update_sql, data_tuple)
            self.__conn.commit()
            print("Task updated")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import random
    import datetime
    t = Task()
    # t.delete_table()
    # print(t.get_data_by_id(2))
    t.delete_all_task()
    # print(t.check_table())
    
    lvl = ['i', 'u', 'n']

    date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    desc = ["test", "hi", ""]



    counter = 1
    for x in range(20):
        start_dt = datetime.date(2022, 8, 9)
        end_dt = datetime.date(2023, 8, 9)
        time_between_dates = end_dt - start_dt
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_dt + datetime.timedelta(days=random_number_of_days)
        random_date = random_date.strftime("%d/%m/%Y")

        task_name = "test" + str(counter)
        t.addTask(task_name, str(random.choice(lvl)), date_time, random_date, str(random.choice(desc)), "Incomplete")
        counter += 1