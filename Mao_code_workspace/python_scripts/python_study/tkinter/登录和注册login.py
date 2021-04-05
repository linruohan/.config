# coding=utf-8
import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('500x400')

# welcome image

canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

canvas.pack(side='top')

tk.Label(text='user name').place(x=50, y=150)
tk.Label(text='password').place(x=50, y=190)
# 用户名
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# 密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


def login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    import os
    if not os.path.exists('D:\\atom\\tkinter\\usr_info.txt'):
        with open('D:\\atom\\tkinter\\usr_info.txt', 'wb') as usr_file:
            usr_info = {'admin': 'admin'}
            pickle.dump(usr_info, usr_file)
    else:
        with open('D:\\atom\\tkinter\\usr_info.txt', 'rb') as usr_file:
            usr_info = pickle.load(usr_file)
    if usr_name in usr_info:
        if usr_pwd == usr_info[usr_name]:
            messagebox.showinfo(title='welcome', message='how are you?' + usr_name)
        else:
            messagebox.showerror(title='error', message='Error,your password is wrong,try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('welcome', 'you have not sign up yet,would you like sign up now?')
        if is_sign_up:
            sign_up()


def sign_up():
    def sign_to_file():
        np = new_pwd.get()
        npf = new_passwd_confirm.get()
        nn = new_name.get()
        with open('D:\\atom\\tkinter\\usr_info.txt', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            messagebox.showerror('error', 'passsword and confirm password must be the same.')
        elif nn in exist_usr_info:
            messagebox.showerror('error', 'the user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('D:\\atom\\tkinter\\usr_info.txt', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            messagebox.showinfo(title='welcome', message='you have sign up successfully!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('sign window')
    window_sign_up.geometry('400x500')

    # 用户名
    new_name = tk.StringVar()
    new_name.set('example@126.com')
    tk.Label(window_sign_up, text='user name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)
    # 密码
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='password:').place(x=10, y=50)
    entry_new_passwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_passwd.place(x=150, y=50)
    # 密码确认
    new_passwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='password confirm:').place(x=10, y=90)
    entry_new_passwd_confirm = tk.Entry(window_sign_up, text='password confirm', textvariable=new_passwd_confirm,
                                        show='*')
    entry_new_passwd_confirm.place(x=150, y=90)

    bu_sign_up = tk.Button(window_sign_up, text='sign up', command=sign_to_file)
    bu_sign_up.place(x=150, y=130)


# 登录和注册按钮
b_login = tk.Button(window, text='Login', command=login)
b_login.place(x=170, y=230)
b_sign_up = tk.Button(window, text='sign up', command=sign_up)
b_sign_up.place(x=270, y=230)

window.mainloop()
