import datetime

def feature1():
    print("feature1")



now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

import turtle

skk = turtle.Turtle()

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()

import calendar

yy = 2021
mm = 12

print(calendar.month(yy, mm))




