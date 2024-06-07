import tkinter as tk 
from tkinter import ttk

class CoeusAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coeus AI")
        self.root.geometry("300x600")
        self.root.configure(bg='#0b1e3d')

        # Main sections
        self.create_schedule_section()
        self.create_todo_section()
        self.create_footer_section()

    def create_schedule_section(self):
        frame = tk.Frame(self.root, bg='#263859')
        frame.pack(pady=10, padx=10, fill='both', expand=True)

        title = tk.Label(frame, text="Today's Schedule", bg='#263859', fg='white', font=('Helvetica', 12, 'bold'))
        title.pack(pady=10)

        # Placeholder for schedule items
        for _ in range(3):
            item = tk.Label(frame, text="", bg='#3a4759', width=30, height=2)
            item.pack(pady=5)

    def create_todo_section(self):
        frame = tk.Frame(self.root, bg='#263859')
        frame.pack(pady=10, padx=10, fill='both', expand=True)

        title = tk.Label(frame, text="Today's Todo List", bg='#263859', fg='white', font=('Helvetica', 12, 'bold'))
        title.pack(pady=10)

        # Placeholder for todo items with action buttons
        for _ in range(4):
            item_frame = tk.Frame(frame, bg='#3a4759')
            item_frame.pack(pady=5, padx=10, fill='x')
            
            item_label = tk.Label(item_frame, text="", bg='#3a4759', width=25, height=2)
            item_label.pack(side='left', padx=5)
            
            complete_btn = tk.Button(item_frame, text="✓", bg='#3a4759', fg='green', borderwidth=0)
            complete_btn.pack(side='right', padx=5)
            
            delete_btn = tk.Button(item_frame, text="✕", bg='#3a4759', fg='red', borderwidth=0)
            delete_btn.pack(side='right')

    def create_footer_section(self):
        frame = tk.Frame(self.root, bg='#0b1e3d')
        frame.pack(side='bottom', pady=10, fill='x')

        title = tk.Label(frame, text="Coeus AI", bg='#0b1e3d', fg='#FFA500', font=('Helvetica', 18, 'bold'))
        title.pack()

        subtitle = tk.Label(frame, text="How can I help you today?", bg='#0b1e3d', fg='white', font=('Helvetica', 10))
        subtitle.pack()

        mic_button = tk.Button(frame, text="🎤", bg='#FFA500', fg='white', font=('Helvetica', 12), borderwidth=0)
        mic_button.pack(pady=10)

        # Placeholder for other footer icons
        icon_frame = tk.Frame(frame, bg='#0b1e3d')
        icon_frame.pack()
        
        settings_btn = tk.Button(icon_frame, text="⚙️", bg='#0b1e3d', fg='white', borderwidth=0)
        settings_btn.pack(side='left', padx=5)
        
        dots_btn = tk.Button(icon_frame, text="⋮", bg='#0b1e3d', fg='white', borderwidth=0)
        dots_btn.pack(side='left', padx=5)
        
        chat_btn = tk.Button(icon_frame, text="💬", bg='#0b1e3d', fg='white', borderwidth=0)
        chat_btn.pack(side='left', padx=5)
        
        keyboard_btn = tk.Button(icon_frame, text="⌨️", bg='#0b1e3d', fg='white', borderwidth=0)
        keyboard_btn.pack(side='left', padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoeusAIApp(root)
    root.mainloop()
