
from graphics import *
import random
import time


def main():
    win = GraphWin("Three Bouncing Balls", 600, 400)
    win.setBackground("white")

    # Each ball stores: [circle, dx, dy]
    balls = []

    colors = ["red", "blue", "green"]

    for color in colors:
        x = random.randint(50, 550)
        y = random.randint(50, 350)
        radius = 15

        ball = Circle(Point(x, y), radius)
        ball.setFill(color)
        ball.draw(win)

        dx = random.choice([-4, -3, 3, 4])
        dy = random.choice([-4, -3, 3, 4])

        balls.append([ball, dx, dy])

    # Animate all three balls.
    while True:
        for item in balls:
            ball = item[0]
            dx = item[1]
            dy = item[2]

            ball.move(dx, dy)

            center = ball.getCenter()
            x = center.getX()
            y = center.getY()

            # Bounce off the left and right walls.
            if x <= 15 or x >= 585:
                item[1] = -dx

            # Bounce off the top and bottom walls.
            if y <= 15 or y >= 385:
                item[2] = -dy

        time.sleep(0.02)

    win.close()


if __name__ == "__main__":
    main()

        