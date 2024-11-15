import cairo

# Set up the image surface and context
width, height = 500, 500
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Define colors
house_color = (0.98, 0.85, 0.71)  # Beige color for the house
roof_color = (0.93, 0.39, 0.13)   # Orange color for the roof
window_color = (0.63, 0.88, 0.81) # Teal color for the windows
door_color = (0.55, 0.27, 0.07)   # Dark brown color for the door
frame_color = (0, 0, 0)           # Black color for the frames

# Draw house base (rectangle)
context.set_source_rgb(*house_color)
context.rectangle(150, 250, 200, 150)
context.fill_preserve()
context.set_source_rgb(*frame_color)
context.set_line_width(2)
context.stroke()

# Draw roof (triangle)
context.move_to(125, 250)
context.line_to(375, 250)
context.line_to(250, 150)
context.close_path()
context.set_source_rgb(*roof_color)
context.fill_preserve()
context.set_source_rgb(*frame_color)
context.stroke()

# Draw windows
def draw_window(x, y, width, height):
    context.set_source_rgb(*window_color)
    context.rectangle(x, y, width, height)
    context.fill_preserve()
    context.set_source_rgb(*frame_color)
    context.set_line_width(2)
    context.stroke()

# Front windows
draw_window(180, 270, 40, 50)
draw_window(280, 270, 40, 50)

# Side window
draw_window(100, 270, 40, 50)

# Draw door
context.set_source_rgb(*door_color)
context.rectangle(240, 320, 30, 80)
context.fill_preserve()
context.set_source_rgb(*frame_color)
context.set_line_width(2)
context.stroke()

# Draw dormer window on the roof
context.set_source_rgb(*roof_color)
context.rectangle(210, 200, 80, 40)
context.fill_preserve()
context.set_source_rgb(*frame_color)
context.stroke()
draw_window(220, 210, 60, 30)

# Save the drawing
surface.write_to_png("3d_house.png")