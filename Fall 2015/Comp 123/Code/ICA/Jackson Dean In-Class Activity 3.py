import turtle
s= turtle.Screen()
s.bgcolor("skyblue")

gt = turtle.Turtle()
gt.speed(0)
gt.shape("blank")
gt.pu()

gt.goto(-800,-300)
gt.color("darkgreen")
gt.pd()
gt.begin_fill()
gt.forward(1500)
gt.right(90)
gt.forward(200)
gt.right(90)
gt.forward(1500)
gt.right(90)
gt.forward(200)
gt.end_fill()
t = turtle.Turtle()
t.speed(0)
t.color("chocolate")
t.shape("blank")
t.right(90)
t.begin_fill()
for i in range(10):
    t.forward(35)
    t.left(4)
    
t.left(230)
t.forward(340)

t.left(230)
for i in range(10):
    t.forward(35)
    t.left(4)
t.right(90)
t.forward(100)
t.end_fill()
t.color("green")
t.pu
t.goto(-100,-60)
t.pd
t.pensize(40)
for i in range(200):
    t.left(i)
    t.pu
    t.forward(i+10)
    t.pd
    t.circle(70)
st = turtle.Turtle()

st.color("yellow")
st.shape("blank")
st.pensize(30)
st.pu()

st.goto(350,250)
st.shape("circle")
st.pd()
st.speed(0)
st.begin_fill()

st.circle(80)
st.end_fill()





s.exitonclick()
