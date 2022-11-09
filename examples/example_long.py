from post_velocity import *

parallax = 1.3616973828503283   ## mas
parallax_error = 0.31826717     ## mas
pmra = 70.22832802893967        ## mas/year
pmra_error = 0.31611034         ## mas/year
pmdec = -195.65413513344822     ## mas/year
pmdec_error = 0.2825489         ## mas/year
l = radians(245.99334300224004) ## degrees to be converted to radians while working with the package
b = radians(13.599432251899845) ## degrees to be converted to radians while working with the package

### Setting parameters of the Galactic prior

hz = 0.33   ## kpc
hr = 1.70   ## kpc
Rsun = 8.34 ## kpc

meas = pmra, pmra_error, pmdec, pmdec_error, parallax, parallax_error, l, b

vtl, pvtl, idx025, idx50, idx975 = compute_posterior (meas, Rsun = Rsun, hz = hz, hr = hr)


varpi = parallax
sigma_varpi = parallax_error

dl = []  ## array to keep distances
ggl = [] ## array to keep conditional probability to measure parallax if distances is fixed
ffl = [] ## array to keep Galactic prior


for k in range (1, 10000):

    d = 0.001 * k

    dl.append (d)
    ggl.append (g (d, varpi, sigma_varpi))  ## 
    ffl.append (fD (d, l, b, hz, hr, Rsun)) ## Galactic prior for distances

ggl = np.asarray(ggl) / np.max(ggl)
ffl = np.asarray(ffl) / np.max(ffl)

tt = ggl*ffl ## here we compute posterior for distances
tt = tt / np.max(tt)

fig, axs = plt.subplots(2)

axs[0].plot (dl, ggl, '--', color='blue', label=r"$g_D (\varpi' | D)$", linewidth=2)
axs[0].plot (dl, ffl, ':', color='black', label=r'$f_D (D; l, b)$', linewidth=2)
axs[0].plot (dl, tt, '-', color='red', label=r"$p_D (D | \varpi')$", linewidth=3)
axs[0].set_xlim([0, 2.5])
axs[0].set_xlabel('D (kpc)')
axs[0].set_ylabel('Relative probability')
axs[0].legend()

axs[1].plot ([vtl[idx025], vtl[idx025]], [-1,1.5], '--', color='red', linewidth=2)
axs[1].plot ([vtl[idx50],  vtl[idx50]], [-1,1.5], ':',   color='red', linewidth=2)
axs[1].plot ([vtl[idx975], vtl[idx975]], [-1,1.5], '--', color='red', linewidth=2)

axs[1].plot (vtl, pvtl, color='red', linewidth=3, label=r"$p(v_t | \varpi', \mu_\alpha', \mu_\delta )$")

axs[1].set_xlabel(r'$v_t$ (km s$^{-1}$)')
axs[1].set_ylabel('Relative probability')
axs[1].set_ylim([0.0, 1.1])
axs[1].legend()
plt.tight_layout()
plt.savefig ('posterior_distance_vt.pdf')
plt.show()



