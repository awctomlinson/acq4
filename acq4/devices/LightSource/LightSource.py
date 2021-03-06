# -*- coding: utf-8 -*-
from acq4.devices.Device import *
from PyQt4 import QtCore, QtGui
import acq4.util.Mutex as Mutex
from collections import OrderedDict


class LightSource(Device):
    """Device tracking the state and properties of multiple illumination sources.
    """
    # emitted when the on/off status of a light changes
    sigLightChanged = QtCore.Signal(object, object)  # self, light_name
    
    def __init__(self, dm, config, name):
        Device.__init__(self, dm, config, name)
        self._sources = OrderedDict()  # [name: {'active': bool, 'wavelength': float, 'power': float, ...}, ...]
        self._lock = Mutex.Mutex()
        self._xkeysDevs = []

    def addSource(self, name, conf):
        self._sources[name] = conf
        if 'xkey' in conf:
            devname, row, col = self._sources[name]['xkey']
            dev = self.dm.getDevice(devname)
            if dev not in self._xkeysDevs:
                dev.sigStateChanged.connect(self._xkeyStateChanged)
                self._xkeysDevs.append(dev)

    def describe(self, onlyActive=True):
        """Return a description of the current state of all active light sources.

        If onlyActive is False, then information for all sources will be returned, whether or not they are active.
        """
        if onlyActive:
            return OrderedDict([(n,s) for n,s in self._sources.items() if s['active']])
        else:
            return self._sources.copy()

    def activeSources(self):
        """Return the names of all active light sources.
        """
        return [s['name'] for s in self._sources if s['active']]

    def sourceActive(self, name):
        """Return True if the named light source is currently active.
        """
        return self._sources[name]['active']

    def setSourceActive(self, name, active):
        """Activate / deactivate a light source.
        """
        raise NotImplementedError()

    def _updateXkeyLight(self, name):
        if 'xkey' in self._sources[name]:
            devname, row, col = self._sources[name]['xkey']
            dev = self.dm.getDevice(devname)
            bl = dev.getBacklights()
            bl[row,col] = int(self._sources[name]['active'])
            dev.setBacklights(bl)

    def _xkeyStateChanged(self, dev, changes):
        keych = changes.get('keys')
        if keych is None:
            return
        for pos, state in keych:
            if state is False:
                continue
            for name, source in self._sources.items():
                if source.get('xkey')[1:] == pos:
                    self.setSourceActive(name, not self.sourceActive(name))




