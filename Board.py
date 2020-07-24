import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Board:
    def __init__(self, height, width, delay):
        self.width = width
        self.height = height
        self.board = np.random.choice(a=[0, 255], p=[.8, .2], size=(width, height))
        self.fig, ax = plt.subplots()
        img = ax.matshow(self.board)
        self.img = img
        self.delay = delay

    def check_spot(self, x, y, newboard):
        count = 0
        pos = np.array([[1, 1], [0, 1], [-1, 1], [-1, 1], [1, 0], [-1, 0], [1, -1], [1, -1]])
        for i in pos:
            count += self.add_number(x + i[0], y + i[1])
        newboard[x, y] = self.is_alive(count, self.board[x, y])

    def start(self):
        ani = animation.FuncAnimation(self.fig, self.update, interval=self.delay)
        plt.show()

    def is_alive(self, count, is_currently_alive):
        if is_currently_alive:
            if count < 2:
                return 0
            elif count == 2 or count == 3:
                return 255
            else:
                return 0
        return (0, 255)[count == 3]

    def update(self, i):
        newBoard = np.zeros((self.width, self.height), dtype=int)
        for x in range(self.width):
            for y in range(self.height):
                self.check_spot(x, y, newBoard)
        self.board = newBoard

        self.img.set_data(self.board)
        return [self.img]

    def add_number(self, x, y):
        return int(self.within_board(x, y) and self.board[x, y] == 255)

    def within_board(self, x, y):
        return (x > -1) and (y > -1) and (x < self.width) and (y < self.height)
