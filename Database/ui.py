import tkinter as tk  # Import Tkinter for GUI
from tkinter import messagebox  # Import messagebox for displaying alerts
from auth import signup, login  # Import signup and login functions from auth.py

class CoeusAIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coeus AI - Login")  # Set the window title
        self.geometry("300x250")  # Set the window size
        self.create_login_screen()  # Create the login screen

    def create_login_screen(self):
        # Function to create the login screen
        for widget in self.winfo_children():
            widget.destroy()  # Clear the window

        tk.Label(self, text="Username").pack(pady=5)  # Username label
        self.username_entry = tk.Entry(self)  # Username entry field
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)  # Password label
        self.password_entry = tk.Entry(self, show='*')  # Password entry field (hidden)
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.handle_login).pack(pady=5)  # Login button
        tk.Button(self, text="Sign Up", command=self.create_signup_screen).pack(pady=5)  # Sign up button

    def create_signup_screen(self):
        # Function to create the sign-up screen
        for widget in self.winfo_children():
            widget.destroy()  # Clear the window

        tk.Label(self, text="Username").pack(pady=5)  # Username label
        self.username_entry = tk.Entry(self)  # Username entry field
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Email").pack(pady=5)  # Email label
        self.email_entry = tk.Entry(self)  # Email entry field
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)  # Password label
        self.password_entry = tk.Entry(self, show='*')  # Password entry field (hidden)
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Sign Up", command=self.handle_signup).pack(pady=5)  # Sign up button
        tk.Button(self, text="Back to Login", command=self.create_login_screen).pack(pady=5)  # Back to login button

    def handle_login(self):
        # Function to handle the login process
        username = self.username_entry.get()  # Get the username
        password = self.password_entry.get()  # Get the password
        if login(username, password):
            # If login is successful, create the main interface
            self.create_main_interface()
        else:
            # If login fails, show an error message
            messagebox.showerror("Error", "Incorrect username or password")

    def handle_signup(self):
        # Function to handle the sign-up process
        username = self.username_entry.get()  # Get the username
        password = self.password_entry.get()  # Get the password
        email = self.email_entry.get()  # Get the email
        if signup(username, password, email):
            # If sign-up is successful, show a success message and go back to the login screen
            messagebox.showinfo("Success", "User signed up successfully!")
            self.create_login_screen()
        else:
            # If sign-up fails, show an error message
            messagebox.showerror("Error", "Username or email already exists")

    def create_main_interface(self):
        # Function to create the main interface after a successful login
        self.title("Coeus AI - Main Interface")  # Set the window title
        for widget in self.winfo_children():
            widget.destroy()  # Clear the window
        tk.Label(self, text="Welcome to Coeus AI!").pack(pady=20)  # Welcome message
        # Add your main interface components here

if __name__ == '__main__':
    from database import setup_database  # Import setup_database function from database.py
    setup_database()  # Set up the database
    app = CoeusAIApp()  # Create an instance of CoeusAIApp
    app.mainloop()  # Start the Tkinter event loop
