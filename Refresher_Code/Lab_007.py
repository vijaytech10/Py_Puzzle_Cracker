"""
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
"""

side_A = float(input("Enter length of side A :"))
side_B = float(input("Enter length of side B :"))
side_C = float(input("Enter length of side C :"))

if side_A == side_B == side_C:
    print ("its a equilateral Triangle")
elif (side_A == side_B) or (side_B == side_C) or (side_A == side_C):
    print ("its a isosceles Triangle")
elif (side_A != side_B) or (side_B != side_C) or (side_A != side_C):
    print ("its a scalene Triangle")
