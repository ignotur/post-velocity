# post-velocity
Package to compute Bayesian posterior distribution for transversal velocity using parallaxes and proper motions

## Introduction

The transversal velocities of stars are important in many astrophysical applications such as a search for run-away stars and ultra-high velocity white dwarfs.
These velocities are often computed using measured parallaxes and proper motions of stars.
The parallax measurements are often have limited accuracy especially for distances of a few kpc.


## Simple usage

The example can be found in example.py

`
from post_velocity import *

parallax = 1.3616973828503283
parallax_error = 0.31826717
pmra = 70.22832802893967
pmra_error = 0.31611034
pmdec = -195.65413513344822
pmdec_error = 0.2825489
l = radians(245.99334300224004)
b = radians(13.599432251899845) 

meas = pmra, pmra_error, pmdec, pmdec_error, parallax, parallax_error, l, b
vtl, pvtl, idx025, idx50, idx975 = compute_posterior (meas)

plt.plot (vtl, pvtl)
plt.plot ([vtl[idx025], vtl[idx025]], [-0.5,1.1], 'r--')
plt.plot ([vtl[idx50],  vtl[idx50]],  [-0.5,1.1], 'r-')
plt.plot ([vtl[idx975], vtl[idx975]], [-0.5,1.1], 'r--')

plt.xlabel(r'$v_t$ (km/s)')
plt.ylabel(r'Probability density')
plt.ylim([0,1.02])
plt.savefig ('posterior_vt.pdf')
plt.show()

`


## References

Details of the calculations can be found in two articles:

Igoshev, Verbunt & Cator (2016) A&A, 591, A123, 10

Igoshev, Perets & Hallakoun (2022) ArXiv: 2209.09915
