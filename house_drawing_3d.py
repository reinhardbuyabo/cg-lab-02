import cairo
import math

WIDTH, HEIGHT = 1600, 1000
BG_COLOR = (0.8, 0.8, 0.8)

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgb(*BG_COLOR)
ctx.paint()

# Roof outline
ctx.set_line_width(5)
ctx.set_source_rgb(0, 0, 0)
ctx.move_to(410, 100)
ctx.line_to(1200, 50)
ctx.line_to(1370, 340)
ctx.line_to(580, 400)
ctx.close_path()
ctx.stroke()

ctx.set_line_width(8)
ctx.set_source_rgb(0, 0, 0)
ctx.move_to(220, 280) # x6, y6
ctx.line_to(400, 100) # x1, y1
ctx.line_to(1200, 50)
ctx.line_to(1370, 340)
ctx.line_to(1360, 360) #
ctx.line_to(560, 420) #
ctx.line_to(400, 130) # x1, y1 + 30
ctx.line_to(230, 300) # x5, y5
ctx.close_path()
ctx.stroke()

ctx.set_source_rgb(0, 0, 0)
ctx.move_to(230, 300)
ctx.line_to(250, 300)
ctx.line_to(250, 280)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.close_path()
ctx.stroke()

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
ctx.close_path()
ctx.stroke()

# Write to png
surface.write_to_png('house.png')
print('3D House with Details Created!')