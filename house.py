import cairo
import math

WIDTH, HEIGHT = 1600, 1000
BG_COLOR = (0.8, 0.8, 0.8)
frame_color = (0, 0, 0)  # Black color for the outlines

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgb(*BG_COLOR)
ctx.paint()

# Roof outline
ctx.set_line_width(5)
ctx.set_source_rgb(*frame_color)
ctx.move_to(410, 100)
ctx.line_to(1200, 50)
ctx.line_to(1370, 340)
ctx.line_to(580, 400)
ctx.close_path()
ctx.stroke()

# House outline
ctx.set_line_width(8)
ctx.move_to(220, 280)  # x6, y6
ctx.line_to(400, 100)  # x1, y1
ctx.line_to(1200, 50)
ctx.line_to(1370, 340)
ctx.line_to(1360, 360)
ctx.line_to(560, 420)
ctx.line_to(400, 130)  # x1, y1 + 30
ctx.line_to(230, 300)  # x5, y5
ctx.close_path()
ctx.stroke()

ctx.move_to(230, 300)
ctx.line_to(250, 300)
ctx.line_to(250, 280)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.close_path()
ctx.stroke()

# House lower part outline
ctx.set_line_width(8)
ctx.set_line_join(cairo.LINE_JOIN_MITER)
ctx.move_to(250, 300)
ctx.line_to(250, 700)
ctx.line_to(550, 820)
ctx.line_to(1330, 720)
ctx.line_to(1330, 360)
ctx.stroke()

ctx.set_line_width(5)
ctx.move_to(550, 820)
ctx.line_to(550, 400)
ctx.stroke()

# Door outline
ctx.set_line_width(5)
door_height = 140
door_width = 80
door_bottom_x = 1150
right_wall_dx = 1330 - 550
right_wall_dy = 720 - 820
right_wall_slope = right_wall_dy / right_wall_dx
door_bottom_y = 820 + (door_bottom_x - 550) * right_wall_slope

ctx.move_to(door_bottom_x, door_bottom_y)
ctx.line_to(door_bottom_x, door_bottom_y - door_height)
ctx.line_to(door_bottom_x + door_width, door_bottom_y + door_width * right_wall_slope - door_height)
ctx.line_to(door_bottom_x + door_width, door_bottom_y + door_width * right_wall_slope)
ctx.close_path()
ctx.stroke()

# Doorknob
ctx.set_line_width(3)
knob_x = door_bottom_x + door_width * 0.8
knob_y = door_bottom_y + (door_width * 0.8 * right_wall_slope) - door_height * 0.4
ctx.arc(knob_x, knob_y, 4, 0, 2*math.pi)
ctx.stroke()

# Windows outlines
ctx.set_line_width(5)
window1_bottom_x = 650
window1_width = 120
window1_height = 100
window1_bottom_y = 820 + (window1_bottom_x - 550) * right_wall_slope - 150
ctx.move_to(window1_bottom_x, window1_bottom_y)
ctx.line_to(window1_bottom_x, window1_bottom_y - window1_height)
ctx.line_to(window1_bottom_x + window1_width, window1_bottom_y + window1_width * right_wall_slope - window1_height)
ctx.line_to(window1_bottom_x + window1_width, window1_bottom_y + window1_width * right_wall_slope)
ctx.close_path()
ctx.stroke()

window2_bottom_x = 850
window2_bottom_y = 820 + (window2_bottom_x - 550) * right_wall_slope - 150
ctx.move_to(window2_bottom_x, window2_bottom_y)
ctx.line_to(window2_bottom_x, window2_bottom_y - window1_height)
ctx.line_to(window2_bottom_x + window1_width, window2_bottom_y + window1_width * right_wall_slope - window1_height)
ctx.line_to(window2_bottom_x + window1_width, window2_bottom_y + window1_width * right_wall_slope)
ctx.close_path()
ctx.stroke()

window3_bottom_x = 350
left_wall_dx = 550 - 250
left_wall_dy = 820 - 700
left_wall_slope = left_wall_dy / left_wall_dx
window3_size = 85
window3_bottom_y = 700 + (window3_bottom_x - 250) * left_wall_slope - 150
ctx.move_to(window3_bottom_x, window3_bottom_y)
ctx.line_to(window3_bottom_x, window3_bottom_y - window3_size)
ctx.line_to(window3_bottom_x + window3_size, window3_bottom_y + window3_size * left_wall_slope - window3_size)
ctx.line_to(window3_bottom_x + window3_size, window3_bottom_y + window3_size * left_wall_slope)
ctx.close_path()
ctx.stroke()

# Add window panes
ctx.set_line_width(2)
mid_x = window3_bottom_x + window3_size/2
mid_y = window3_bottom_y + (window3_size/2) * left_wall_slope
ctx.move_to(mid_x, mid_y)
ctx.line_to(mid_x, mid_y - window3_size)
ctx.stroke()

ctx.move_to(window3_bottom_x, window3_bottom_y - window3_size/2)
ctx.line_to(window3_bottom_x + window3_size, window3_bottom_y + window3_size * left_wall_slope - window3_size/2)
ctx.stroke()

# Save to PNG
surface.write_to_png("house.png")
