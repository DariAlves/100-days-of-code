def turn_around():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()
    
while not at_goal():
    jump() if wall_in_front() else move()       

# or 
# while not at_goal():
#     jump() if not front_is_clear() else move() 
        
        




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
