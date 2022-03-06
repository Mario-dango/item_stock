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
    
    def ver(self):
        sql = 'select * from robots'

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("Estado:", user[1])
            print("Nombre:", user[2])
            print("Descripción:", user[3])

        except Exception as e:
            raise


    def select_all_robots(self):
        sql = 'SELECT * FROM Robots'
        try:
            self.cursor.execute(sql)
            robots = self.cursor.fetchall()

            for robot in robots:
                print("Id:", robot[0])
                print("Estado:", robot[1])
                print("Nombre:", robot[2])
                print("Descripción:", robot[3])
                print("____________________\n")
        except Exception as e:
            raise


    def agregar(self, tabla):
        sql = 'CREATE TABLE IF NOT EXISTS bawydb.{}'.format(tabla)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            raise


    def close(self):
        self.connection.close()


db_cheta = Database()
#db_cheta.select_robot(1)
db_cheta.select_all_robots()
db_cheta.agregar('datos')
