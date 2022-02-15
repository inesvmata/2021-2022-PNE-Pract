import turtle

smart = turtle.Turtle()
# loop 4 times. everything I want to repeat is *indented* by 4 spaces
for i in range(4):
    smart.format(50) #smart does whatever the person that has created the turtle method has defined
    smart.right(90)
#This isn´t indented, so we aren´t repeating it
turtle.down()