import tkinter as tk
from tkinter import messagebox
from auth import signup, login

class CoeusAIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coeus AI - Login")
        self.geometry("300x250")
        self.create_login_screen()

    def create_login_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.handle_login).pack(pady=5)
        tk.Button(self, text="Sign Up", command=self.create_signup_screen).pack(pady=5)

    def create_signup_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Sign Up", command=self.handle_signup).pack(pady=5)
        tk.Button(self, text="Back to Login", command=self.create_login_screen).pack(pady=5)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login(username, password):
            self.create_main_interface()
        else:
            messagebox.showerror("Error", "Incorrect username or password")

    def handle_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        if signup(username, password, email):
            messagebox.showinfo("Success", "User signed up successfully!")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "Username or email already exists")

    def create_main_interface(self):
        self.title("Coeus AI - Main Interface")
        for widget in self.winfo_children():
            widget.destroy()
        tk.Label(self, text="Welcome to Coeus AI!").pack(pady=20)
        # Add your main interface components here

if __name__ == '__main__':
    from database import setup_database
    setup_database()
    app = CoeusAIApp()
    app.mainloop()
