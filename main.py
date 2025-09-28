import math


# Screen size in pixels, for change picture resolution
width = 305
height = 543

screen = width * height
print(f"Screen size is {width} X {height} pixels\n")
square_5 = int(screen * 0.05)
square_2 = int(screen * 0.02)
a_side = int(math.sqrt(square_5))
overlight_side = int(math.sqrt(square_2))
print(f"5% square is {square_5} squared pixels")
print(f"a side of square is {a_side} pixels")
print()
print(f"2% square is {square_2} squared pixels")
print(f"a side of overlight square is {overlight_side} pixels")
print()

variable_artifact_width = int(input("Enter artifact width: "))
variable_artifact_height = int(input("Enter artefact height: "))



def calculate_artifact_area(width, height, screen):
  artifact_area_percentage = (width * height) *100 / screen
  return artifact_area_percentage

def show_artifact_area_percentage(artifact_area_percentage):
  artifact_area_percentage = int(artifact_area_percentage)
  print(f"\nThe artifact area percentage is: {artifact_area_percentage}%")


show_artifact_area_percentage(calculate_artifact_area(variable_artifact_width, variable_artifact_height, screen))
