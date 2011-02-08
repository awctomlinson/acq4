# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from lib.analysis.AnalysisModule import AnalysisModule
#from flowchart import *
import os
from advancedTypes import OrderedDict
import debug
#import FileLoader
#import DatabaseGui
#import FeedbackButton
from MosaicEditorTemplate import *
import DataManager

class MosaicEditor(AnalysisModule):
    def __init__(self, host):
        AnalysisModule.__init__(self, host)
        
        self.ctrl = QtGui.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.ctrl)
        
        
        self._elements_ = OrderedDict([
            ('File Loader', {'type': 'fileInput', 'size': (200, 300), 'host': self}),
            ('Mosaic', {'type': 'ctrl', 'object': self.ctrl, 'pos': ('right',), 'size': (600, 200)}),
            ('Canvas', {'type': 'canvas', 'pos': ('bottom', 'Mosaic'), 'size': (600, 600)}),
        ])
        
        self.initializeElements()

        self.ui.canvas = self.getElement('Canvas', create=True)
        self.items = {}
        self.cells = {}
        
        self.connect(self.ui.canvas, QtCore.SIGNAL('itemTransformChangeFinished'), self.itemMoved)
        self.ui.exportSvgBtn.clicked.connect(self.exportSvg)
        
        
        atlasDir = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'atlas')
        fh = DataManager.getHandle(os.path.join(atlasDir, 'CN_coronal.png'))
        scale = 3.78e-6
        pos = (-676*scale/2., -577*scale/2.)
        self.atlas = self.ui.canvas.addImage(fh, pos=pos, scale=(scale, scale))
        self.atlas.setMovable(False)


    def loadFileRequested(self, f):
        canvas = self.getElement('Canvas')
        if f is None:
            return
            
        if f.info().get('dirType', None) == 'Cell':
            item = canvas.addMarker(handle=f, scale=[20e-6,20e-6])
            self.items[item] = f
        else:
            item = canvas.addFile(f)
            self.items[item] = f
            
            item.timestamp = f.info()['__timestamp__']
            if not item.hasUserTransform():
                ## Record the timestamp for this file, see what is the most recent transformation to copy
                best = None
                for i2 in self.items:
                    if i2 is item:
                        continue
                    if not hasattr(i2, 'timestamp'):
                        continue
                    if i2.timestamp < item.timestamp:
                        if best is None or i2.timestamp > best.timestamp:
                            best = i2
                            
                if best is None:
                    return
                    
                trans = best.saveTransform()
                item.restoreTransform(trans)
                
        canvas.selectItem(item)


    def itemMoved(self, canvas, item):
        """Save an item's transformation if the user has moved it. 
        This is saved in the 'userTransform' attribute; the original position data is not affected."""
        if item not in self.items:
            return
        fh = self.items[item]
        trans = item.saveTransform()
        fh.setInfo(userTransform=trans)
        #print fh, "moved"
        
    def exportSvg(self):
        self.ui.canvas.view.writeSvg()