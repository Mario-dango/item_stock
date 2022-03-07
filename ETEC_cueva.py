# from PyQt5.QtWidgets import *
import pymysql
import sys 

####### Machete del bueno :v    
# CURSOR (): cree un cursor de la base de datos.
#  Ejecutar (): Ejecutar una declaración SQL.
#  Commit (): Presente la operación de la base de datos a los datos.
#  Fetchone (): Datos únicos de consulta.  
#  Fetchall (): Consulta múltiples datos.
#  Cerrar (): Apague la conexión de datos.


class Database:

    def __init__(self):                     #Constructor del objeto conección a la base de datos
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='bawydb',
        )
        self.cursor = self.connection.cursor()          #Establecer conexión con base de datos 
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
    def update(self, nombre, id):
        sql = "UPDATE robots SET nombre='{}' WHERE id={}".format(nombre, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def agregar_tabla(self, tabla):
        sql = 'CREATE TABLE IF NOT EXISTS bawydb.{} (\
            id INT NOT NULL AUTO_INCREMENT,\
            img LONGBLOB,\
            PRIMARY KEY(id)) ENGINE = InnoDB'.format(tabla)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            raise



# cargar varias imagenes https://programmerclick.com/article/10891114686/
    def add_img(self):        

        ### por si quiero subir varias al mismo tiempo
        # for i in range(1,4):
        #     image_name = 'IMG%d.jpg' % i
        #     image_path = 'image/%s' % image_name
        #     with open(image_path, "rb") as fd:
        #         data = fd.read()
            
        #     try:
        #         sql = "insert into Images \
        #         values(%s, %s,%s, %s);"
                
        #         cur.execute(sql, [str(i), image_name, image_path, data])
        #         db.commit()
        #     except Exception as e:
        #         db.rollback()
        #         print("Mensaje de error: ",e)

        
        create_table = """CREATE TABLE IF NOT EXISTS demo(id INT PRIMARY KEY,\
        name VARCHAR (255) NOT NULL, profile_pic BLOB NOT NULL, \
        imp_files BLOB NOT NULL) """
    
        # Execute the create_table query first
        self.cursor.execute(create_table)
        # printing successful message
        print("Table created Successfully")
    
        query = """ INSERT INTO demo(id, name, profile_pic, imp_files)\
        VALUES (%s,%s,%s,%s)"""
    
        # First Data Insertion
        student_id = "1"
        student_name = "Shubham"
        first_profile_picture = convert_data('C:\\Users\\mario\\Documents\\ETEC\\Laboratorio\\QRs\\tipos_QR\\cuadrado.png')
        first_text_file = convert_data('C:\\Users\\mario\\Documents\\ETEC\\Laboratorio\\QRs\\tipos_QR\\dato.txt')
        try:
            # Inserting the data in database in tuple format
            self.cursor.execute(query, (student_id, student_name, first_profile_picture, first_text_file))
            # Commiting the data
            self.connection.commit()#cierra transaccion
            print("Successfully Inserted Values")
        except Exception as e:
            raise

    #Metodo para traer de la tabla Demo los archivos BLOB (Imagenes, textos, etc..) y guardarlos en la QRs/... en la clomuna N°x
    def get_imagen(self):                
        sql = "select * from demo"
        self.cursor.execute(sql)
        for image in self.cursor.fetchall():
            with open('QRs/baka.txt','wb') as fd:
                fd.write(image[3])

    def close(self):
        self.connection.close()

# Convert images or files data to binary format
def convert_data(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return binary_data


db_cheta = Database()
#db_cheta.select_robot(1)
db_cheta.select_all_robots()
# db_cheta.agregar_tabla('images')
#db_cheta.add_img()
db_cheta.get_imagen()

