from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["MediumBlue", "LimeGreen", "DarkOrange", "Indigo", "SaddleBrown", "IndianRed", "SpringGreen", "Aquamarine"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angole = 360 / num_sides
        tim.forward(100)
        tim.right(angole)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

#LEZIONE 169 CHALLANGE 4 DA FARE