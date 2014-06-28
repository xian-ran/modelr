# -*- coding: utf-8 -*-
'''
===================
ForwardModel.py
===================

Provide the forward model object.

@author: Ben Bougher
'''
import matplotlib
matplotlib.use('Agg')
from modelr.reflectivity import get_reflectivity, do_convolve
import os
import numpy as np

import json

class ForwardModel(object):

    def __init__(self, earth_model, seismic_model, plots):

        self.earth_model = earth_model
        
        self.seismic_model = seismic_model
        self.plots = plots

    def go(self):

        self.plots.go(self.seismic_model, self.earth_model)

        metadata = {}

        f = self.seismic_model.wavelet_cf()

        if np.ndim(f) == 0:
            f = [f]
        
        metadata["f"] = tuple(f)
        metadata["time"] = \
          tuple(np.arange(self.seismic_model.seismic.shape[0]) *
                self.seismic_model.dt*1000)

        metadata["trace"] = \
          tuple(range(1,self.seismic_model.n_sensors +1))

        # --------------------------
        # Added June 2014 by Matt
        # We're going to get a dictionary of rock properties back
        # from rock.get_moduli(). Planning to pass it to the
        # front end and tabulate.
        metadata["moduli"] = {"test key":"test value"}
        #for k,v in self.earth_model.property_map.iteritems():
        #    metadata["moduli"][k] = v.get_moduli()

        # --------------------------
        # Resuming normal service
        return self.plots.plot, metadata

    
