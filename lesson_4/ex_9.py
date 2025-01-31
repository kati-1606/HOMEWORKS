# LINE SEGMENT
#  9_You are given four real numbers-the coordinates of  two points on a plane.
#  The first two numbers are the x and y coordinates of the first point,
#  and the last two numbers are the x and y coordinates of the second point.
#  Output the length of the line segment bounded by the two points.

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
line_length = ((x2-x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5
print(line_length)