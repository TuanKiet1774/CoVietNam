#=====CỜ MẶT TRẬN DÂN TỘC GIẢI PHÓNG MIỀN NAM VIÊT NAM=====
import turtle
import math
import time


FLAG_W, FLAG_H = 600, 400
FPS = 33
phase_speed = 0.15  

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=FLAG_W + 100, height=FLAG_H + 100)
screen.tracer(0)
screen.title("Cờ Mặt Trận Dân Tộc Giải Phóng Miền Nam Việt Nam")

flag_bg = turtle.Turtle()
flag_bg.hideturtle()
flag_bg.speed(0)

flag_star = turtle.Turtle()
flag_star.hideturtle()
flag_star.speed(0)

def draw_flag_background(phase):
    flag_bg.clear()
    
    flag_bg.color("red")
    flag_bg.penup()
    flag_bg.goto(-300, 0)
    flag_bg.pendown()
    flag_bg.begin_fill()
    
    for x in range(-300, 301, 2):  
        wave_middle = 5 * math.sin(x / 50 + phase)
        flag_bg.goto(x, 0 + wave_middle)
    
    for y in range(0, 201, 2):
        wave_right = 10 * math.sin(300 / 50 + phase + y / 100)
        flag_bg.goto(300 + wave_right, y)
    
    for x in range(300, -301, -2):
        wave_top = 10 * math.sin(x / 50 + phase + 0.5)
        flag_bg.goto(x, 200 + wave_top)
    
    for y in range(200, -1, -2):
        wave_left = 10 * math.sin(-300 / 50 + phase + y / 100 + 0.5)
        flag_bg.goto(-300 + wave_left, y)
    
    flag_bg.end_fill()
    
    flag_bg.color("blue")
    flag_bg.penup()
    flag_bg.goto(-300, 0)
    flag_bg.pendown()
    flag_bg.begin_fill()
    
    for x in range(-300, 301, 2):
        wave_middle = 5 * math.sin(x / 50 + phase)
        flag_bg.goto(x, 0 + wave_middle)
    
    for y in range(0, -201, -2):
        wave_right = 10 * math.sin(300 / 50 + phase + y / 100)
        flag_bg.goto(300 + wave_right, y)
    
    for x in range(300, -301, -2):
        wave_bottom = 10 * math.sin(x / 50 + phase)
        flag_bg.goto(x, -200 + wave_bottom)
    
    for y in range(-200, 1, 2):
        wave_left = 10 * math.sin(-300 / 50 + phase + y / 100 + 0.5)
        flag_bg.goto(-300 + wave_left, y)
    
    flag_bg.end_fill()

def draw_star(phase):
    flag_star.clear()
    flag_star.penup()
    flag_star.goto(95, 55)    
    flag_star.setheading(180)  
    flag_star.color("yellow")
    flag_star.begin_fill()
    
    star_size = 87.19 * (0.95 + 0.05 * math.sin(phase * 2.5))
    for _ in range(5):
        flag_star.forward(star_size)
        flag_star.right(72)
        flag_star.forward(star_size)
        flag_star.left(144)
    
    flag_star.end_fill()

phase = 0
try:
    while True:
        draw_flag_background(phase)
        draw_star(phase)
        screen.update()
        phase += phase_speed
        time.sleep(1 / FPS)
except:
    pass
