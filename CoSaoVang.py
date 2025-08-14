#=====CỜ ĐỎ SAO VÀNG NƯỚC CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIÊT NAM=====
import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)  
screen.title("Cờ Đỏ Sao Vàng Nước Cộng Hòa Xã Hội Chủ Nghĩa Việt Nam")

flag = turtle.Turtle()
flag.speed(0)  
flag.hideturtle() 

def draw_waving_flag(phase):
    flag.clear()
    
    flag.color("red")
    flag.penup()
    flag.goto(-300, -200)
    flag.pendown()
    flag.begin_fill()
    
    for x in range(-300, 301, 10):
        wave_bottom = 10 * math.sin(x/50 + phase)
        flag.goto(x, -200 + wave_bottom)
    
    for y in range(-200, 201, 10):
        wave_right = 10 * math.sin(300/50 + phase + y/100)
        flag.goto(300, y + wave_right)
    
    for x in range(300, -301, -10):
        wave_top = 10 * math.sin(x/50 + phase + 0.5)
        flag.goto(x, 200 + wave_top)
    
    for y in range(200, -201, -10):
        wave_left = 10 * math.sin(-300/50 + phase + y/100 + 0.5)
        flag.goto(-300, y + wave_left)
    
    flag.end_fill()

    flag.penup()     
    flag.goto(95, 55)    
    flag.setheading(180)  
    flag.color("yellow")
    flag.begin_fill()
    
    star_size = 87.19 * (0.95 + 0.03 * math.sin(phase * 2.5))
    for _ in range(5):
        flag.forward(star_size)
        flag.right(72)
        flag.forward(star_size)
        flag.left(144)
    
    flag.end_fill()

phase = 0
try:
    while True:
        draw_waving_flag(phase)
        screen.update() 
        phase += 0.2 
        time.sleep(0.09)  
except:
    pass  
