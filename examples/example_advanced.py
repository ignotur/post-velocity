from post_velocity import post_velocity
from math import *
import matplotlib.pyplot as plt

parallax = 1.3616973828503283   ## mas
parallax_error = 0.31826717     ## mas
pmra = 70.22832802893967        ## mas/year
pmra_error = 0.31611034         ## mas/year
pmdec = -195.65413513344822     ## mas/year
pmdec_error = 0.2825489         ## mas/year
l = radians(245.99334300224004) ## degrees to be converted to radians while working with the package
b = radians(13.599432251899845) ## degrees to be converted to radians while working with the package

meas = pmra, pmra_error, pmdec, pmdec_error, parallax, parallax_error, l, b

## Posterior will be computed for the velocity range from min_vt to max_vt
min_vt = 30   ## km/s
max_vt = 3000 ## km/s

## Vary velocity prior
sigma1000 = 1000.0 ## km/s
sigma3000 = 3000.0 ## km/s

vtl1, pvtl1, idx025, idx50, idx975 = post_velocity.compute_posterior (meas, min_vt=min_vt, max_vt=max_vt, sigma=sigma1000)
vtl3, pvtl3, idx025, idx50, idx975 = post_velocity.compute_posterior (meas, min_vt=min_vt, max_vt=max_vt, sigma=sigma3000)

plt.plot (vtl1, pvtl1, 'k-', label=r'$\sigma=1000$ km/s')
plt.plot (vtl3, pvtl3, 'b--', label=r'$\sigma=3000$ km/s')

plt.xlabel(r'$v_t$ (km/s)')
plt.ylabel(r'Probability density')
plt.ylim([0,1.02])
plt.legend()
plt.savefig ('posterior_vt_sigma.pdf')
plt.show()
