# Importing pi for circle calculations
from math import pi# Importing pi for circle calculations
# Loop to keep the program running until the user decides to exit
while True:  
    print("\nChoose any  three options")
    print("1. Area and circumference of a circle")
    print("2. Area and perimeter of a triangle")
    print("3. Area and perimeter of a rectangle")
    print("4. Exit")  # exit option incase the user needs to exit
    
    choice = int(input("Choose among the choices: "))
    
    if choice == 1:
        # Calculate area and circumference of a circle
        radius = float(input("Enter radius of the circle: "))
        area = pi * radius * radius
        circumference = 2 * pi * radius
        print("Area of the circle:", area)
        print("Circumference of the circle:", circumference)
    
    elif choice == 2:
        # Calculate area and perimeter of a triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        hypotenuse = float(input("Enter the hypotenuse of the triangle: "))
        area = 0.5 * base * height
        perimeter = base + height + hypotenuse
        print("Area of the triangle:", area)
        print("Perimeter of the triangle:", perimeter)
    
    elif choice == 3:
        # Calculate area and perimeter of a rectangle
        width = float(input("Enter the width of the rectangle: "))
        length = float(input("Enter the length of the rectangle: "))
        area = width * length
        perimeter = 2 * (width + length)
        print("Area of the rectangle:", area)
        print("Perimeter of the rectangle:", perimeter)
    
    elif choice == 4:
        # Exit the program
        print("Exiting program.....!")
        break
    #print invalid of the user does not put the need value
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
