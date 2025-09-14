#Defining all the variables for Newton's second law in static equilibrium.
mass = float(input("The mass is: "))
dis = float(input("The displacement is: "))
gravity = 9.80665

#mg=kx, rearranged to get spring constant value.
springcon = (mass * gravity) / dis
print(springcon)