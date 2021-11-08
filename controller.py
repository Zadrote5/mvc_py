import tkinter
from config import *
from model import User
from view import View


class WindowMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Window(metaclass=WindowMeta):

    def __init__(self):
        self.view = View()

    def page_add(self, function):
        self.view.view_add_page(function)

    def view_user(self, users):
        self.view.view_users_list(users)

    def add_user(self, name, surname, born):
        User.add_user(name, surname, born)
        self.view.view_users_list(User.get_all_users())

    def edit_user(self, users):
        self.view.edit_user_page(users)


win = Window()
win.view_user(User.get_all_users())
win.page_add(win.add_user)
win.edit_user(User.get_all_users())
win.view.mainloop()