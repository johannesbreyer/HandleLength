# [h] Measure Handles Tool

import os
from AppKit import NSImage
from mojo.events import *
from MeasureHandles import MeasureHandles

# objects

class MeasureHandlesTool(EditingTool):

    icon_file_name = 'measure-handles-tool-icon.pdf'
    dirname = os.path.dirname(__file__)
    toolbar_icon = NSImage.alloc().initByReferencingFile_(os.path.join(dirname, icon_file_name))

    def setup(self):
        glyph = self.getGlyph()
        self.calculator = MeasureHandles(glyph)

    def draw(self, scale):
        self.calculator.draw(scale)

    def getToolbarIcon(self):
        return self.toolbar_icon

    def getToolbarTip(self):
        return "Measure Handles Tool"

# install tool

installTool(MeasureHandlesTool())
