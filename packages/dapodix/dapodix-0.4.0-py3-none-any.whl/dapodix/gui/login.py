import tkinter as tk
from dapodik import __semester__, Dapodik


class LoginFrame(tk.Frame):
    def __init__(self, master=None, on_login=None, cnf=None, **kw):
        super(LoginFrame, self).__init__(master, cnf=cnf if cnf else {}, **kw)
        on_login = on_login if callable(on_login) else self.login
        # Email Form
        self.emailLabel = tk.Label(self, text="Email")
        self.emailLabel.grid(row=0, column=0)
        self.email = tk.StringVar(self)
        self.emailEntry = tk.Entry(self, textvariable=self.email)
        self.emailEntry.grid(row=0, column=1)
        # Password Form
        self.passwordLabel = tk.Label(self, text="Password")
        self.passwordLabel.grid(row=1, column=0)
        self.password = tk.StringVar(self)
        self.passwordEntry = tk.Entry(self, textvariable=self.password, show="*")
        self.passwordEntry.grid(row=1, column=1)
        # Semester Form
        self.semesterLabel = tk.Label(self, text="Semester")
        self.semesterLabel.grid(row=2, column=0)
        self.semester = tk.StringVar(self, value=__semester__)
        self.semesterEntry = tk.Entry(self, textvariable=self.semester)
        self.semesterEntry.grid(row=2, column=1)
        # Server Form
        self.serverLabel = tk.Label(self, text="Server")
        self.serverLabel.grid(row=3, column=0)
        self.server = tk.StringVar(self, value="http://localhost:5774/")
        self.serverEntry = tk.Entry(self, textvariable=self.server)
        self.serverEntry.grid(row=3, column=1)
        # Button
        self.loginButton = tk.Button(self, text="Masuk", command=on_login)
        self.loginButton.grid(row=5, column=0)

    def login(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        print(f"{email} {password}")

    def dapodik(self) -> Dapodik:
        return Dapodik(
            username=self.emailEntry.get(),
            password=self.passwordEntry.get(),
            semester_id=self.semesterEntry.get(),
            server=self.serverEntry.get(),
        )
