import sqlite3


class Database:
    def __init__(self, path_to_db='data/test_db.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()  # эта поебень будет выполнять команды
        data = None
        cursor.execute(sql, parameters)  # Выполняет нашу команду sql

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
        id int NOT NULL,
        Name varchar(255) NOT NULL,
        tg_nik varchar(255),
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, tg_nik: str = None):
        sql = """
        INSERT INTO Users(id, name, tg_nik) VALUES (?, ?, ?)
        """
        parameters = (id, name, tg_nik)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = """
        SELECT * FROM Users WHERE 
        """
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT (*) FROM Users;", fetchone=True)

    def update_tg_nik(self, tg_nik, id):
        sql = """
        UPDATE Users SET tg_nik=? WHERE id=?
        """
        return self.execute(sql, parameters=(tg_nik, id), commit=True)

    def delete_all_users(self):
        self.execute("DELETE FROM Users WHERE True", commit=True)


def logger(statement):
    print(f"""
    {'__' * 50}
    Executing
    {statement}
    {'__' * 50}
    """)
