import sqlite3

sql_task_table = """ CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    urgent_lvl CHAR NOT NULL
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

    def insertVariableIntoTable(self, task, lvl):
        """ Inserts variable into SQLite table with specific param
        :param task: user inputted task
        :param lvl: urgency level chosen by user
        :return:
        """
        try:
            cur = self.__conn.cursor()

            insert_data_with_param = """ INSERT INTO tasks (
                task_name, urgent_lvl)
                VALUES (?, ?); """
            
            data_tuple = (task, lvl)
            cur.execute(insert_data_with_param, data_tuple)
            self.__conn.commit()
            print("Data added")
        except sqlite3.Error as e:
            print("Failed to insert Python variable into sqlite table", e)


    def addTask(self, task_name, lvl):
        self.__task = task_name
        self.insertVariableIntoTable(self.__task, lvl)

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
        sql = 'DELETE FROM tasks WHERE id=?'
        cur = self.__conn.cursor()
        cur.execute(sql, (id,))
        self.__conn.commit()
        print("Task deleted.")
    
    def delete_all_task(self):
        """
        Delete all tasks in the tasks table
        :return:
        """
        sql = 'DELETE FROM tasks'
        sql2 = 'UPDATE sqlite_sequence SET SEQ=0 WHERE NAME="tasks";'
        cur = self.__conn.cursor()
        cur.execute(sql)
        cur.execute(sql2)
        self.__conn.commit()
        print("All Tasks deleted")

if __name__ == "__main__":
    t = Task()
    t.delete_all_task()