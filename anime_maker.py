import customtkinter as ctk
from turtle import *
import turtle

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("395x545")
app.configure(fg_color="#555555")
app.title("Anime Maker!!")

lbl = ctk.CTkLabel(
    app,
    text="Go in Full screen to\nWatch the whole Drawing!\nCan draw only two drawing at once!\nClose the canvas and go!",
    font=("Algera", 18),
)
lbl.pack(pady=20)


def doraemon():
    # Doraemon with Python Turtle
    def ankur(x, y):
        penup()
        goto(x, y)
        pendown()

    def aankha():
        fillcolor("#ffffff")
        begin_fill()

        tracer(False)
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                lt(3)
                fd(a)
            else:
                a += 0.05
                lt(3)
                fd(a)
        tracer(True)
        end_fill()

    def daari():
        ankur(-32, 135)
        seth(165)
        fd(60)

        ankur(-32, 125)
        seth(180)
        fd(60)

        ankur(-32, 115)
        seth(193)
        fd(60)

        ankur(37, 135)
        seth(15)
        fd(60)

        ankur(37, 125)
        seth(0)
        fd(60)

        ankur(37, 115)
        seth(-13)
        fd(60)

    def mukh():
        ankur(5, 148)
        seth(270)
        fd(100)
        seth(0)
        circle(120, 50)
        seth(230)
        circle(-120, 100)

    def muflar():
        fillcolor("#ff0011")
        begin_fill()
        seth(0)
        fd(200)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        fd(207)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        end_fill()

    def nak():
        ankur(-10, 158)
        seth(315)
        fillcolor("#ff0011")
        begin_fill()
        circle(20)
        end_fill()

    def black_aankha():
        seth(0)
        ankur(-20, 195)
        fillcolor("#000000")
        begin_fill()
        circle(13)
        end_fill()

        pensize(6)
        ankur(20, 205)
        seth(75)
        circle(-10, 150)
        pensize(3)

        ankur(-17, 200)
        seth(0)
        fillcolor("#ffffff")
        begin_fill()
        circle(5)
        end_fill()
        ankur(0, 0)

    def face():
        fd(183)
        lt(45)
        fillcolor("#ffffff")
        begin_fill()
        circle(120, 100)
        seth(180)
        # print(pos())
        fd(121)
        pendown()
        seth(215)
        circle(120, 100)
        end_fill()
        ankur(63.56, 218.24)
        seth(90)
        aankha()
        seth(180)
        penup()
        fd(60)
        pendown()
        seth(90)
        aankha()
        penup()
        seth(180)
        fd(64)

    def taauko():
        penup()
        circle(150, 40)
        pendown()
        fillcolor("#00b7ff")
        begin_fill()
        circle(150, 280)
        end_fill()

    def Doraemon():
        taauko()

        muflar()

        face()

        nak()

        mukh()

        daari()

        ankur(0, 0)

        seth(0)
        penup()
        circle(150, 50)
        pendown()
        seth(30)
        fd(40)
        seth(70)
        circle(-30, 270)

        fillcolor("#00b7ff")
        begin_fill()

        seth(230)
        fd(80)
        seth(90)
        circle(1000, 1)
        seth(-89)
        circle(-1000, 10)

        # print(pos())

        seth(180)
        fd(70)
        seth(90)
        circle(30, 180)
        seth(180)
        fd(70)

        # print(pos())
        seth(100)
        circle(-1000, 9)

        seth(-86)
        circle(1000, 2)
        seth(230)
        fd(40)

        # print(pos())

        circle(-30, 230)
        seth(45)
        fd(81)
        seth(0)
        fd(203)
        circle(5, 90)
        fd(10)
        circle(5, 90)
        fd(7)
        seth(40)
        circle(150, 10)
        seth(30)
        fd(40)
        end_fill()

        seth(70)
        fillcolor("#ffffff")
        begin_fill()
        circle(-30)
        end_fill()

        ankur(103.74, -182.59)
        seth(0)
        fillcolor("#ffffff")
        begin_fill()
        fd(15)
        circle(-15, 180)
        fd(90)
        circle(-15, 180)
        fd(10)
        end_fill()

        ankur(-96.26, -182.59)
        seth(180)
        fillcolor("#ffffff")
        begin_fill()
        fd(15)
        circle(15, 180)
        fd(90)
        circle(15, 180)
        fd(10)
        end_fill()

        ankur(-133.97, -91.81)
        seth(50)
        fillcolor("#ffffff")
        begin_fill()
        circle(30)
        end_fill()
        # Doraemon with Python Turtle

        ankur(-103.42, 15.09)
        seth(0)
        fd(38)
        seth(230)
        begin_fill()
        circle(90, 260)
        end_fill()

        ankur(5, -40)
        seth(0)
        fd(70)
        seth(-90)
        circle(-70, 180)
        seth(0)
        fd(70)

        ankur(-103.42, 15.09)
        fd(90)
        seth(70)
        fillcolor("#ffd200")
        # print(pos())
        begin_fill()
        circle(-20)
        end_fill()
        seth(170)
        fillcolor("#ffd200")
        begin_fill()
        circle(-2, 180)
        seth(10)
        circle(-100, 22)
        circle(-2, 180)
        seth(180 - 10)
        circle(100, 22)
        end_fill()
        goto(-13.42, 15.09)
        seth(250)
        circle(20, 110)
        seth(90)
        fd(15)
        dot(10)
        ankur(0, -150)

        black_aankha()

    if __name__ == "__main__":
        screensize(800, 600, "#f0f0f0")
        pensize(3)
        speed(9)
        Doraemon()
        ankur(100, -300)
        mainloop()


