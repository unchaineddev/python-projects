# Reeborg's Hurdle1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Reeborg's Hurdle2 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# Reeborg's Hurdle3
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def side():
    move()
    turn_left()
    move()

def cycle():
    side()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#using for loop
for step in range(6):
    cycle()

# using while loop 
#while at_goal() != True:
#   cycle()


#Hurdle3
#while at_goal() != True:
#    if wall_in_front() == True:
#       cycle()
#    else:
#       move()





#def turn_right():
#       turn_left()
#       turn_left()
#       turn_left()
#                 
#def jump():
#       turn_left()
#           while wall_on_right():
#               move()
#       turn_right()
#       move()
#       turn_right()

#while front_is_clear():
#       move()
#       turn_left()
#                                                  
# while not at_goal():
#    if wall_in_front():
#   jump()
#else:
#   move()
#                                                                                        
