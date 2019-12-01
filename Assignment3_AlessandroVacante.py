# This Python program calculates different geometrical characteristics of a polygon
# The user can enter the number of polygon points and the their x and y coordinates 

import math

# A list that stores all entered coordinates. Its empty at start.
coord_x = []
coord_y = []

# Personalizing by Alessandro Vacante
print("Dear User, welcome to my Python program! This program calculates the geometrical characteristics of a polygon. Let's start!")
print("What's your name?")
name = input()
print('Hi ' + name +'! ' + 'Are you ready? Yes or No')
choose = input()
if choose == 'Yes':     
    print("Let's start!")

    # Input: number of polygon
    n = int(input("Enter the number of polygon points: "))
    print()

    # Personalizing by Alessandro Vacante
    if n == 3:
        print('Compliment ' + name + ', you have chosen a triangol!')
    elif n == 4:
        print('Compliment ' + name + ', you have chosen a polygon with 4 sides, probably a square or a rectangle!')
    else:
        print('Compliment ' + name + ', you have chosen a polygon with ' + n + ' sides!')

    # Coordinate points according to the number of polygon
    print()
    print("Enter x and y coordinates for polygon points ordered counterclockwise please: ")
    for i in range(n):
        x = float(input(f"Point {i+1} - x{i+1}: ")) 
        y = float(input(f"Point {i+1} - y{i+1}: "))
        coord_x.append(x)
        coord_y.append(y)

    # Print a table of entered data
    print()
    print(f"{'Point'} {'x':>10} {'y':>10}")
    print("-" * 40)
    for i in range(n):
        print(f"{i + 1} {coord_x[i]:17.2f} {coord_y[i]:10.2f}")

    # Calculate the geometrical characteristics (I've chosen a solution to train the loops)
    print()
    i = 0
    j = 1
    Ax = Sx = Sy = Ix = Iy = Ixy = 0
    while i <= n - 1:
        Ax = Ax + ( 1 / 2 ) * ( ( coord_x[j] + coord_x[i] ) * (coord_y[j] - coord_y[i] ) )
        Sx = Sx - ( 1 / 6 ) * ( ( coord_x[j] - coord_x[i] ) * ( coord_y[j]**2 + ( coord_y[i] * coord_y[j] ) + coord_y[i]**2 ) )
        Sy = Sy + ( 1 / 6 ) * ( ( coord_y[j] - coord_y[i] ) * ( coord_x[j]**2 + ( coord_x[i] * coord_x[j] ) + coord_x[i]**2 ) )
        Ix = Ix - ( 1 / 12 ) * ( ( coord_x[j] - coord_x[i] ) * ( coord_y[j]**3 + coord_y[j]**2*coord_y[i] + coord_y[j]*coord_y[i]**2 + coord_y[i]**3 ) )
        Iy = Iy + ( 1 / 12 ) * ( ( coord_y[j] - coord_y[i] ) * ( coord_x[j]**3 + coord_x[j]**2*coord_x[i] + coord_x[j]*coord_x[i]**2 + coord_x[i]**3 ) )
        Ixy = Ixy - ( 1 / 24 ) * ( ( coord_y[j] - coord_y[i] ) * ( coord_y[j] * ( 3*coord_x[j]**2 + 2*coord_x[j]*coord_x[i] + coord_x[i]**2 ) + coord_y[i] * ( 3*coord_x[i]**2 + 2*coord_x[j]*coord_x[i] + coord_x[j]**2)))
        if j == n - 1:
            i = i + 1
            j = 0
        else:
            j = j + 1
            i = i + 1
    xt = Sy / Ax
    yt = Sx / Ax
    Ixt = Ix - yt**2*Ax
    Iyt = Iy - xt**2*Ax
    Ixyt = Ixy + xt*yt*Ax

    # Printing results
    print("Geometric characteristics:")
    print(f"{'Ax:'} {Ax:10.2f}")
    print(f"{'Sx:'} {Sx:10.2f}")
    print(f"{'Sy:'} {Sy:10.2f}")
    print(f"{'Ix:'} {Ix:10.2f}")
    print(f"{'Iy:'} {Iy:10.2f}")
    print(f"{'Ixy:'} {Ixy:9.2f}")
    print(f"{'xt:'} {xt:10.2f}")
    print(f"{'yt:'} {yt:10.2f}")
    print(f"{'Ixt:'} {Ixt:9.2f}")
    print(f"{'Iyt:'} {Iyt:9.2f}")
    print(f"{'Ixyt:'} {Ixyt:8.2f}")
    print()
    print("End.")
    print('Goodbye ' + name + ', see you!')

else:
    print("Ok, see you next time!")