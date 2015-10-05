# build RoboFont Extension

import os
import shutil

from mojo.extensions import ExtensionBundle

lib_path = os.path.dirname(__file__)
extension_file = 'MeasureHandles.roboFontExt'
extension_path = os.path.join(os.path.join(lib_path, 'extension'), extension_file)
# extension_html = os.path.join(lib_path, "_docs")
extension_lib_path = os.path.join(extension_path, 'lib')

print 'building extension...',
B = ExtensionBundle()
B.name = u"Measure Handles Tool"
B.developer = u'Gustavo Ferreira, Johannes Breyer'
B.developerURL = 'http://hipertipo.com/'
B.version = "0.1"
B.mainScript = "MeasureHandlesTool.py"
B.launchAtStartUp = 1
B.addToMenu = []
B.requiresVersionMajor = '1'
B.requiresVersionMinor = '5'
B.infoDictionary["html"] = 0
B.infoDictionary["com.robofontmechanic.Mechanic"] = {
    "repository" : "johannesbreyer/HandleLength",
    "description" : "A tool to display length & angle of bezier handles in a glyph",
}
B.save(extension_path, libPath=lib_path, htmlPath=None, resourcesPath=None, pycOnly=False)
print 'done.\n'
