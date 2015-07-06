# make extension icon

# settings

size(20, 20)

margin = 0.18
oncurve_point_size = 4.8
offcurve_point_size = 3.36
handle_stroke = 1.17
points_stroke = 1.68
box_stroke = 0.94

save_img = True

# box points

p0_x, p0_y = width() * margin, height() * margin
p1_x, p1_y = width() * margin, height() * (1.0 - margin)
p2_x, p2_y = width() * (1.0 - margin), height() * margin
p3_x, p3_y = width() * (1.0 - margin), height() * (1.0 - margin)

# box dimensions

w = width() * (1.0 - margin * 2)
h = height() * (1.0 - margin * 2)

# draw handle

stroke(0)
strokeWidth(handle_stroke)
lineDash(None)
line((p0_x, p0_y), (p3_x, p3_y))

# draw box

box_stroke_radius = box_stroke * 0.5
box_stroke_steps = 9

stroke(None)
fill(0)

for j in range(box_stroke_steps):
    rs_y = p0_y + (j * h / (box_stroke_steps-1))

    for i in range(box_stroke_steps):
        rs_x = p0_x + (i * w / (box_stroke_steps-1))

        if j == 0 or j == box_stroke_steps - 1:
            rect(rs_x - box_stroke_radius, rs_y - box_stroke_radius, box_stroke, box_stroke)

        else:
            if i == 0 or i == box_stroke_steps - 1:
                rect(rs_x - box_stroke_radius, rs_y - box_stroke_radius, box_stroke, box_stroke)                

# draw on-curve point

fill(1)
stroke(0)
strokeWidth(points_stroke)
lineDash(None)
oncurve_point_radius = oncurve_point_size * 0.5

rect(p0_x - oncurve_point_radius, p0_y - oncurve_point_radius, oncurve_point_size, oncurve_point_size)

# draw control point

fill(0)
offcurve_point_radius = offcurve_point_size * 0.5
oval(p3_x - offcurve_point_radius, p3_y - offcurve_point_radius, offcurve_point_size, offcurve_point_size)

# save image

if save_img:
    saveImage(['measure-handles-tool-icon.pdf'])
