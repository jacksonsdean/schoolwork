import turtle

scrn = turtle.Screen()

carl = turtle.Turtle()
carl.goto(-75,0)
carl.shape("turtle")
carl.color("darkred")
for i in range(5):
    carl.forward(150)
    carl.left(144)
carl.right(73)   
carl.circle(79) 
carl.shape("blank")

lori = turtle.Turtle()
lori.color("darkred")
lori.shape("blank")
lori.pu()
lori.goto(-30,-100)
lori.speed(1)
lori.write("Drink Blood",font=(30))
lori.goto(-30,-150)
lori.write("Smoke Crack",font=(30))
lori.goto(-30,-200)
lori.write("Worship Satin",font=(30))
lori.goto(-30,-250)
lori.write("GO MAC",font=(230))
lori.goto(0,-300)
scrn.exitonclick()
    
    