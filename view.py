import sys
import tkinter
from tkinter import *
from config import *
from tkinter import *
from tkinter.ttk import Notebook


class View:

    def __init__(self):
        self.win = Tk()
        self.win.title('GUI')
        self.win.config(bg=bg_color)
        self.notebook = Notebook(self.win)

        self.add_page = Frame(self.notebook)
        self.notebook.add(self.add_page, text='Add user')
        self.notebook.grid(column=0, row=0)

        self.list_page = Frame(self.notebook)
        self.notebook.add(self.list_page, text='Users list')
        self.notebook.grid(column=0, row=0)

        self.edit_page = Frame(self.notebook)
        self.notebook.add(self.edit_page, text='Edit/delete user')
        self.notebook.grid(column=0, row=0)

    def mainloop(self):
        self.win.mainloop()

    @classmethod
    def get_user(cls, users, pk, name_field, surname_field, born_field):
        for user in users:
            if user.id == pk:
                name_field.delete(0, "end")
                name_field.insert(0, user.name)

                surname_field.delete(0, "end")
                surname_field.insert(0, user.surname)

                born_field.delete(0, "end")
                born_field.insert(0, user.born)

    def edit_user_page(self, users):
        name_search = tkinter.Entry(self.edit_page, bg=bg_color,
                                    font=(font, f_size, f_type),
                                    fg=f_color, width=25)
        name_search.grid(column=0, row=1)
        id_text = tkinter.Label(self.edit_page, bg=bg_color,
                                font=(font, f_size, f_type), text='Введите ID пользователя:',
                                fg=f_color, width=25)
        id_text.grid(column=0, row=0)
        id_ent = tkinter.Entry(self.edit_page, bg=bg_color,
                               font=(font, f_size, f_type),
                               fg=f_color, width=25)
        id_ent.grid(column=1, row=0)
        id_btn = tkinter.Button(self.edit_page, bg=btn_color, text='Найти',
                                font=(font, f_size, f_type),
                                fg=f_color, width=23, command=lambda: self.get_user(users, int(id_ent.get()),
                                                                                    name_search, surname_search,
                                                                                    born_search)
                                )
        id_btn.grid(column=2, row=0)

        surname_search = tkinter.Entry(self.edit_page, bg=bg_color,
                                       font=(font, f_size, f_type),
                                       fg=f_color, width=25)
        surname_search.grid(column=1, row=1)
        born_search = tkinter.Entry(self.edit_page, bg=bg_color,
                                    font=(font, f_size, f_type),
                                    fg=f_color, width=25)
        born_search.grid(column=2, row=1)
        del_btn = tkinter.Button(self.edit_page, bg='red', text='Удалить',
                                 font=(font, f_size, f_type),
                                 fg=f_color, width=23
                                 )
        del_btn.grid(column=2, row=2)
        save_btn = tkinter.Button(self.edit_page, bg=btn_color, text='Сохранить изменения',
                                  font=(font, f_size, f_type),
                                  fg=f_color, width=23
                                  )
        save_btn.grid(column=1, row=2)

    def view_users_list(self, users):
        pk = tkinter.Label(self.list_page, text='ID', bg=bg_color,
                           fg=f_color,
                           font=(font, f_size, f_type),
                           anchor='w',
                           justify=tkinter.LEFT,
                           width=5
                           )
        pk.grid(row=0, column=0)
        name = tkinter.Label(self.list_page, text='Имя', bg=bg_color,
                             fg=f_color,
                             font=(font, f_size, f_type),
                             anchor='w',
                             justify=tkinter.LEFT,
                             width=15
                             )
        name.grid(row=0, column=1)
        surname = tkinter.Label(self.list_page, text='Фамилия',
                                bg=bg_color,
                                fg=f_color,
                                font=(font, f_size, f_type),
                                anchor='w',
                                justify=tkinter.LEFT,
                                width=15
                                )
        surname.grid(row=0, column=2)
        born = tkinter.Label(self.list_page, text='Дата рождения',
                             bg=bg_color,
                             fg=f_color,
                             font=(font, f_size, f_type),
                             anchor='w',
                             justify=tkinter.LEFT,
                             width=15
                             )
        born.grid(row=0, column=3)
        user_num = 1
        for user in users:
            user_num = user_num + 1
            pk = tkinter.Label(self.list_page, text=user.id, bg=bg_color,
                               fg=f_color,
                               font=(font, f_size, f_type),
                               anchor='w',
                               justify=tkinter.LEFT,
                               width=5
                               )
            pk.grid(row=user_num, column=0)
            name = tkinter.Label(self.list_page, text=user.name, bg=bg_color,
                                 fg=f_color,
                                 font=(font, f_size, f_type),
                                 anchor='w',
                                 justify=tkinter.LEFT,
                                 width=15
                                 )
            name.grid(row=user_num, column=1)
            surname = tkinter.Label(self.list_page, text=user.surname,
                                    bg=bg_color,
                                    fg=f_color,
                                    font=(font, f_size, f_type),
                                    anchor='w',
                                    justify=tkinter.LEFT,
                                    width=15
                                    )
            surname.grid(row=user_num, column=2)
            born = tkinter.Label(self.list_page, text=user.born,
                                 bg=bg_color,
                                 fg=f_color,
                                 font=(font, f_size, f_type),
                                 anchor='w',
                                 justify=tkinter.LEFT,
                                 width=15
                                 )
            born.grid(row=user_num, column=3)

    def view_add_page(self, function):
        name_text = tkinter.Label(self.add_page, bg=bg_color,
                                  font=(font, f_size, f_type), text='Введите имя пользователя',
                                  fg=f_color, width=40)
        name_text.grid(column=0, row=1)
        name_field = tkinter.Entry(self.add_page, bg=bg_color,
                                   font=(font, f_size, f_type),
                                   fg=f_color, width=30)
        name_field.grid(column=1, row=1)

        surname_text = tkinter.Label(self.add_page, bg=bg_color,
                                     font=(font, f_size, f_type), text='Введите фамилию пользователя',
                                     fg=f_color, width=40)
        surname_text.grid(column=0, row=2)
        surname_field = tkinter.Entry(self.add_page, bg=bg_color,
                                      font=(font, f_size, f_type),
                                      fg=f_color, width=30)
        surname_field.grid(column=1, row=2)

        born_text = tkinter.Label(self.add_page, bg=bg_color,
                                  font=(font, f_size, f_type), text='Введите дату рождения пользователя',
                                  fg=f_color, width=40)
        born_text.grid(column=0, row=3)
        born_field = tkinter.Entry(self.add_page, bg=bg_color,
                                   font=(font, f_size, f_type),
                                   fg=f_color, width=30)
        born_field.grid(column=1, row=3)

        add_user_btn = tkinter.Button(self.add_page, bg=btn_color,
                                      font=(font, f_size, f_type),
                                      fg=f_color, text='Добавить',
                                      command=lambda: [function(name_field, surname_field, born_field),
                                                       name_field.delete(0, 'end'),
                                                       surname_field.delete(0, 'end'),
                                                       born_field.delete(0, 'end'),
                                                       ])
        add_user_btn.grid(column=1, row=4)
