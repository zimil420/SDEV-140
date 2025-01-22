# Program to mix two primary colors and determine the resulting secondary color

def mix_colors(color1, color2):
    """
    This function takes two primary colors as input and returns the secondary color
    or an error message if invalid inputs are provided.
    """
    # Define a dictionary mapping color pairs to their resulting color
    color_combinations = {
        ("red", "blue"): "purple",
        ("blue", "red"): "purple",
        ("red", "yellow"): "orange",
        ("yellow", "red"): "orange",
        ("blue", "yellow"): "green",
        ("yellow", "blue"): "green",
    }

    # Check if the input colors are in the dictionary and return the result
    return color_combinations.get((color1, color2), "Error: Invalid color combination.")

# Prompt the user for two colors
print("Enter the names of two primary colors (red, blue, yellow) to mix:")
color1 = input("Enter the first color: ").strip().lower()  # Remove leading/trailing spaces and convert to lowercase
color2 = input("Enter the second color: ").strip().lower()

# Validate the inputs
primary_colors = {"red", "blue", "yellow"}  # Set of valid primary colors

if color1 in primary_colors and color2 in primary_colors:
    # If both inputs are valid, mix the colors
    result = mix_colors(color1, color2)
    print(f"The resulting color is: {result}")
else:
    # If any input is invalid, display an error message
    print("Error: Please enter valid primary colors (red, blue, yellow).")
