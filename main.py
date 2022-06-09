import turtle

turtle.setup (500,500)
turtle.shape("turtle")
screen = turtle.Screen()




def drawSquare(turtle):
  corners = 0
  while corners < 4:
    turtle.forward(200)
    turtle.right(90)
    corners +=1


def drawArt():
  kaia = turtle.Turtle()
  kaia.color("green")
  kaia.speed(2147483647)
  x = 0
  while x < 36:
    drawSquare(kaia)
    kaia.right(10)
    x += 1


  komi = turtle.Turtle()
  komi.color("blue")
  komi.speed(2147483647)
  x = 0
  while x < 300:
    komi.forward(x)
    komi.right(91)
    x += 1

    
drawArt()
