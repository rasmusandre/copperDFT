# Creates: bandstructure.png
"""Band structure tutorial

Calculate the band structure of Si along high symmetry directions
Brillouin zone
"""
# P1
from ase.build import bulk
from gpaw import GPAW, PW, FermiDirac
import matplotlib.pyplot as plt
import numpy as np

# Perform standard ground state calculation (with plane wave basis)
si = bulk('Cu', 'fcc', 3.62)
calc = GPAW(mode=PW(340),
            xc='PBE',
            kpts=(8, 8, 8),
            random=True,  # random guess (needed if many empty bands required)
            occupations=FermiDirac(0.01),
            txt='Si_gs.txt')
si.calc = calc
si.get_potential_energy()
calc.write('Si_gs.gpw')
# P2
# Restart from ground state and fix potential:
calc = GPAW('Si_gs.gpw',
            nbands=16,
            fixdensity=True,
            symmetry='off',
            kpts={'path': 'GXWKL', 'npoints': 60},
            convergence={'bands': 8})

calc.get_potential_energy()
e_f = calc.get_fermi_level()
e, dos = calc.get_dos(spin=0, npts=2001, width=0.1)

plt.figure(0)
plt.plot(dos, e)
plt.plot([0,5], e_f*np.ones(2))
plt.ylim(-1,17.5)
plt.show()

print(e_f)
# P3
bs = calc.band_structure()
bs.plot(filename='bandstructure.png', show=True, emax=10.0)
