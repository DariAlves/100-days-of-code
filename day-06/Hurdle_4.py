def turn_around():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()   
    turn_around()
    move()
    turn_around()
    move()
    while wall_on_right() and not wall_in_front():
        move()
    turn_left()
while not at_goal():
    jump() if not front_is_clear() else move()
    
        
        




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
