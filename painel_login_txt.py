import tkinter as tk
from tkinter import messagebox
import json


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")
        self.master.resizable(False, False)

        # definir ícone da janela
        self.master.iconbitmap("rbem.ico")

        # criar widgets
        self.username_label = tk.Label(self.master, text="Usuário:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Senha:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(
            self.master, text="Entrar", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(
            self.master, text="Cadastrar", command=self.register)
        self.register_button.pack()

        # adicionar botão de fechar
        self.close_button = tk.Button(
            self.master, text="Fechar", command=self.master.destroy)
        self.close_button.pack()

    def write_user_to_file(self, username, password):
        with open("users.txt", "r") as f:
            existing_users = json.load(f)

        if username in existing_users:
            messagebox.showerror("Erro", "Usuário já cadastrado")
            return

        existing_users[username] = password

        with open("users.txt", "w") as f:
            json.dump(existing_users, f)

        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")

    def register(self):
        # obter o valor dos campos de entrada
        username = self.username_entry.get()
        password = self.password_entry.get()

        # validar se o campo de usuário foi preenchido
        if not username:
            messagebox.showerror(
                "Erro", "Por favor, preencha o campo de usuário")
            return

        # insere o novo usuário no arquivo
        self.write_user_to_file(username, password)

    def login(self):
        # obter o valor dos campos de entrada
        username = self.username_entry.get()
        password = self.password_entry.get()

        # validar se os campos foram preenchidos
        if not username or not password:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return

        # verificar se as credenciais estão corretas
        with open("users.txt", "r") as f:
            existing_users = json.load(f)

        if username in existing_users and existing_users[username] == password:
            messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")


if __name__ == "__main__":
    # criar o arquivo de usuários se não existir
    with open("users.txt", "a+") as f:
        f.seek(0)
        if f.read() == "":
            f.write("{}")

    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
