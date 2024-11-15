import cairo
import math

# Define colors
house_color = (0.98, 0.85, 0.71)  # Beige color for the house front
house_side_color = (0.93, 0.80, 0.66)  # Darker beige for the house side
roof_color = (0.93, 0.39, 0.13)  # Orange color for the roof
window_color = (0.63, 0.88, 0.81)  # Teal color for the windows
door_color = (0.55, 0.27, 0.07)  # Dark brown color for the door
frame_color = (0, 0, 0)  # Black color for the frames


def draw_house_frame(ctx):
    # House side (darker beige)
    ctx.set_source_rgb(*house_side_color)
    ctx.move_to(220, 280)
    ctx.line_to(400, 100)
    ctx.line_to(400, 130)
    ctx.line_to(230, 300)
    ctx.close_path()
    ctx.fill()

    # Roof outline and fill
    ctx.set_line_width(5)
    ctx.move_to(410, 100)
    ctx.line_to(1200, 50)
    ctx.line_to(1370, 340)
    ctx.line_to(580, 400)
    ctx.close_path()
    ctx.set_source_rgb(*roof_color)
    ctx.fill_preserve()
    ctx.set_source_rgb(*frame_color)
    ctx.stroke()

    # House frame
    ctx.set_line_width(8)
    ctx.set_source_rgb(*frame_color)
    ctx.move_to(220, 280)
    ctx.line_to(400, 100)
    ctx.line_to(1200, 50)
    ctx.line_to(1370, 340)
    ctx.line_to(1360, 360)
    ctx.line_to(560, 420)
    ctx.line_to(400, 130)
    ctx.line_to(230, 300)
    ctx.close_path()
    ctx.stroke()

    # Fill house front with beige color
    ctx.set_source_rgb(*house_color)
    ctx.move_to(250, 300)
    ctx.line_to(250, 700)
    ctx.line_to(550, 820)
    ctx.line_to(1330, 720)
    ctx.line_to(1330, 360)
    ctx.line_to(560, 420)
    ctx.close_path()
    ctx.fill()


def draw_small_roof_detail(ctx):
    ctx.set_source_rgb(*frame_color)
    ctx.move_to(230, 300)
    ctx.line_to(250, 300)
    ctx.line_to(250, 280)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.close_path()
    ctx.stroke()


def draw_main_walls(ctx):
    ctx.set_line_width(8)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.set_source_rgb(*frame_color)
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


def draw_dormer(ctx):
    # Dormer roof
    ctx.move_to(600, 250)
    ctx.line_to(675, 175)
    ctx.line_to(725, 195)
    ctx.line_to(800, 250)
    ctx.close_path()
    ctx.set_source_rgb(*roof_color)
    ctx.fill_preserve()
    ctx.set_source_rgb(*frame_color)
    ctx.set_line_width(3)
    ctx.stroke()

    # Dormer walls
    ctx.move_to(600, 250)
    ctx.line_to(600, 300)
    ctx.line_to(800, 300)
    ctx.line_to(800, 250)
    ctx.close_path()
    ctx.set_source_rgb(*house_color)
    ctx.fill_preserve()
    ctx.set_source_rgb(*frame_color)
    ctx.stroke()

    # Dormer window frame
    window_x = 650
    window_y = 260
    window_width = 100
    window_height = 35

    ctx.rectangle(window_x, window_y, window_width, window_height)
    ctx.set_source_rgb(*window_color)
    ctx.fill_preserve()
    ctx.set_source_rgb(*frame_color)
    ctx.stroke()

    # Dormer window panes
    ctx.move_to(window_x + window_width / 2, window_y)
    ctx.line_to(window_x + window_width / 2, window_y + window_height)
    ctx.stroke()

    ctx.move_to(window_x, window_y + window_height / 2)
    ctx.line_to(window_x + window_width, window_y + window_height / 2)
    ctx.stroke()


def draw_window(ctx, x, y, width, height):
    ctx.save()

    # Apply perspective transformation
    ctx.translate(x, y)
    ctx.scale(1, 0.8)

    # Window frame
    ctx.set_line_width(3)
    ctx.rectangle(0, 0, width, height)
    ctx.set_source_rgb(*window_color)
    ctx.fill_preserve()
    ctx.set_source_rgb(*frame_color)
    ctx.stroke()

    # Window panes
    ctx.move_to(width / 2, 0)
    ctx.line_to(width / 2, height)
    ctx.stroke()

    # Horizontal divider
    ctx.move_to(0, height / 2)
    ctx.line_to(width, height / 2)
    ctx.stroke()

    ctx.restore()


def draw_door(ctx, x, y, width, height):
    ctx.save()

    ctx.translate(x, y)
    ctx.scale(1, 0.8)

    # Door frame
    ctx.rectangle(0, 0, width, height)
    ctx.set_source_rgb(*door_color)
    ctx.fill_preserve()
    ctx.set_source_rgb(*frame_color)
    ctx.stroke()

    # Door handle
    ctx.arc(width * 0.8, height * 0.5, 5, 0, 2 * math.pi)
    ctx.set_source_rgb(0.3, 0.3, 0.3)
    ctx.fill()

    ctx.restore()


def main():
    WIDTH, HEIGHT = 1600, 1000
    BG_COLOR = (0.8, 0.8, 0.8)

    # Set up surface
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(*BG_COLOR)
    ctx.paint()

    # Draw house components
    draw_house_frame(ctx)
    draw_small_roof_detail(ctx)
    draw_main_walls(ctx)
    draw_dormer(ctx)

    # Add windows
    draw_window(ctx, 300, 450, 100, 150)  # Left window
    draw_window(ctx, 700, 450, 80, 120)  # Center window 1
    draw_window(ctx, 900, 450, 80, 120)  # Center window 2

    # Add door
    draw_door(ctx, 1100, 500, 70, 140)

    # Write to png
    surface.write_to_png('house_3.png')
    print('3D House with Updated Colors Created!')


if __name__ == "__main__":
    main()