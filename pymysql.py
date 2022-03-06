# from PyQt5.QtWidgets import *
import pymysql
    
class Database:

    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='bawydb',
        )
        self.cursor = self.connection.cursor()

        print("conexión exitosa")

    def select_robot(self, id):
        sql = 'SELECT id, estado, nombre, descripcion FROM Robots WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("Estado:", user[1])
            print("Nombre:", user[2])
            print("Descripción:", user[3])

        except Exception as e:
            raise
    
    # def insert(self, )

db_cheta = Database()
db_cheta.select_robot(1)