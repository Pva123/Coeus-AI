from ui import CoeusAIApp
from database import setup_database

if __name__ == '__main__':
    setup_database()
    app = CoeusAIApp()
    app.mainloop()
