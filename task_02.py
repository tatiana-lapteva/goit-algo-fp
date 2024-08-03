"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала 
“дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач 
повинен мати можливість вказати рівень рекурсії.
"""


import turtle


def treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle):
  """ Y Fractal tree """
  if recursionLevel == 0:
    TTL.fd(0)
  else:
    branchLength = branchLength - branchReduction
    TTL.forward(branchLength)
    TTL.left(angle)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.right(angle * 2)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.left(angle)
    TTL.backward(branchLength)


if __name__ == "__main__":
    
    recursion_level = int(input("Entry recursion level (integer): "))
    branch_length = 80
    branch_reduction = 5
    angle = 40
    
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.colormode(255) 

    TTL = turtle.Turtle()
    TTL.speed(0)
    TTL.color("brown") #Set the turtle's color.
    TTL.pensize(3)
    TTL.setposition(0, -100)
    TTL.pendown()
    TTL.hideturtle()
    TTL.setheading(90)

    treeFractal(TTL, recursion_level, branch_length, branch_reduction, angle)

    screen.exitonclick()