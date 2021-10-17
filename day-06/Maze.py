while not wall_in_front():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    
    
        


        
        
        
        




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
