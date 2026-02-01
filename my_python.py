from turtle import *
import colorsys
speed(0)
bgcolor("black")
h = 0
for i in range(20):
    for j in range(20):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        pencolor(c)
        circle(100)
        left(20)
        h += 0.005

        rt(90)
        circle(200 -j *10 ,100)
        lt(90)
        circle(200 -j *10 ,100)
        rt(180)
        circle(40,24)
done(300)