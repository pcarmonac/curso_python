import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QTimer

class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.snake = [(200, 200)]
        self.direction = (0, -20)
        self.food = self.generate_food()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_snake)
        self.timer.start(100)

    def generate_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                return (x, y)

    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if (new_head == self.food):
            self.snake.insert(0, new_head)
            self.food = self.generate_food()
        else:
            self.snake = [new_head] + self.snake[:-1]

        self.check_collision()
        self.update()

    def check_collision(self):
        head = self.snake[0]
        if (head in self.snake[1:] or
            head[0] < 0 or head[0] >= 400 or
            head[1] < 0 or head[1] >= 400):
            self.game_over()

    def game_over(self):
        self.timer.stop()
        print("Game Over!")

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up and self.direction != (0, 20):
            self.direction = (0, -20)
        elif key == Qt.Key_Down and self.direction != (0, -20):
            self.direction = (0, 20)
        elif key == Qt.Key_Left and self.direction != (20, 0):
            self.direction = (-20, 0)
        elif key == Qt.Key_Right and self.direction != (-20, 0):
            self.direction = (20, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)

        painter.setBrush(Qt.green)
        for segment in self.snake:
            painter.drawRect(segment[0], segment[1], 20, 20)

        painter.setBrush(Qt.red)
        painter.drawRect(self.food[0], self.food[1], 20, 20)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snake Game")
        self.game = SnakeGame()
        self.setCentralWidget(self.game)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())