import turtle as t

def main():
    word = input ("What word should be drawn?")
    color = input ("What color should be drawn?")
    screen = t.Screen()
    screen.bgcolor('white')
    pen = t.Turtle()
    pen.speed(1)
    pen.pencolor(color)
    pen.goto (100,100)
    for letter in word:
        pen.forward (200)
        pen.left(90)


    t.mainloop()


if __name__ == "__main__":
    main()