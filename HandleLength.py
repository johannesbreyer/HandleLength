from math import *

from mojo.events import addObserver, removeObserver
from mojo.drawingTools import *

BEZIER_ARC_CIRCLE = 0.5522847498

def vector((x, y), angle, distance):
    """Calculate a new position `(x, y)` based on a given angle and distance."""
    _x = x + cos(radians(angle)) * distance
    _y = y + sin(radians(angle)) * distance
    return _x, _y

def get_vector((x1, y1), (x2, y2)):
    a = x2 - x1
    b = y2 - y1
    distance = sqrt(a ** 2 + b ** 2)
    if a != 0:
        angle_radians = atan(float(b) / a)
        angle_degrees = degrees(angle_radians)
    else:
        angle_degrees = 0
    return distance, angle_degrees

class handlesViewer(object):

    draw_box = True
    draw_handles = True
    draw_angles = True

    draw_in = True
    draw_out = True

    radius = 0.5

    font_size = 7
    font = "Lucida Grande Bold"

    stroke_width = 0.5
    color = 0, 0, 1
    
    def __init__(self):
        addObserver(self, 'draw', 'draw')
        addObserver(self, 'remove_observers', 'glyphWindowWillClose')

    def remove_observers(self, info):
        removeObserver(self, 'draw')
        removeObserver(self, 'glyphWindowWillClose')

    def draw(self, info):
        glyph = info["glyph"]
        if glyph is not None:
            save()
            fontSize(self.font_size)
            font(self.font)
            if self.draw_box:
                self._draw_box(glyph)
            if self.draw_handles:
                self._draw_handles(glyph)
            if self.draw_angles:
                self._draw_angles(glyph)
            restore()

    def _draw_handles(self, glyph):

        save()
        fill(*self.color)
        stroke(None)

        d = 0.65

        for c in glyph:
            for bPoint in c.bPoints:

                x0, y0 = bPoint.anchor
                w1, h1 = bPoint.bcpIn
                w2, h2 = bPoint.bcpOut
                x1, y1 = x0 + w1, y0 + h1
                x2, y2 = x0 + w2, y0 + h2

                if self.draw_in:
                    if w1 != 0 or h1 != 0:
                        d1 = sqrt(w1 ** 2 + h1 ** 2)
                        d1_caption = '%.2f' % d1
                        text(d1_caption, (x0 + w1 * 0.5, y0 + h1 * d))

                if self.draw_out:
                    if w2 != 0 or h2 != 0:
                        d2 = sqrt(w2 * w2 + h2 * h2)
                        d2_caption = '%.2f' % d2
                        text(d2_caption, (x0 + w2 * 0.5, y0 + h2 * d))

        restore()

    def _draw_box(self, glyph):

        save()
        strokeWidth(self.stroke_width)
        fill(None)
        dashLine(2, 2)

        for contour in glyph:
            for pt in contour.bPoints:
                x0, y0 = pt.anchor
                w1, h1 = pt.bcpIn
                w2, h2 = pt.bcpOut
                x1, y1 = x0 + w1, y0 + h1
                x2, y2 = x0 + w2, y0 + h2

                if self.draw_in and not int(w1) == 0 and not int(h1) == 0:
                    fill(None)
                    c = self.color + (0.5,)
                    stroke(*c)
                    rect(x0, y0, w1, h1)
                    line((x0, y0), (x1, y1))

                    if y1 > y0:
                        y1_ = y1 + 4
                    else:
                        y1_ = y1 - 14

                    if x1 > x0:
                        x1_ = x1 + 4
                    else:
                        x1_ = x1 - 20

                    stroke(None)
                    fill(*self.color)
                    text('%.2f' % w1, (x0 + w1 * 0.5, y1_))
                    text('%.2f' % h1, (x1_, y0 + h1 * 0.5))
                                
                if self.draw_out and not int(w2) == 0 and not int(h2) == 0:
                    fill(None)
                    c = self.color + (0.5,)
                    stroke(*c)
                    rect(x0, y0, w2, h2)
                    line((x0, y0), (x2, y2))

                    if y2 > y0:
                        y2_ = y2 + 4
                    else:
                        y2_ = y2 - 14

                    if x2 > x0:
                        x2_ = x2 + 4
                    else:
                        x2_ = x2 - 20

                    stroke(None)
                    fill(*self.color)
                    text('%.2f' % x2, (x0 + w2 * 0.5, y2_))
                    text('%.2f' % y2, (x2_, y0 + h2 * 0.5))

        restore()

    def _draw_angles(self, glyph):

        d = 0.25
        f = BEZIER_ARC_CIRCLE

        save()

        fill(None)
        strokeWidth(self.stroke_width)
        dashLine(2, 2)

        for contour in glyph:
            for pt in contour.bPoints:

                x0, y0 = pt.anchor
                w1, h1 = pt.bcpIn
                w2, h2 = pt.bcpOut
                x1, y1 = x0 + w1, y0 + h1
                x2, y2 = x0 + w2, y0 + h2

                if self.draw_in and not int(w1) == 0 and not int(h1) == 0:

                    distance, angle = get_vector((x0, y0), (x1, y1))
                    r = distance * d * self.radius

                    if w1 > 0 and h1 > 0:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x3, y3 = vector((x0, y0), angle - a1 * 0.5, distance * d)
                        x4, y4 = vector((x0, y0), angle + a2 * 0.5, distance * d)
                        p1_x, p1_y = x0 + r, y0
                        p2_x, p2_y = x0, y0 + r
                        p3_x, p3_y = p1_x, p1_y + r * f
                        p4_x, p4_y = p2_x + r * f, p2_y

                    elif w1 > 0 and h1 < 0:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x3, y3 = vector((x0, y0), angle - a1 * 0.5, distance * d)                            
                        x4, y4 = vector((x0, y0), angle + a2 * 0.5, distance * d)
                        p1_x, p1_y = x0 + r, y0
                        p2_x, p2_y = x0, y0 - r
                        p3_x, p3_y = p1_x, p1_y - r * f
                        p4_x, p4_y = p2_x + r * f, p2_y

                    elif w1 < 0 and h1 < 0:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x3, y3 = vector((x0, y0), 180 + angle - a1 * 0.5, distance * d)
                        x4, y4 = vector((x0, y0), 180 + angle + a2 * 0.5, distance * d)
                        p2_x, p2_y = x0 - r, y0
                        p1_x, p1_y = x0, y0 - r
                        p3_x, p3_y = p1_x - r * f, p1_y
                        p4_x, p4_y = p2_x, p2_y - r * f

                    else:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x3, y3 = vector((x0, y0), 180 + angle - a1 * 0.5, distance * d)
                        x4, y4 = vector((x0, y0), 180 + angle + a2 * 0.5, distance * d)
                        p1_x, p1_y = x0 - r, y0
                        p2_x, p2_y = x0, y0 + r
                        p3_x, p3_y = p1_x, p1_y + r * f
                        p4_x, p4_y = p2_x - r * f, p2_y

                    c = self.color + (0.5,)
                    stroke(*c)
                    fill(None)

                    newPath()
                    moveTo((p1_x, p1_y))
                    curveTo((p3_x, p3_y), (p4_x, p4_y), (p2_x, p2_y))
                    drawPath()

                    stroke(None)
                    fill(*self.color)
                    text('%.2f' % a1, (x3, y3))
                    text('%.2f' % a2, (x4, y4))
                    
                if self.draw_out and not int(w2) == 0 and not int(h2) == 0:

                    distance, angle = get_vector((x0, y0), (x2, y2))
                    r = distance * d * self.radius

                    if w2 > 0 and h2 > 0:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x5, y5 = vector((x0, y0), angle - a1 * 0.5, distance * d)
                        x6, y6 = vector((x0, y0), angle + a2 * 0.5, distance * d)
                        p1_x, p1_y = x0 + r, y0
                        p2_x, p2_y = x0, y0 + r
                        p3_x, p3_y = p1_x, p1_y + r * f
                        p4_x, p4_y = p2_x + r * f, p2_y

                    elif w2 > 0 and h2 < 0:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x5, y5 = vector((x0, y0), angle - a1 * 0.5, distance * d)
                        x6, y6 = vector((x0, y0), angle + a2 * 0.5, distance * d)
                        p1_x, p1_y = x0, y0 - r
                        p2_x, p2_y = x0 + r, y0
                        p3_x, p3_y = p1_x + r * f, p1_y
                        p4_x, p4_y = p2_x, p2_y - r * f

                    elif w2 < 0 and h2 < 0:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x5, y5 = vector((x0, y0), 180 + angle - a1 * 0.5, distance * d)
                        x6, y6 = vector((x0, y0), 180 + angle + a2 * 0.5, distance * d)
                        p1_x, p1_y = x0 - r, y0
                        p2_x, p2_y = x0, y0 - r
                        p3_x, p3_y = p1_x, p1_y - r * f
                        p4_x, p4_y = p2_x - r * f, p2_y

                    else:
                        a1 = angle % 90
                        a2 = 90 - a1
                        x5, y5 = vector((x0, y0), 180 + angle - a1 * 0.5, distance * d)
                        x6, y6 = vector((x0, y0), 180 + angle + a2 * 0.5, distance * d)
                        p1_x, p1_y = x0 - r, y0
                        p2_x, p2_y = x0, y0 + r
                        p3_x, p3_y = p1_x, p1_y + r * f
                        p4_x, p4_y = p2_x - r * f, p2_y

                    c = self.color + (0.5,)
                    stroke(*c)
                    fill(None)
                    newPath()
                    moveTo((p1_x, p1_y))
                    curveTo((p3_x, p3_y), (p4_x, p4_y), (p2_x, p2_y))
                    drawPath()

                    stroke(None)
                    fill(*self.color)
                    text('%.2f' % a1, (x5, y5))
                    text('%.2f' % a2, (x6, y6))

        restore()

if __name__ == '__main__':

    handlesViewer()
