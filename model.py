import db
from db import Database
import uuid
import base64


class User:
    db = Database()

    def __init__(self, pk, name, surname, born):
        self.name = name
        self.surname = surname
        self.born = born
        self.id = pk

    def __str__(self):
        return ' '.join((self.name, self.surname, self.born))

    @classmethod
    def get_all_users(cls):
        users_db = cls.db.get_all_records()
        users = []
        for user_db in users_db:
            user = cls(user_db['id'], user_db['name'], user_db['surname'], user_db['born'])
            users.append(user)
        return users

    @classmethod
    def add_user(cls, name, surname, born):
        name = name.get()
        surname = surname.get()
        born = born.get()
        cls.db.add_new_user(name, surname, born)





