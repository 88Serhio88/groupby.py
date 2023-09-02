side_triangle_1 = int(input("enter the first side of triangle"))
side_triangle_2 = int(input("enter the second side of triangle"))
side_triangle_3 = int(input("enter the third side of triangle"))
if side_triangle_1 > side_triangle_2+side_triangle_3 or side_triangle_2 > side_triangle_1+side_triangle_3 or side_triangle_3 > side_triangle_2+side_triangle_1:
    print("there is no such triangle")
else:
    print("the triangle exists")