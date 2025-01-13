"""
File: cube.py

This program calculates and prints the surface area of a cube.
"""

# Prompt the user to enter the length of a cube's edge (integer value)
edge_length = int(input("Enter the length of an edge of the cube (in units): "))

# Calculate the surface area of the cube
# Surface area formula: 6 * edge_length^2
surface_area = 6 * (edge_length ** 2)

# Display the calculated surface area with a descriptive label
print(f"The surface area of the cube is: {surface_area} square units.")
