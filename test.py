import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt

class FadingButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMouseTracking(True)
        self.animation_timer = QTimer()
        self.animation_timer.setInterval(30)
        self.animation_timer.timeout.connect(self.update_alpha)
        self.alpha = 1.0
        self.hovered = False

    def enterEvent(self, event):
        self.hovered = True
        self.animation_timer.start()

    def leaveEvent(self, event):
        self.hovered = False

    def update_alpha(self):
        if self.hovered:
            self.alpha = min(1.0, self.alpha + 0.1)
        else:
            self.alpha = max(0.0, self.alpha - 0.1)
        
        self.setStyleSheet(f"background-color: rgba(0, 0, 255, {self.alpha});")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle('Fading Button Example')

        button = FadingButton('Hover Me', self)
        button.setGeometry(75, 50, 100, 30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
