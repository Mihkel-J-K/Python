import turtle
'''
degrees = 10800
i=0
turtle.speed(0)
while i != degrees:
    turtle.forward(2)
    turtle.left(1 + i/degrees)
    i+=1
'''

'''
turtle.circle(50,None,50)
'''
turtle.speed(0)
counter = 0
while counter != 16:
    degrees = 0
    while degrees != 360:
        if degrees == 45:
            ring1 = 0
            turtle.right(45)
            while ring1 != 360:
                if ring1 == 45:
                    ring2 = 0
                    while ring2 != 360:
                        turtle.width(2)
                        turtle.forward(1)
                        turtle.right(1)
                        ring2 += 1 
                turtle.forward(2)
                turtle.right(1)
                if ring1 == 135 or ring1 == 0 or ring1 == 315:
                    turtle.color("black")
                    turtle.width(3)
                elif ring1 == 225 or ring1 == 45 or ring1 == 360:
                    turtle.color("black")
                    turtle.width(1)
                ring1 += 1
            turtle.left(45)
        if degrees == 135 or degrees == 0 or degrees == 315:
            if degrees == 0 or degrees == 315:
                turtle.color('black')
            else:
                turtle.color("black")
            turtle.width(4)
        elif degrees == 45 or degrees == 360:
            turtle.color("black")
            turtle.width(1)
        turtle.forward(3)
        turtle.right(1)
        degrees += 1
    counter += 1
    turtle.right(22.5)
counter = 0
turtle.width(1)
while counter != 16:
    ring4 = 0
    while ring4 != 360:
        turtle.rorward(6)
        turtle.right(2)
        ring4 += 2
    counter += 1
        
    
    
