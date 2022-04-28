import sqlite3


class Manager:

    @staticmethod
    def get_value(col, user_id):
        conn = sqlite3.connect("Clients.db")
        cur = conn.cursor()
        val = cur.execute(f"SELECT {col} FROM ClientData WHERE UserId = '{user_id}'").fetchall()
        return val

    @staticmethod
    def set_value(col, val, user_id):
        conn = sqlite3.connect("Clients.db")
        cur = conn.cursor()
        cur.execute(f"UPDATE ClientData SET {col} = {val} WHERE UserId = '{user_id}'")
        conn.commit()

    @staticmethod
    def del_row(user_id):
        conn = sqlite3.connect("Clients.db")
        cur = conn.cursor()
        cur.execute(f"DELETE FROM ClientData WHERE UserId = '{user_id}'")
        conn.commit()

    @staticmethod
    def create_row(user_id):
        conn = sqlite3.connect("Clients.db")
        cur = conn.cursor()
        cur.execute(f"INSERT INTO ClientData(UserId) VALUES('{user_id}')")
        conn.commit()

    @staticmethod
    def set_default(user_id):
        Manager.del_row(user_id)
