from turtle import *
from datetime import *


#表盘绘制函数
def setupClock(radius):
    """
    Docstring for setupClock
    """
    #建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i%5==0:
            forward(20)#短线段
            Skip(-radius-20)
        else:
            dot(5)#小原点
            Skip(-radius)
        right(6)

#跨越函数
def Skip(step):
    """
    Docstring for Skip(step)"""
    penup()
    forward(step)
    pendown()
#定义表针函数
def mkHand(name,length):
    """
    Docstring for mkHand
    """
    #注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm=get_poly()
    register_shape(name,handForm)

def init():
    global secHand,minHand,hurHand,printer
    mode("logo")#重置Turtle指向北
    #建立三个表针Turtle并初始化
    mkHand("secHand",125)
    mkHand("minHand",130)
    mkHand("hurHand",90)
    secHand=Turtle()
    secHand.shape("secHand")
    minHand=Turtle()
    minHand.shape("minHand")
    hurHand=Turtle()
    hurHand.shape("hurHand")
    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,3)
        hand.speed(0)
    #建立输出文字Turtle
    printer=Turtle()
    printer.hideturtle()
    printer.penup()
def week(date):
  week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
  }
  day = date.weekday()
  return week_day_dict[day]
#更新时钟函数
def tick():
    # 绘制表针的动态显示
    t=datetime.today()
    second=t.second+t.microsecond*0.000001
    minute=t.minute+second/60.0
    hour=t.hour+minute/60.0

    tracer(False)
    printer.forward(65)
    printer.write(week(t),align="center",font=("Courier", 16, "bold"))
    printer.back(130)
    printer.write(t.date(),align="center",font=("Courier", 10, "bold"))
    printer.home()
    tracer(True)
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(6*hour)
    ontimer(tick,100)#每100ms后继续调用tick

def main():
    tracer(False)
    init()
    setupClock(160)
    tracer(True)
    tick()
    mainloop()
if __name__ == '__main__':
    main()
