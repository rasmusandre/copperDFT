from ase.build import bulk
from gpaw import GPAW, PW, FermiDirac
from ase.dft.kpoints import ibz_points, bandpath
from ase.phonons import Phonons
from ase.db import connect
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def create_plt(database):



    db = connect(database)

    for outer_obj in db.select():
            obj = outer_obj['data']
            q = obj['q']
            Q = obj['Q']
            omega_kn = obj['omega_kn']
            point_names = obj['point_names']
            dos_e = obj['dos_e']
            omega_e = obj['omega_e']


    plt.figure(1, (8, 6))
    plt.axes([.1, .07, .67, .85])

    for n in range(len(omega_kn[0])):
        omega_n = omega_kn[:, n]
        plt.plot(q, omega_n, 'k-', lw=2)



    plt.xticks(Q, point_names, fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlim(q[0], q[-1])
    plt.ylabel("Frequency ($\mathrm{meV}$)", fontsize=22)
    plt.grid('on')

    plt.axes([.8, .07, .17, .85])
    plt.fill_between(dos_e, omega_e, y2=0, color='lightgrey', edgecolor='k', lw=1)

    plt.ylim(0, 35)
    plt.xticks([], [])
    plt.yticks([], [])
    plt.xlabel("DOS", fontsize=18)
    plt.show()

    deb_plot(omega_e, dos_e)

def deb_plot(omegas, dos):

    vol_cu = 11.664
    vol_fe = 11.575

    bm_cu = 1350 #*10**9
    bm_fe = 1850.7 #*10**9

    dens_cu = 8.96*(10**6)/1000
    dens_fe = 7.874*(10**6)/1000

    atomic_weight_cu = 63.546
    atomic_weight_fe = 55.845

    n_cu = 4/vol_cu
    n_fe = 4/vol_fe

    rs_cu = (3/(4*np.pi*n_cu))**(1/3)
    rs_fe = (3/(4*np.pi*n_fe))**(1/3)

    deb_temp_cu = 67.48*(rs_cu*bm_cu/atomic_weight_cu)**(1/2)
    deb_temp_fe = 67.48*(rs_fe*bm_fe/atomic_weight_fe)**(1/2)

    speed_cu = (bm_cu/dens_cu)**(1/2)
    speed_fe = (bm_fe/dens_fe)**(1/2)

    plancks = 1.054*10**-34
    ev = 1.6*10**-19
    boltzmann = 1.38*10**-23

    deb_freq_cu = deb_temp_cu*boltzmann/plancks
    deb_freq_fe = deb_temp_fe*boltzmann/plancks

    omegas_ang = [w*ev/(plancks*1000) for w in omegas]
    dos_deb = [w**2 for w in omegas_ang]

    omegas_deb = [w for w in omegas_ang if w < deb_freq_fe]
    dos_deb = dos_deb[:len(omegas_deb)]
    dos_deb[-1] = 0
    #normalization_factor = np.max(dos)/np.max(dos_deb)

    #dos_deb = [i*normalization_factor for i in dos_deb]

    int_dos = integrate.simps(dos, omegas_ang)
    int_dos_deb = integrate.simps(dos_deb, omegas_deb)

    dos_deb = [i*int_dos/int_dos_deb for i in dos_deb]


    plt.figure(0)
    plt.plot(omegas_deb, dos_deb)
    plt.plot(omegas_ang, dos)
    plt.legend(['Debye DOS', 'Calculated DOS'])
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('DOS')
    plt.ylim(0,max(dos_deb)+10)
    plt.show()



db = 'fe_phon_band.db'
create_plt(db)
