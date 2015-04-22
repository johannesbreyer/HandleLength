from mojo.events import addObserver, removeObserver
from mojo.drawingTools import *
from math import sqrt

# handlesLenght Object definition
class handlesLength(object):

    def __init__(self):
        addObserver(self, 'draw_handles', 'draw')
        addObserver(self, 'remove_observers', 'glyphWindowWillClose')
        
    def remove_observers(self, info):
        removeObserver(self, 'draw')
        removeObserver(self, 'glyphWindowWillClose')
        print 'removed Observers'
                
    def draw_handles(self, info):
        # print 'dpoing stuff'
        g = CurrentGlyph()
        for c in g:
            for bPoint in c.bPoints:
                x, y = bPoint.anchor[0], bPoint.anchor[1] 
                # get absolute coordinates 
                x_bcpIn = bPoint.anchor[0] + bPoint.bcpIn[0]
                y_bcpIn = bPoint.anchor[1] + bPoint.bcpIn[1]
                pt_bcpIn = x_bcpIn, y_bcpIn

                x_bcpOut = bPoint.anchor[0] + bPoint.bcpOut[0]
                y_bcpOut = bPoint.anchor[1] + bPoint.bcpOut[1]
                pt_bcpOut = x_bcpOut, y_bcpOut

                # calculate deltas
                b1, c1 = bPoint.bcpIn  # unpack bPoint.bcpIn tuple
                b2, c2 = bPoint.bcpOut # unpack bPoint.bcpOut tuple
                #print bPoint.bcpIn
                if b1 != 0 or c1 != 0:
                    # calculate d1 with Pithagoras help
                    distanceBcpIn = sqrt(b1*b1 + c1*c1)
                    distanceBcpIn = '%.2f' % distanceBcpIn
                    # print "HandleLenght IN is", distanceBcpIn
                    text(distanceBcpIn, (x + b1 * 0.5, y + c1 * 0.5))
                if b2 != 0 or c2 != 0:
                    # calculate d2 with Pithagoras help
                    distanceBcpOut = sqrt(b2*b2 + c2*c2)
                    distanceBcpOut = '%.2f' % distanceBcpOut
                    # print "HandleLenght OUT is", distanceBcpIn
                    font('Helvetica')
                    fill(0, 0, 1)
                    stroke(None)
                    fontSize(25)
                    text(distanceBcpOut, (x + b2 * 0.5, y + c2 * 0.5))
                
handlesLength()
