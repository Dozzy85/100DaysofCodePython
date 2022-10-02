# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(246, 244, 243), (232, 238, 245), (240, 245, 243), (246, 238, 241), (134, 166, 202), (219, 148, 108), (198, 136, 148), (33, 42, 60), (44, 104, 150), (235, 212, 94), (142, 183, 163), (163, 61, 50), (151, 58, 65), (35, 60, 54), (53, 111, 91), (212, 81, 70), (229, 162, 167), (168, 30, 34), (157, 33, 31), (234, 168, 157), (17, 98, 70), (56, 52, 49), (54, 46, 50), (170, 186, 220), (193, 99, 107), (30, 61, 112), (38, 150, 207), (108, 127, 155), (176, 199, 188), (64, 66, 57)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()