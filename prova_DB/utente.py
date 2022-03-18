

class Utente:

    def __init__(self, name, surname, email, db):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__db = db

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_email(self, email):
        self.__email = email

    def save(self):
        self.__db.insert_all(self.__name, self.__surname, self.__email)

    def update_name(self, name, id):
        self.__db.update_name(name, id)

    def update_surname(self, surname, id):
        self.__db.update_surname(surname, id)

    def update_email(self, email, id):
        self.__db.update_email(email, id)

    def delete(self, id):
        self.__db.delete(id)