def hint_username(username): #declaracion funcion y uso de elif
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15: # es lo mismo que else if
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")