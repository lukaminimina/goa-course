from turtle import*
shape("circle")


width(4)
      


# we start drawning a square


begin_fill()
color("green")
      
speed(1)

 # we start drawning a house

forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()
#we finished drawing a square

# we start drawing a door

left(90)
forward(60)
color("brown")
begin_fill()
left(90)  
forward(70)
right(90)
forward(30)
right(90)
forward(70)
end_fill()
#we finishd drawing a door

#we start drawing a roof

penup()
goto(150 ,150)
pendown()
begin_fill()
color("red")

left(210)


forward(150)
left(120)
forward(150)
end_fill()

#we start drawing a windows

penup()
goto(130 ,130)
pendown()


color("blue")

left(30)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

right(90)
forward(20)

left(90)
forward(40)

penup()
goto(20 ,90)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)







exitonclick()
    


