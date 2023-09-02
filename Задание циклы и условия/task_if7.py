x1 = int(input("enter x1"))
y1 = int(input("enter y1"))
x2 = int(input("enter x2"))
y2 = int(input("enter y2"))

means_xy = [1, 2, 3, 4, 5, 6, 7, 8]

if x1 and y1 in means_xy:
    if x2 and y2 in means_xy:
        if x2 == x1+1 and y2 == y1 + 2 or x2 == x1+2 and y1+1 or x2 == x1 - 1 and y2 == y1 - 2 or y2 == y1 - 2 and x2 == x1 - 1:
            print("right move")

        else:
            print("wrong ")
else:
    print("wrong choice :), good luck!!!")



