import psycopg2

class PostGres:
    
    def __init__(self, ip, name_db, user, password):
        self.__ip = ip
        self.__name_db = name_db
        self.__user = user
        self.__password = password


    def insert_all(self, name, surname, email):
        self.__conn = psycopg2.connect(host=self.__ip ,database=self.__name_db ,user=self.__user ,password=self.__password)
        self.__cur = self.__conn.cursor()
        self.__cur.execute("INSERT INTO users (name, surname, email) VALUES(%s, %s, %s)", (name, surname, email))
        self.__cur.close()
        self.__conn.commit()
        self.__conn.close()

    def update_name(self, name, id):
        self.__conn = psycopg2.connect(host=self.__ip ,database=self.__name_db ,user=self.__user ,password=self.__password)
        self.__cur = self.__conn.cursor()
        self.__cur.execute("Update users set name = %s where id = %s", (name, id))
        self.__cur.close()
        self.__conn.commit()
        self.__conn.close()
    
    def update_surname(self, surname, id):
        self.__conn = psycopg2.connect(host=self.__ip ,database=self.__name_db ,user=self.__user ,password=self.__password)
        self.__cur = self.__conn.cursor()
        self.__cur.execute("Update users set surname = %s where id = %s", (surname, id))
        self.__cur.close()
        self.__conn.commit()
        self.__conn.close()

    def update_email(self, email, id):
        self.__conn = psycopg2.connect(host=self.__ip ,database=self.__name_db ,user=self.__user ,password=self.__password)
        self.__cur = self.__conn.cursor()
        self.__cur.execute("Update users set email = %s where id = %s", (email, id))
        self.__cur.close()
        self.__conn.commit()
        self.__conn.close()

    def delete(self, id):
        self.__conn = psycopg2.connect(host=self.__ip ,database=self.__name_db ,user=self.__user ,password=self.__password)
        self.__cur = self.__conn.cursor()
        self.__cur.execute("Delete from users where id = %s", (id,))
        self.__cur.close()
        self.__conn.commit()
        self.__conn.close()