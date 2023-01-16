from random import randint
import curses

win = curses.initscr()
h, w = win.getmaxyx()
win.keypad(True), win.timeout(100), curses.curs_set(0)

x, y = food = w // 2, h // 2
snake = [(x - 2, y), (x - 1, y), (x, y)]
key = curses.KEY_RIGHT

while 0 < x < w - 1 and 0 < y < h - 1 and snake[0] not in snake[1:]:
    if (x, y) == food:
        food = randint(1, w - 2), randint(1, h - 2)
        win.addch(food[1], food[0], "*")
    else:
        last = snake.pop(0)
        win.addch(last[1], last[0], " ")

    new_key = win.getch()
    key = key if new_key == -1 else new_key

    if key == curses.KEY_RIGHT: x += 1
    if key == curses.KEY_LEFT:  x -= 1
    if key == curses.KEY_DOWN:  y += 1
    if key == curses.KEY_UP:    y -= 1

    snake.append((x, y))
    win.addch(y, x, "#")