def shinchan():
    wn = turtle.Screen()
    wn.setup(width=1000, height=700)
    speed(5)
    turtle.title("Shinchan")

    def myPosition(x, y):
        penup()
        goto(x, y)
        pendown()

    pensize(2)

    def short():
        fillcolor("#fbff00")
        begin_fill()
        right(25)
        forward(20)
        right(45)
        forward(20)
        left(70)
        forward(90)
        left(95)
        forward(75)
        left(85)
        forward(175)
        left(85)
        forward(75)
        left(95)
        forward(90)
        left(85)
        forward(18)
        end_fill()

    def leftLeg():
        myPosition(-39, -25)
        fillcolor("#ffd699")
        begin_fill()
        right(89)
        forward(25)
        right(90)
        forward(50)
        right(90)
        forward(20)
        right(85)
        forward(50)
        end_fill()

    def leftSock():
        myPosition(-36, -78)
        fillcolor("#ffffff")
        begin_fill()
        right(90)
        circle(80, 13)
        right(110)
        forward(22)
        right(85)
        forward(19)
        right(90)
        forward(21)
        end_fill()

    def leftShoe():
        myPosition(-69, -112)
        fillcolor("#fbff00")
        begin_fill()
        right(90)
        left(5)
        forward(56)
        left(105)
        forward(13)
        left(75)
        forward(20)
        right(90)
        forward(15)
        circle(10, 15)
        left(80)
        forward(4)
        circle(10, 15)
        left(40)
        circle(20, 15)
        forward(10)
        right(45)
        forward(15)
        circle(25, 25)
        end_fill()

    def rightLeg():
        myPosition(60, -28)
        fillcolor("#ffd699")
        begin_fill()
        # right(90)
        left(128)
        forward(25)
        right(95)
        forward(55)
        right(90)
        forward(20)
        right(85)
        forward(55)
        end_fill()

    def rightSock():
        myPosition(64, -79)
        fillcolor("#ffffff")
        begin_fill()
        right(90)
        circle(90, 14)
        right(110)
        forward(23)
        right(90)
        forward(15)
        right(80)
        forward(21)
        end_fill()

    def rightShoe():
        myPosition(64, -108)
        fillcolor("#fbff00")
        begin_fill()
        right(100)
        forward(56)
        left(160)
        forward(25)
        right(68)
        forward(17)
        left(90)
        circle(18, 15)
        forward(5)
        left(75)
        forward(11)
        right(85)
        forward(20)
        left(45)
        circle(10, 30)
        left(25)
        forward(5)
        end_fill()

    def myShirt():
        myPosition(-75, 48)
        fillcolor("#ff0000")
        begin_fill()
        left(72)
        forward(185)
        left(87)
        forward(75)
        right(68)
        circle(20, 8)
        circle(300, 23)
        left(90)
        circle(35, 17)
        right(38)
        circle(35, 17)
        left(58)
        forward(75)
        right(12)
        forward(140)
        right(40)
        forward(93)
        left(120)
        circle(-20, 65)
        left(75)
        forward(10)
        left(23)
        forward(88)
        # circle(-80,10)
        right(31)
        forward(87)
        right(180)
        forward(108)
        right(180)
        forward(104)
        circle(10, 70)
        end_fill()

    def myHead():
        myPosition(-20, 295)
        left(20)
        pensize(2)
        fillcolor("#fcc6a0")
        begin_fill()
        right(90)
        forward(40)
        right(90)
        circle(50, 80)
        left(10)
        circle(50, 80)
        left(2)
        circle(200, 50)

        left(48)
        forward(60)
        # left(20)
        circle(45, 60)
        right(5)
        circle(100, 85)
        end_fill()
        fillcolor("black")
        begin_fill()

        pensize(2)
        right(170)
        circle(-100, 165)
        right(78)
        forward(26)
        right(87)
        forward(55)
        circle(45, 60)
        right(5)
        circle(100, 85)
        end_fill()

        fillcolor("#fcc6a0")
        begin_fill()
        right(180)
        circle(-100, 105)
        right(37)
        forward(49)
        pensize(2)
        left(130)
        forward(30)
        # right(5)
        circle(-10, 70)
        right(50)
        # circle(10,10)
        forward(36)
        right(80)
        forward(50)
        pencolor("#fcc6a0")
        right(90)
        forward(30)

        end_fill()

    def rightHand():
        # left(35)
        myPosition(197, 209)
        pencolor("black")
        fillcolor("#fcc6a0")
        begin_fill()
        right(45)
        forward(6)
        left(55)
        forward(20)
        circle(-5, 70)
        right(100)
        forward(18)
        left(105)
        forward(18)
        circle(-5, 70)
        right(100)
        forward(18)
        left(145)
        forward(15)
        circle(-5, 70)
        right(100)
        forward(18)

        left(150)
        forward(13)
        circle(-5, 70)
        right(100)
        forward(15)

        left(150)
        forward(10)
        circle(-5, 70)
        right(100)
        forward(12)
        circle(60, 10)
        left(45)
        forward(6)
        right(90)
        forward(10)
        end_fill()

    def leftHand():
        myPosition(-94, 242)
        fillcolor("#fcc6a0")
        begin_fill()
        right(10)
        forward(6)
        left(90)
        penup()
        forward(12)
        pendown()
        left(90)
        forward(8)
        left(90)
        forward(12)
        end_fill()

    def myBis():
        myPosition(-103, 291)
        right(90)
        fillcolor("#02d302")
        begin_fill()
        right(90)
        forward(55)
        left(80)
        forward(12)
        left(10)
        forward(17)
        left(10)
        forward(12)
        left(80)
        forward(55)
        left(80)
        forward(12)
        left(10)
        forward(17)
        left(10)
        forward(12)
        left(80)
        left(80)
        forward(12)
        left(10)
        forward(17)
        left(10)
        forward(12)
        end_fill()
        penup()
        right(100)
        forward(20)
        right(90)
        forward(14)
        pendown()
        pencolor("#9c5e4a")
        fillcolor("#9c5e4a")
        begin_fill()
        for i in range(5):
            forward(15)
            right(144)
        end_fill()
        penup()
        forward(27)
        left(90)
        forward(16)
        left(90)
        forward(7)
        pendown()
        fillcolor("#9c5e4a")
        begin_fill()
        for i in range(5):
            forward(10)
            right(144)
        end_fill()
        penup()
        forward(20)
        right(90)
        forward(5)
        pendown()
        fillcolor("#9c5e4a")
        begin_fill()
        for i in range(5):
            forward(10)
            right(144)
        end_fill()
        penup()
        right(180)
        forward(6)
        pendown()
        fillcolor("#9c5e4a")
        begin_fill()
        for i in range(5):
            forward(10)
            right(144)
        end_fill()

    def leftHand2():
        myPosition(-112, 284)
        pencolor("black")
        fillcolor("#fcc6a0")
        begin_fill()
        right(180)
        forward(31)
        left(90)
        for i in range(2):
            circle(4, 90)
            # circle(4//2,45)
        for i in range(3):
            right(180)
            for i in range(2):
                circle(4, 90)
        end_fill()

    def myMouth():
        myPosition(-25, 200)
        left(65)
        fillcolor("#77332e")
        begin_fill()
        # circle(20)
        # forward(20)
        for i in range(2):
            circle(25, 90)
            circle(25 // 2, 90)
        end_fill()

    def myEyebrow(x, y):
        myPosition(x, y)
        pensize(18)
        right(150)
        forward(25)
        right(90)
        for i in range(1):
            right(45)
            dot(15)
        left(55)
        forward(25)
        for i in range(1):
            right(45)
            dot(15)

    def myEyelid(x, y):
        myPosition(x, y)
        pensize(2)
        left(170)
        circle(-23, 180)

    def myallEyes1(x, y):
        myPosition(x, y)
        right(90)
        fillcolor("#000000")
        begin_fill()
        circle(18)
        end_fill()
        left(90)
        penup()
        forward(19)
        right(90)
        forward(7)
        pendown()
        fillcolor("#ffffff")
        begin_fill()
        left(90)
        circle(9)
        end_fill()

    def myallEyes2(x, y):
        myPosition(x, y)
        right(90)
        fillcolor("#000000")
        begin_fill()
        circle(18)
        end_fill()
        left(90)
        penup()
        forward(19)
        right(90)
        forward(8)
        pendown()
        fillcolor("#ffffff")
        begin_fill()
        left(90)
        circle(9)
        end_fill()

    def allLegs():
        leftLeg()
        leftSock()
        leftShoe()
        rightLeg()
        rightSock()
        rightShoe()

    def allHands():
        rightHand()
        leftHand()
        myBis()
        leftHand2()

    def allEyebrows():
        myEyebrow(-8, 300)
        right(90)
        myEyebrow(72, 300)
        myEyelid(-8, 270)
        left(15)
        myEyelid(68, 265)

    def allEyes():
        myallEyes1(17, 275)
        myallEyes2(95, 270)

    def my_goto(x, y):
        penup()
        goto(x, y)
        pendown()

    short()
    allLegs()
    myShirt()
    myHead()
    allHands()
    myMouth()
    allEyebrows()
    allEyes()
    ht()
    done()


def pikachu():
    t = turtle.Turtle()

    def noTrace_goto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def leftEye(x, y):
        noTrace_goto(x, y)
        t.seth(0)
        t.fillcolor("#333333")
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        noTrace_goto(x, y + 10)
        t.fillcolor("#000000")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        noTrace_goto(x + 6, y + 22)
        t.fillcolor("#ffffff")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def rightEye(x, y):
        noTrace_goto(x, y)
        t.seth(0)
        t.fillcolor("#333333")
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        noTrace_goto(x, y + 10)
        t.fillcolor("#000000")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        noTrace_goto(x - 6, y + 22)
        t.fillcolor("#ffffff")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mouth(x, y):
        noTrace_goto(x, y)

        t.fillcolor("#88141D")
        t.begin_fill()

        l1 = []
        l2 = []
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)
            l1.append(t.position())

        noTrace_goto(x, y)

        t.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
            l2.append(t.position())

        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)

        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

        noTrace_goto(17, 54)
        t.fillcolor("#DD716F")
        t.begin_fill()
        t.seth(145)
        t.circle(40, 86)
        t.penup()
        for pos in reversed(l1[:20]):
            t.goto(pos[0], pos[1] + 1.5)
        for pos in l2[:20]:
            t.goto(pos[0], pos[1] + 1.5)
        t.pendown()
        t.end_fill()

        noTrace_goto(-17, 94)
        t.seth(8)
        t.fd(4)
        t.back(8)

    def leftCheek(x, y):
        turtle.tracer(False)
        noTrace_goto(x, y)
        t.seth(300)
        t.fillcolor("#DD4D28")
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def rightCheek(x, y):
        turtle.tracer(False)
        noTrace_goto(x, y)
        t.seth(60)
        t.fillcolor("#DD4D28")
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def colorLeftEar(x, y):
        noTrace_goto(x, y)
        t.fillcolor("#000000")
        t.begin_fill()
        t.seth(330)
        t.circle(100, 35)
        t.seth(219)
        t.circle(-300, 19)
        t.seth(110)
        t.circle(-30, 50)
        t.circle(-300, 10)
        t.end_fill()

    def colorRightEar(x, y):
        noTrace_goto(x, y)
        t.fillcolor("#000000")
        t.begin_fill()
        t.seth(300)
        t.circle(-100, 30)
        t.seth(35)
        t.circle(300, 15)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 17)
        t.end_fill()

    def body():
        t.fillcolor("#FFD000")
        t.begin_fill()
        # right face
        t.penup()
        t.circle(130, 40)
        t.pendown()
        t.circle(100, 105)
        t.left(180)
        t.circle(-100, 5)

        # right ear
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 36)

        # upper face
        t.seth(150)
        t.circle(150, 70)

        # left ear
        t.seth(200)
        t.circle(300, 40)
        t.circle(30, 50)
        t.seth(20)
        t.circle(300, 35)
        # print(t.pos())

        # left face
        t.seth(240)
        t.circle(105, 95)
        t.left(180)
        t.circle(-105, 5)

        # left hand
        t.seth(210)
        t.circle(500, 18)
        t.seth(200)
        t.fd(10)
        t.seth(280)
        t.fd(7)
        t.seth(210)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(220)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(240)
        t.fd(12)
        t.seth(0)
        t.fd(13)
        t.seth(240)
        t.circle(10, 70)
        t.seth(10)
        t.circle(10, 70)
        t.seth(10)
        t.circle(300, 18)

        t.seth(75)
        t.circle(500, 8)
        t.left(180)
        t.circle(-500, 15)
        t.seth(250)
        t.circle(100, 65)

        # left foot
        t.seth(320)
        t.circle(100, 5)
        t.left(180)
        t.circle(-100, 5)
        t.seth(220)
        t.circle(200, 20)
        t.circle(20, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(300)
        t.circle(10, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(10)
        t.circle(100, 60)

        # left
        t.seth(180)
        t.circle(-100, 10)
        t.left(180)
        t.circle(100, 10)
        t.seth(5)
        t.circle(100, 10)
        t.circle(-100, 40)
        t.circle(100, 35)
        t.left(180)
        t.circle(-100, 10)

        # right foot
        t.seth(290)
        t.circle(100, 55)
        t.circle(10, 50)

        t.seth(120)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(0)
        t.circle(10, 50)

        t.seth(110)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(30)
        t.circle(20, 50)

        t.seth(100)
        t.circle(100, 40)

        # right body
        t.seth(200)
        t.circle(-100, 5)
        t.left(180)
        t.circle(100, 5)
        t.left(30)
        t.circle(100, 75)
        t.right(15)
        t.circle(-300, 21)
        t.left(180)
        t.circle(300, 3)

        # right hand
        t.seth(43)
        t.circle(200, 60)

        t.right(10)
        t.fd(10)

        t.circle(5, 160)
        t.seth(90)
        t.circle(5, 160)
        t.seth(90)

        t.fd(10)
        t.seth(90)
        t.circle(5, 180)
        t.fd(10)

        t.left(180)
        t.left(20)
        t.fd(10)
        t.circle(5, 170)
        t.fd(10)
        t.seth(240)
        t.circle(50, 30)

        t.end_fill()
        noTrace_goto(130, 125)
        t.seth(-20)
        t.fd(5)
        t.circle(-5, 160)
        t.fd(5)

        # finger
        noTrace_goto(166, 130)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)

        # tail
        noTrace_goto(168, 134)
        t.fillcolor("#FFD000")
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        # print(t.pos())
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        # tail
        t.fillcolor("#923E24")
        noTrace_goto(126.82, -156.84)
        t.begin_fill()

        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(40)
        t.pencolor("#923e24")
        t.seth(-30)
        t.fd(30)
        t.left(140)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(150)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(130)
        t.fd(18)
        t.pencolor("#000000")
        t.seth(-45)
        t.fd(67)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)
        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.end_fill()

        # cap、eye、mouse、chin
        cap(-134.07, 147.81)
        mouth(-5, 25)
        leftCheek(-126, 32)
        rightCheek(107, 63)
        colorLeftEar(-250, 100)
        colorRightEar(140, 270)
        leftEye(-85, 90)
        rightEye(50, 110)
        t.hideturtle()

    def cap(x, y):
        noTrace_goto(x, y)
        t.fillcolor("#CD0000")
        t.begin_fill()
        t.seth(200)
        t.circle(400, 7)
        t.left(180)
        t.circle(-400, 30)
        t.circle(30, 60)
        t.fd(50)
        t.circle(30, 45)
        t.fd(60)
        t.left(5)
        t.circle(30, 70)
        t.right(20)
        t.circle(200, 70)
        t.circle(30, 60)
        t.fd(70)
        # print(t.pos())
        t.right(35)
        t.fd(50)
        t.circle(8, 100)
        t.end_fill()
        noTrace_goto(-168.47, 185.52)
        t.seth(36)
        t.circle(-270, 54)
        t.left(180)
        t.circle(270, 27)
        t.circle(-80, 98)

        t.fillcolor("#444444")
        t.begin_fill()
        t.left(180)
        t.circle(80, 197)
        t.left(58)
        t.circle(200, 45)
        t.end_fill()

        noTrace_goto(-58, 270)
        t.pencolor("#228B22")
        t.dot(35)

        noTrace_goto(-30, 280)
        t.fillcolor("#228B22")
        t.begin_fill()
        t.seth(100)
        t.circle(30, 180)
        t.seth(190)
        t.fd(15)
        t.seth(100)
        t.circle(-45, 180)
        t.right(90)
        t.fd(15)
        t.end_fill()
        t.pencolor("#000000")

    t.speed(100)
    body()
    turtle.mainloop()


