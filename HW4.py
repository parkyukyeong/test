#5

ss = 'Python'
for i in range(0,len(ss)):
    print(ss[i]+'$',end='')

#11
print('')
input_value = ''
result = ''
input_value = input('문자열 입력하세요=')
for i in input_value :
    if i.isdigit():
        continue
    elif i.isalpha():
        result += i
    

print(result)


#9

inStr,outStr = "Python",""
strLen = len(inStr)

for i in range(0,strLen):
    outStr += inStr[strLen-i-1]

print("내용을 거꾸로 출력 --> %s" % outStr)

#13
import turtle
import random
from tkinter.simpledialog import *
import math

inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0, 0, 20
radius, angle, radian = 200, 0, 0

turtle.title('거북이가 나선모양의 글자쓰기')
turtle.shape('turtle')
#turtle.setup(width = swidth+150, height = sheight+150)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr = askstring('문자열입력','거북이가 쓸 문자열을 입력')
Length = len(inStr)
theta = 360*2/Length
delta = swidth/3 /Length

def random_color():
    list = ["red", "blue", "green", "yellow", "black"]
    return random.choice(list)

for character in inStr:
    radian = 3.14*angle/180
    tX = radius*math.cos(radian)
    tY = radius*math.sin(radian)
    turtle.goto(tX,tY)
    turtle.pencolor(random_color())
    turtle.write(character, font=('맑은 고딕', txtSize, 'bold'))
    angle += theta
    radius -= delta

 

