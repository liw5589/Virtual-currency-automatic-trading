# import turtle as tt
#
#
#
# tt.bgcolor("black")
# tt.pensize(2)
#
# def curve():
#     for i in range(200):
#         tt.right(1)
#         tt.forward(1)
#
# tt.speed(10)
# tt.color("red","pink")
#
# tt.begin_fill()
# tt.left(140)
# tt.forward(111.65)
# curve()
#
# tt.left(120)
# curve()
# tt.forward(111.65)
# tt.end_fill()
#
# tt.exitonclick()

import pyautogui as pag
while True:
    x,y =  pag.position()
    position_str = "X : " + str(x) +"Y : " + str(y)
    print(position_str)
    #660,520