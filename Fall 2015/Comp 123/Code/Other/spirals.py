import turtle


def spiral1():
   s2=turtle.Screen()
   t2=turtle.Turtle()   
   t2.speed(0)
   t2.shape("blank")
   for i in range(1,99):
      t2.left(10)
      t2.forward(i)
      t2.right(60)
      if i != 98:
         t2.forward(i*2)
   t2.forward(65)   
   s2.exitonclick()
   
def spiral2():
   s=turtle.Screen()
   t=turtle.Turtle()
   t.speed(0)
   t.shape("blank")  
   t.color("darkred")
   for i in range(1,287):
      t.left(10)
      t.forward(i/4)
      t.right(90)
      t.forward(i/4)
      t.right(60)
      t.pu()
      t.forward(i*2)   
      t.pd()
   s.exitonclick()
         
spiral2()


spiral1()