def peppa_pig():
    def nose(x, y):
        penup()
        goto(x, y)
        pendown()
        setheading(-30)
        begin_fill()
        a = 0.4
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                left(3)
                forward(a)
            else:
                a = a - 0.08
                left(3)
                forward(a)
        end_fill()

        penup()
        setheading(90)
        forward(25)
        setheading(0)
        forward(10)
        pendown()
        pencolor(255, 155, 192)
        setheading(10)
        begin_fill()
        circle(5)
        color(160, 82, 45)
        end_fill()

        penup()
        setheading(0)
        forward(20)
        pendown()
        pencolor(255, 155, 192)
        setheading(10)
        begin_fill()
        circle(5)
        color(160, 82, 45)
        end_fill()

    def head(x, y):
        color((255, 155, 192), "pink")
        penup()
        goto(x, y)
        setheading(0)
        pendown()
        begin_fill()
        setheading(180)
        circle(300, -30)
        circle(100, -60)
        circle(80, -100)
        circle(150, -20)
        circle(60, -95)
        setheading(161)
        circle(-300, 15)
        penup()
        goto(-100, 100)
        pendown()
        setheading(-30)
        a = 0.4
        for i in range(60):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                lt(3)
                fd(a)
            else:
                a = a - 0.08
                lt(3)
                fd(a)
        end_fill()

    def ears(x, y):
        color((255, 155, 192), "pink")
        penup()
        goto(x, y)
        pendown()
        begin_fill()
        setheading(100)
        circle(-50, 50)
        circle(-10, 120)
        circle(-50, 54)
        end_fill()

        penup()
        setheading(90)
        forward(-12)
        setheading(0)
        forward(30)
        pendown()
        begin_fill()
        setheading(100)
        circle(-50, 50)
        circle(-10, 120)
        circle(-50, 56)
        end_fill()

    def eyes():
        color((255, 155, 192), "white")
        penup()
        setheading(90)
        forward(-20)
        setheading(0)
        forward(-95)
        pendown()
        begin_fill()
        circle(15)
        end_fill()

        color("black")
        penup()
        setheading(90)
        forward(12)
        setheading(0)
        forward(-3)
        pendown()
        begin_fill()
        circle(3)
        end_fill()

        color((255, 155, 192), "white")
        penup()
        seth(90)
        forward(-25)
        seth(0)
        forward(40)
        pendown()
        begin_fill()
        circle(15)
        end_fill()

        color("black")
        penup()
        setheading(90)
        forward(12)
        setheading(0)
        forward(-3)
        pendown()
        begin_fill()
        circle(3)
        end_fill()

    def cheek(x, y):
        color((255, 155, 192))
        penup()
        goto(x, y)
        pendown()
        setheading(0)
        begin_fill()
        circle(30)
        end_fill()

    def mouth(x, y):
        color(239, 69, 19)
        penup()
        goto(x, y)
        pendown()
        setheading(-80)
        circle(30, 40)
        circle(40, 80)

    def body(x, y):
        color("red", (255, 99, 71))
        penup()
        goto(x, y)
        pendown()
        begin_fill()
        setheading(-130)
        circle(100, 10)
        circle(300, 30)
        setheading(0)
        forward(230)
        setheading(90)
        circle(300, 30)
        circle(100, 3)
        color((255, 155, 192), (255, 100, 100))
        setheading(-135)
        circle(-80, 63)
        circle(-150, 24)
        end_fill()

    def hands(x, y):
        color((255, 155, 192))
        penup()
        goto(x, y)
        pendown()
        setheading(-160)
        circle(300, 15)
        penup()
        setheading(90)
        forward(15)
        setheading(0)
        forward(0)
        pendown()
        setheading(-10)
        circle(-20, 90)

        penup()
        setheading(90)
        forward(30)
        setheading(0)
        forward(237)
        pendown()
        setheading(-20)
        circle(-300, 15)
        penup()
        setheading(90)
        forward(20)
        setheading(0)
        forward(0)
        pendown()
        setheading(-170)
        circle(20, 90)

    def foot(x, y):
        pensize(10)
        color((240, 128, 128))
        penup()
        goto(x, y)
        pendown()
        setheading(-90)
        forward(40)
        setheading(-180)
        color("black")
        pensize(15)
        fd(20)

        pensize(10)
        color((240, 128, 128))
        penup()
        setheading(90)
        forward(40)
        setheading(0)
        forward(90)
        pendown()
        setheading(-90)
        forward(40)
        setheading(-180)
        color("black")
        pensize(15)
        fd(20)

    def tail(x, y):
        pensize(4)
        color((255, 155, 192))
        penup()
        goto(x, y)
        pendown()
        seth(0)
        circle(70, 20)
        circle(10, 330)
        circle(70, 30)

    def setting():
        pensize(4)
        hideturtle()
        colormode(255)
        color((255, 155, 192), "pink")
        setup(840, 500)
        speed(10)

    def main():
        setting()
        nose(-100, 100)
        head(-69, 167)
        ears(0, 160)
        eyes()
        cheek(80, 10)
        mouth(-20, 30)
        body(-32, -8)
        hands(-56, -45)
        foot(2, -177)
        tail(148, -155)
        done()

    if __name__ == "__main__":
        main()


bt_frame = ctk.CTkFrame(app, fg_color="#555555")
bt_frame.pack(pady=120)

bt1 = ctk.CTkButton(
    bt_frame,
    text="Doraemon",
    width=95,
    height=75,
    command=doraemon,
    fg_color="purple",
    hover_color="blue",
)
bt1.grid(row=0, column=0)

bt2 = ctk.CTkButton(
    bt_frame,
    text="Peppa Pig",
    width=95,
    height=75,
    command=peppa_pig,
    fg_color="purple",
    hover_color="blue",
)
bt2.grid(row=0, column=1, padx=10)

bt3 = ctk.CTkButton(
    bt_frame,
    text="Shinchan",
    width=95,
    height=75,
    command=shinchan,
    fg_color="purple",
    hover_color="blue",
)
bt3.grid(row=1, column=0, pady=10)

bt4 = ctk.CTkButton(
    bt_frame,
    text="Pikachu",
    width=95,
    height=75,
    command=pikachu,
    fg_color="purple",
    hover_color="blue",
)
bt4.grid(row=1, column=1, pady=10, padx=10)

app.mainloop()
