import tkinter as tk
from tkinter import ttk

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, width, height, radius=25, color="#3a4759", hover_color="#5a6789", **kwargs):
        tk.Canvas.__init__(self, parent, width=width, height=height, bg='#0b1e3d', highlightthickness=0, **kwargs)
        self.radius = radius
        self.color = color
        self.hover_color = hover_color
        self.rect = self.create_rounded_rectangle(0, 0, width, height, radius, fill=color)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1, x1+radius, y1,
                  x2-radius, y1, x2-radius, y1,
                  x2, y1, x2, y1+radius,
                  x2, y2-radius, x2, y2-radius,
                  x2, y2, x2-radius, y2,
                  x1+radius, y2, x1+radius, y2,
                  x1, y2, x1, y2-radius,
                  x1, y1+radius, x1, y1+radius,
                  x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True)

    def _on_enter(self, event):
        self.itemconfig(self.rect, fill=self.hover_color)

    def _on_leave(self, event):
        self.itemconfig(self.rect, fill=self.color)

class RoundedButton(RoundedFrame):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(parent, **kwargs)
        self.command = command
        self.text_id = self.create_text(self.winfo_reqwidth() // 2, self.winfo_reqheight() // 2, text=text, fill="white", font=("Helvetica", 10, "bold"))
        self.bind("<Button-1>", self._on_click)

    def _on_click(self, event):
        self.command()

class CoeusAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coeus AI")
        self.root.geometry("1000x700")
        self.root.configure(bg='#0b1e3d')

        # Create main layout
        self.create_layout()

    def create_layout(self):
        # Left frame for buttons
        self.left_frame = tk.Frame(self.root, bg='#0b1e3d')
        self.left_frame.pack(side='left', fill='y', padx=10, pady=10)

        # Right frame for content
        self.right_frame = tk.Frame(self.root, bg='#263859')
        self.right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        self.create_buttons()
        self.create_content()

    def create_buttons(self):
        
        chat_btn = RoundedButton(self.left_frame, text="💬", command=self.open_chat, width=80, height=50, radius=25, color="#3a4759", hover_color="#5a6789")
        chat_btn.pack(pady=10)
        
        calendar_btn = RoundedButton(self.left_frame, text="⌨️", command=self.open_calendar, width=80, height=50, radius=25, color="#3a4759", hover_color="#5a6789")
        calendar_btn.pack(pady=10)

        spacer_frame = tk.Frame(self.left_frame, bg='#0b1e3d')
        spacer_frame.pack(expand=True, fill='both')

        settings_btn = RoundedButton(self.left_frame, text="⚙️", command=self.open_settings, width=80, height=50, radius=25, color="#3a4759", hover_color="#5a6789")
        settings_btn.pack(side='bottom', pady=10)
        
        

    def create_content(self):
        # Top frame for schedule
        self.schedule_frame = tk.Frame(self.right_frame, bg='#263859', bd=2, relief='groove')
        self.schedule_frame.pack(pady=10, padx=10, fill='x')

        title = tk.Label(self.schedule_frame, text="Today's Schedule", bg='#263859', fg='white', font=('Helvetica', 14, 'bold'))
        title.pack(pady=10)

        # Placeholder for schedule items
        for _ in range(3):
            item = RoundedFrame(self.schedule_frame, width=400, height=50, radius=25, color="#3a4759", hover_color="#5a6789")
            item.pack(pady=5, padx=5)

        # Bottom frame for todo list
        self.todo_frame = tk.Frame(self.right_frame, bg='#263859', bd=2, relief='groove')
        self.todo_frame.pack(pady=10, padx=10, fill='x')

        title = tk.Label(self.todo_frame, text="Today's Todo List", bg='#263859', fg='white', font=('Helvetica', 14, 'bold'))
        title.pack(pady=10)

        # Placeholder for todo items with action buttons
        for _ in range(4):
            item_frame = RoundedFrame(self.todo_frame, width=400, height=50, radius=25, color="#3a4759", hover_color="#5a6789")
            item_frame.pack(pady=5, padx=10, fill='x')
            
            item_label = tk.Label(item_frame, text="Todo Item", bg='#3a4759', fg='white')
            item_frame.create_window(10, 25, anchor='w', window=item_label)
            
            complete_btn = RoundedButton(item_frame, text="✓", command=self.complete_task, width=30, height=30, radius=15, color="#3a4759", hover_color="#5a6789")
            item_frame.create_window(350, 25, anchor='center', window=complete_btn)
            
            delete_btn = RoundedButton(item_frame, text="✕", command=self.delete_task, width=30, height=30, radius=15, color="#3a4759", hover_color="#5a6789")
            item_frame.create_window(380, 25, anchor='center', window=delete_btn)

    def complete_task(self):
        print("Task completed!")

    def delete_task(self):
        print("Task deleted!")

    def activate_mic(self):
        print("Mic activated!")

    def open_settings(self):
        print("Settings opened!")

    def open_menu(self):
        print("Menu opened!")

    def open_chat(self):
        print("Chat opened!")

    def open_calendar(self):
        print("Calendar opened!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoeusAIApp(root)
    root.mainloop()
