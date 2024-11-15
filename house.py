import cairo
import math

WIDTH, HEIGHT = 1600, 1000
BG_COLOR = (0.8, 0.8, 0.8)

# Define colors
house_color = (0.98, 0.85, 0.71)  # Beige color for the house
frame_color = (0, 0, 0)           # Black color for the frames

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgb(*BG_COLOR)
ctx.paint()

# Draw the house walls
ctx.set_line_width(8)
ctx.set_line_join(cairo.LINE_JOIN_MITER)

# Fill the lower part of the house (walls)
ctx.set_source_rgb(*house_color)
ctx.move_to(250, 300)
ctx.line_to(250, 700)
ctx.line_to(550, 820)
ctx.line_to(1330, 720)
ctx.line_to(1330, 360)
ctx.close_path()
ctx.fill_preserve()

# Draw outlines for the walls
ctx.set_source_rgb(*frame_color)
ctx.stroke()

# Save to PNG
surface.write_to_png("house.png")
