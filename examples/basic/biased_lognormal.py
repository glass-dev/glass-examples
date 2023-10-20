"""
Biased lognormal fields
=======================

This example shows how to compute a biased lognormal field by rescaling the
*alms* of the matter field with a biased angular power spectrum.

**WARNING**: This model has a major caveat. See below.

"""

# %%
# Setup
# -----
#
# This example simulates a lognormal matter field and a biased tracer field.
#
# The precomputed angular matter power spectra from the :doc:`/basic/shells`
# example are used, so the simulation is set up in the same way.

import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

# use the CAMB cosmology that generated the matter power spectra
import camb
from cosmology import Cosmology

# GLASS imports
from glass.shells import distance_grid, partition, tophat_windows
from glass.fields import (discretized_cls, lognormal_gls, generate_alms,
                          biased_cls, rescaled_alm, alm_to_lognormal, getcl)
from glass.user import load_cls


# cosmology for the simulation
h = 0.7
Oc = 0.25
Ob = 0.05

# basic parameters of the simulation
nside = lmax = 256

# set up CAMB parameters for matter angular power spectrum
pars = camb.set_params(H0=100*h, omch2=Oc*h**2, ombh2=Ob*h**2,
                       NonLinear=camb.model.NonLinear_both)

# get the cosmology from CAMB
cosmo = Cosmology.from_camb(pars)

# shells of 200 Mpc in comoving distance spacing
zgrid = distance_grid(cosmo, 0., 1., dx=200.)

# uniform matter weight function
shells = tophat_windows(zgrid)

# load the previously-computed angular matter power spectra
cls = load_cls("cls.npz")

# apply angular discretisation to cls
cls = discretized_cls(cls, nside=nside, lmax=lmax, ncorr=3)

# %%
# Matter
# ------
#
# The matter fields in this example are lognormal.  To simulate both matter and
# the biased tracer field, we require the Gaussian *alm* array for each shell.
# We therefore use the :func:`~glass.fields.generate_alms` generator, instead
# of generating the lognormal matter fields directly.

# compute Gaussian angular power spectra for lognormal matter fields
gls = lognormal_gls(cls)

# generator for Gaussian random field alms
alms = generate_alms(gls, ncorr=3)

# %%
# Biased tracer
# -------------
#
# The biased tracer fields in this example have a single bias factor *bias*,
# but this could be an array with a different value for each shell.  The
# biasing works by first applying the bias factors to the original *cls* array
# using the :func:`~glass.fields.biased_cls` function.  We then compute the
# Gaussian angular power spectra for biased lognormal fields.
#
# This is just one example of how to obtained biased tracer fields.  The
# Gaussian angular power spectra could be obtained in any number of ways.

# this is the bias we want to implement
bias = 1.8

# apply linear bias factor to the cls
cls_b = biased_cls(cls, bias)

# compute Gaussian cls for the biased lognormal galaxy fields
gls_b = lognormal_gls(cls_b)

# %%
# This example will produce an integrated density for the unbiased and biased
# fields.  Here, we are making an example *dndz* distribution, and computing
# its contribution to each matter shell.

# localised redshift distribution
# the actual density per arcmin2 does not matter here, it is never used
z = np.linspace(0, 1, 101)
dndz = np.exp(-(z - 0.5)**2/(0.1)**2)

# partition the dndz function into a ngal value for each shell
ngal = partition(z, dndz, shells)

# %%
# Simulation
# ----------
# The simulation generates the Gaussian *alm* for each matter shell and
# computes its lognormal matter field.  The *alm* array is rescaled with the
# biased *gls* to compute the biased lognormal tracer field.  Both are then
# added to an integrated number density field, using the shell's contribution
# *ngal* to the total redshift distribution.

# initialise maps for biased and unbiased total number densities
ntot = np.zeros(12 * nside**2)
ntot_b = np.zeros(12 * nside**2)

# main loop to simulate the matter fields iteratively
for i, alm in enumerate(alms):

    # first, compute the lognormal matter field
    delta = alm_to_lognormal(alm, nside)

    # now rescale the alm to the biased lognormal field for galaxies
    alm_b = rescaled_alm(alm, getcl(gls_b, i), getcl(gls, i))

    # compute the biased lognormal galaxies field
    delta_b = alm_to_lognormal(alm_b, nside)

    # add both fields to number density
    ntot += ngal[i] * (1 + delta)
    ntot_b += ngal[i] * (1 + delta_b)

# %%
# Analysis
# --------
# To make sure the biased tracer field works as expected, we compute the
# density contrast of the unbiased and biased integrated fields, then compare
# their bias to the linear bias factor we used above.

# this is the mean number density over the entire distribution
nbar = np.trapz(dndz, z)

# compute the integrated density contrasts
delta_tot = (ntot - nbar)/nbar
delta_tot_b = (ntot_b - nbar)/nbar

# get the angular power spectra of the number density maps
sim_cls = hp.anafast([delta_tot, delta_tot_b],
                     pol=False, lmax=lmax, use_pixel_weights=True)

# plot the unbiased and biased cls
l = np.arange(lmax+1)
fig, ax = plt.subplots(2, 1, sharex=True, sharey=True, layout="constrained")
ax[0].plot(l, (sim_cls[1]/sim_cls[0])**0.5, "-k", lw=2, label="simulated bias (biased $\\times$ biased)")
ax[0].axhline(bias, c="r", ls="-", lw=1, label="bias factor")
ax[0].legend(frameon=False)
ax[0].set_ylabel(r"bias factor")
ax[1].plot(l, sim_cls[2]/sim_cls[0], "-k", lw=2, label="simulated bias (biased $\\times$ unbiased)")
ax[1].axhline(bias, c="r", ls="-", lw=1, label="bias factor")
ax[1].legend(frameon=False)
ax[1].set_ylabel(r"bias factor")
ax[1].set_xscale("log")
ax[1].set_xlabel(r"angular mode number $l$")
ax[1].set_ylim(bias - 0.25, bias + 0.25)
plt.show()

# %%
# The results show that the biased lognormal tracer is able to capture the
# linear bias in the auto-correlation of the biased tracer reasonably well.
# **However, there is a significant deviation from the linear model in the
# cross-correlation between biased tracer and unbiased field.**  The biased
# lognormal tracer model should therefore only be used where this defect is
# acceptable.
