size(20, 20)

m = 0.19
r = 0.12 * width()

sw = 0.6 * r
sw2 = 0.28 * r

p0_x, p0_y = width() * m, height() * m
p1_x, p1_y = width() * m, height() * (1.0 - m)
p2_x, p2_y = width() * (1.0 - m), height() * m
p3_x, p3_y = width() * (1.0 - m), height() * (1.0 - m)

w = width() * (1.0 - m * 2)
h = height() * (1.0 - m * 2)

stroke(0)
lineCap('butt')
fill(None)
strokeWidth(sw)
lineDash(None)
line((p0_x, p0_y), (p3_x, p3_y))

o = width() * m * 2.5

strokeWidth(sw2)

stroke(0)
strokeWidth(sw)

r2 = r * 0.5

fill(None)
strokeWidth(sw2)
rect(p0_x, p0_y, w, h)

fill(1)
strokeWidth(sw)
lineDash(None)
rect(p0_x - r, p0_y - r, r * 2, r * 2)
rect(p3_x - r2, p3_y - r2, r2 * 2, r2 * 2)

saveImage(['measure-handles-tool-icon.pdf'])
