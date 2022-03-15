while True:
    #Choice
    ch = input("         AREA OF FIGURES\nType 'squ' for finding the area of a Square\nType 'tri' for finding the Area of a triangle\nType 'rec' for finding the Area of a Rectangle\n")
    #Square
    if ch == "squ":
        Side = int(input("Enter the Side of your Square: "))
        Area = int(Side*Side)
        print(f'Area of the Square is {Area}')
    #Triangle
    elif ch == "tri":
        Base = int(input("Enter the Base of your Triangle: "))
        Height = int(input("Enter the Height of your Triangle: "))
        Area = int(0.5*Base*Height)
        print(f'The Area of your Triangle is {Area}')
    #Rectangle
    elif ch == "rec":
        Width = int(input("Enter the Width of your Rectangle: "))
        Breadth = int(input("Enter the Breadth of your Rectangle: "))
        Area = int(Width*Breadth)
        print(f'Area of the Rectangle is {Area}')
