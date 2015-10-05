# [h] Measure Handles Object

from math import *
from mojo.drawingTools import *

#-----------
# constants
#-----------

#: Handle length in relation to circle radius, for creating circles with Bezier curves.
BEZIER_ARC_CIRCLE = 0.5522847498

#-----------
# functions
#-----------

def vector((x, y), angle, distance):
    """
    Calculate a new position based on a given angle and distance.

    """
    _x = x + cos(radians(angle)) * distance
    _y = y + sin(radians(angle)) * distance
    return _x, _y

def get_vector((x1, y1), (x2, y2)):
    """
    Get the distance and angle between two points.

    """
    a = x2 - x1
    b = y2 - y1
    distance = sqrt(a ** 2 + b ** 2)
    if a != 0:
        angle_radians = atan(float(b) / a)
        angle_degrees = degrees(angle_radians)
    else:
        angle_degrees = 0
    return distance, angle_degrees

#---------
# objects
#---------

class MeasureHandles(object):

    draw_box = True
    draw_handles = True
    draw_angles = True

    draw_in = True
    draw_out = True

    radius = 0.3

    font_size = 9
    font = "Lucida Grande Bold"

    stroke_width = 1

    color_angle = 0, 1, 1
    color_box = 1, 0, 0
    color_handle = 0, 0, 1

    stroke_alpha = 0.65
    stroke_dash = 2

    def __init__(self, glyph):
        self.glyph = glyph

    def _get_positions(self, bPoint):
        # box origin point
        x0, y0 = bPoint.anchor
        # incoming bcp
        w1, h1 = bPoint.bcpIn
        x1, y1 = x0 + w1, y0 + h1
        # outgoing bcp
        w2, h2 = bPoint.bcpOut
        x2, y2 = x0 + w2, y0 + h2
        # done
        return x0, y0, w1, h1, w2, h2, x1, y1, x2, y2

    def draw(self, scale=1.0):

        if self.glyph is not None:

            # setup drawing
            save()
            fontSize(self.font_size * scale)
            font(self.font)

            # draw!
            for contour in self.glyph:
                for bPoint in contour.bPoints:

                    # draw box info
                    if self.draw_box:
                        self._draw_box(bPoint, scale)

                    # draw handles info
                    if self.draw_handles:
                        self._draw_handles(bPoint, scale)

                    # draw angles info
                    if self.draw_angles:
                        self._draw_angles(bPoint, scale)

            # done with glyph
            restore()

    def _draw_handles(self, bPoint, scale):

        # get positions
        x0, y0, w1, h1, w2, h2, x1, y1, x2, y2 = self._get_positions(bPoint)

        # setup drawing
        save()
        strokeWidth(self.stroke_width * scale)
        sw = self.stroke_width * scale * self.stroke_dash
        dashLine(sw, sw)

        # draw incoming bcp
        if self.draw_in:
            if w1 != 0 or h1 != 0:

                # draw line
                fill(None)
                c = self.color_handle + (self.stroke_alpha,)
                stroke(*c)
                line((x0, y0), (x1, y1))

                # draw caption
                d1 = sqrt(w1 ** 2 + h1 ** 2)
                d1_caption = '%.2f' % d1
                d1_w, d1_h = textSize(d1_caption)
                d1_x = x0 + (w1 * 0.5) - (d1_w * 0.5)
                d1_y = y0 + (h1 * 0.5) - (d1_h * 0.4)

                fill(*self.color_handle)
                stroke(None)
                textBox(d1_caption, (d1_x, d1_y, d1_w, d1_h), align='center')

        # draw outgoing bcp
        if self.draw_out:
            if w2 != 0 or h2 != 0:

                # draw line
                fill(None)
                c = self.color_handle + (self.stroke_alpha,)
                stroke(*c)
                line((x0, y0), (x2, y2))

                # draw caption
                d2 = sqrt(w2 * w2 + h2 * h2)
                d2_caption = '%.2f' % d2
                d2_w, d2_h = textSize(d2_caption)
                d2_x = x0 + (w2 * 0.5) - (d2_w * 0.5)
                d2_y = y0 + (h2 * 0.5) - (d2_h * 0.4)

                fill(*self.color_handle)
                stroke(None)
                textBox(d2_caption, (d2_x, d2_y, d2_w, d2_h), align='center')

        # done
        restore()

    def _draw_box(self, bPoint, scale):

        # get positions
        x0, y0, w1, h1, w2, h2, x1, y1, x2, y2 = self._get_positions(bPoint)

        # setup drawing
        save()
        strokeWidth(self.stroke_width * scale)
        sw = self.stroke_width * scale * self.stroke_dash
        dashLine(sw, sw)

        # draw box for incoming bcp
        if self.draw_in and not int(w1) == 0 and not int(h1) == 0:

            # draw box
            fill(None)
            c = self.color_box + (self.stroke_alpha,)
            stroke(*c)
            rect(x0, y0, w1, h1)

            # draw captions
            stroke(None)
            fill(*self.color_box)

            # draw x caption
            x1_caption = '%.2f' % abs(w1)
            x1_w, x1_h = textSize(x1_caption)
            x1_x = x0 + (w1 * 0.5) - (x1_w * 0.5)
            x1_y = y1 - x1_h * 0.4
            textBox(x1_caption, (x1_x, x1_y, x1_w, x1_h), align='center')

            # draw y caption
            y1_caption = '%.2f' % abs(h1)
            y1_w, y1_h = textSize(y1_caption)
            y1_x = x1 - (y1_w * 0.5)
            y1_y = y0 + (h1 * 0.5) - (y1_h * 0.4)
            textBox(y1_caption, (y1_x, y1_y, y1_w, y1_h), align='center')

        # draw box for outcoming bcp
        if self.draw_out and not int(w2) == 0 and not int(h2) == 0:

            # draw box
            fill(None)
            c = self.color_box + (self.stroke_alpha,)
            stroke(*c)
            rect(x0, y0, w2, h2)

            # draw captions
            stroke(None)
            fill(*self.color_box)

            # draw x caption
            x2_caption = '%.2f' % abs(w2)
            x2_w, x2_h = textSize(x2_caption)
            x2_x = x0 + (w2 * 0.5) - (x2_w * 0.5)
            x2_y = y2 - x2_h * 0.4
            textBox(x2_caption, (x2_x, x2_y, x2_w, x2_h), align='center')

            # draw y caption
            y2_caption = '%.2f' % abs(h2)
            y2_w, y2_h = textSize(y2_caption)
            y2_x = x2 - (y2_w * 0.5)
            y2_y = y0 + (h2 * 0.5) - (y2_h * 0.4)
            textBox(y2_caption, (y2_x, y2_y, y2_w, y2_h), align='center')

        # done
        restore()

    def _draw_angles(self, bPoint, scale):

        f = BEZIER_ARC_CIRCLE

        # get positions
        x0, y0, w1, h1, w2, h2, x1, y1, x2, y2 = self._get_positions(bPoint)

        # setup drawing
        save()
        strokeWidth(self.stroke_width * scale)
        sw = self.stroke_width * scale * self.stroke_dash
        dashLine(sw, sw)

        # draw angles for incoming BCP
        if self.draw_in and not int(w1) == 0 and not int(h1) == 0:

            handle_length, angle = get_vector((x0, y0), (x1, y1))
            r = handle_length * self.radius

            a1 = angle % 90
            a2 = 90 - a1

            if w1 > 0 and h1 > 0:

                x3, y3 = vector((x0, y0), angle - a1 * 0.5, r)
                x4, y4 = vector((x0, y0), angle + a2 * 0.5, r)

                p1_x, p1_y = x0 + r, y0
                p2_x, p2_y = x0, y0 + r
                p3_x, p3_y = p1_x, p1_y + r * f
                p4_x, p4_y = p2_x + r * f, p2_y

            elif w1 > 0 and h1 < 0:

                x3, y3 = vector((x0, y0), angle - a1 * 0.5, r)
                x4, y4 = vector((x0, y0), angle + a2 * 0.5, r)

                p1_x, p1_y = x0 + r, y0
                p2_x, p2_y = x0, y0 - r
                p3_x, p3_y = p1_x, p1_y - r * f
                p4_x, p4_y = p2_x + r * f, p2_y

            elif w1 < 0 and h1 < 0:

                x3, y3 = vector((x0, y0), 180 + angle - a1 * 0.5, r)
                x4, y4 = vector((x0, y0), 180 + angle + a2 * 0.5, r)

                p2_x, p2_y = x0 - r, y0
                p1_x, p1_y = x0, y0 - r
                p3_x, p3_y = p1_x - r * f, p1_y
                p4_x, p4_y = p2_x, p2_y - r * f

            else:

                x3, y3 = vector((x0, y0), 180 + angle - a1 * 0.5, r)
                x4, y4 = vector((x0, y0), 180 + angle + a2 * 0.5, r)

                p1_x, p1_y = x0 - r, y0
                p2_x, p2_y = x0, y0 + r
                p3_x, p3_y = p1_x, p1_y + r * f
                p4_x, p4_y = p2_x - r * f, p2_y

            # draw angle arch
            c = self.color_angle + (self.stroke_alpha,)
            stroke(*c)
            fill(None)
            newPath()
            moveTo((p1_x, p1_y))
            curveTo((p3_x, p3_y), (p4_x, p4_y), (p2_x, p2_y))
            drawPath()

            # draw angle captions
            stroke(None)
            fill(*self.color_angle)

            # caption angle 1
            caption_a1 = '%.2f' % a1
            a1_w, a1_h = textSize(caption_a1)
            a1_x = x3 - (a1_w * 0.5)
            a1_y = y3 - (a1_h * 0.4)
            textBox(caption_a1, (a1_x, a1_y, a1_w, a1_h), align='center')

            # caption angle 2
            caption_a2 = '%.2f' % a2
            a2_w, a2_h = textSize(caption_a2)
            a2_x = x4 - (a2_w * 0.5)
            a2_y = y4 - (a2_h * 0.5)
            textBox(caption_a2, (a2_x, a2_y, a2_w, a2_h), align='center')

        # draw angles for outcoming BCP
        if self.draw_out and not int(w2) == 0 and not int(h2) == 0:

            handle_length, angle = get_vector((x0, y0), (x2, y2))
            r = handle_length * self.radius

            a1 = angle % 90
            a2 = 90 - a1

            if w2 > 0 and h2 > 0:

                x5, y5 = vector((x0, y0), angle - a1 * 0.5, r)
                x6, y6 = vector((x0, y0), angle + a2 * 0.5, r)

                p1_x, p1_y = x0 + r, y0
                p2_x, p2_y = x0, y0 + r
                p3_x, p3_y = p1_x, p1_y + r * f
                p4_x, p4_y = p2_x + r * f, p2_y

            elif w2 > 0 and h2 < 0:

                x5, y5 = vector((x0, y0), angle - a1 * 0.5, r)
                x6, y6 = vector((x0, y0), angle + a2 * 0.5, r)

                p1_x, p1_y = x0, y0 - r
                p2_x, p2_y = x0 + r, y0
                p3_x, p3_y = p1_x + r * f, p1_y
                p4_x, p4_y = p2_x, p2_y - r * f

            elif w2 < 0 and h2 < 0:

                x5, y5 = vector((x0, y0), 180 + angle - a1 * 0.5, r)
                x6, y6 = vector((x0, y0), 180 + angle + a2 * 0.5, r)

                p1_x, p1_y = x0 - r, y0
                p2_x, p2_y = x0, y0 - r
                p3_x, p3_y = p1_x, p1_y - r * f
                p4_x, p4_y = p2_x - r * f, p2_y

            else:

                x5, y5 = vector((x0, y0), 180 + angle - a1 * 0.5, r)
                x6, y6 = vector((x0, y0), 180 + angle + a2 * 0.5, r)

                p1_x, p1_y = x0 - r, y0
                p2_x, p2_y = x0, y0 + r
                p3_x, p3_y = p1_x, p1_y + r * f
                p4_x, p4_y = p2_x - r * f, p2_y

            # draw angle arch
            c = self.color_angle + (self.stroke_alpha,)
            stroke(*c)
            fill(None)
            newPath()
            moveTo((p1_x, p1_y))
            curveTo((p3_x, p3_y), (p4_x, p4_y), (p2_x, p2_y))
            drawPath()

            # draw angle captions
            stroke(None)
            fill(*self.color_angle)

            # caption angle 1
            caption_a1 = '%.2f' % a1
            a1_w, a1_h = textSize(caption_a1)
            a1_x = x5 - (a1_w * 0.5)
            a1_y = y5 - (a1_h * 0.4)
            textBox(caption_a1, (a1_x, a1_y, a1_w, a1_h), align='center')

            # caption angle 2
            caption_a2 = '%.2f' % a2
            a2_w, a2_h = textSize(caption_a2)
            a2_x = x6 - (a2_w * 0.5)
            a2_y = y6 - (a2_h * 0.5)
            textBox(caption_a2, (a2_x, a2_y, a2_w, a2_h), align='center')

        # done
        restore()
