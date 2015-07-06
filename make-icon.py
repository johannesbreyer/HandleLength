# make extension icon

size(20, 20)

# margin
m = 0.18

# radius
r = 0.12 * width()

# stroke width : handle
sw = 0.7 * r

# stroke width : box
sw2 = 0.35 * r

# calculate box points
p0_x, p0_y = width() * m, height() * m
p1_x, p1_y = width() * m, height() * (1.0 - m)
p2_x, p2_y = width() * (1.0 - m), height() * m
p3_x, p3_y = width() * (1.0 - m), height() * (1.0 - m)

# calculate box
w = width() * (1.0 - m * 2)
h = height() * (1.0 - m * 2)

# draw handle
stroke(0)
lineCap('butt')
fill(None)
strokeWidth(sw * 0.7)
lineDash(None)
line((p0_x, p0_y), (p3_x, p3_y))

# draw box

stroke(0)
strokeWidth(sw)
fill(None)
strokeWidth(sw2)
lineDash(sw2 * 1.15, sw2 *1.45)
rect(p0_x, p0_y, w, h)

# draw on-curve point

fill(1)
strokeWidth(sw * 1)
lineDash(None)
rect(p0_x - r, p0_y - r, r * 2, r * 2)

# draw control point

r2 = r * 0.7

fill(0)
oval(p3_x - r2, p3_y - r2, r2 * 2, r2 * 2)

# save image

saveImage(['measure-handles-tool-icon.pdf'])
