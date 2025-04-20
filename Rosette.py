import turtle
tracy=turtle.Pen()
tracy.speed(0)
n=int(turtle.numinput("How many circles would you want in a circle? ",6))
for i in range(n):
    tracy.circle(100)
    tracy.left(360/n)

   