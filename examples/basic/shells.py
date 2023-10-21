'''
Matter shell definition
=======================

This example demonstrates how matter shells are defined, and their angular power
spectra computed.

The the angular power spectra are saved here, so that they can be reused in
other examples without recomputing.

'''


# %%
# Compute
# -------
# Here we define the shells for these examples, and use CAMB to compute the
# angular matter power spectra for the shell definitions.

import camb
from cosmology import Cosmology

from glass.shells import distance_grid, tophat_windows
from glass.ext.camb import matter_cls, camb_tophat_weight
from glass.user import save_cls


# cosmology for the simulation
h = 0.7
Oc = 0.25
Ob = 0.05

# basic parameters of the simulation
lmax = 1000

# set up CAMB parameters for matter angular power spectrum
pars = camb.set_params(H0=100*h, omch2=Oc*h**2, ombh2=Ob*h**2,
                       NonLinear=camb.model.NonLinear_both)

# get the cosmology from CAMB
cosmo = Cosmology.from_camb(pars)

# shells of 200 Mpc in comoving distance spacing
zgrid = distance_grid(cosmo, 0., 1., dx=200.)

# uniform matter weight function
# CAMB requires linear ramp for low redshifts
shells = tophat_windows(zgrid, weight=camb_tophat_weight)

# compute angular matter power spectra with CAMB
cls = matter_cls(pars, lmax, shells)

# save the angular power spectra to file, to use in other examples
save_cls("cls.npz", cls)
