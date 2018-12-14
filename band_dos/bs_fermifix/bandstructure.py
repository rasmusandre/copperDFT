# Creates: bandstructure.png
"""Band structure tutorial

Calculate the band structure of Si along high symmetry directions
Brillouin zone
"""
# P1
from ase import Atoms
from ase.build import bulk
from gpaw import GPAW, PW, FermiDirac
import matplotlib.pyplot as plt
import numpy as np
b = 3.64
k = 3
# Perform standard ground state calculation (with plane wave basis)
#si =  Atoms('Fe', scaled_positions=[(0, 0, 0)], magmoms=[k], cell=(b, b, b), pbc=True)
# si = bulk('Cu','fcc',b)
#
# calc = GPAW(mode=PW(600),
#             xc='PBE',
#             kpts=(8, 8, 8),
#             random=True,  # random guess (needed if many empty bands required)
#             occupations=FermiDirac(0.1),
#             txt='Si_gs.txt')
# si.calc = calc
# si.get_potential_energy()
# calc.write('Si_gs.gpw')
# P2
# Restart from ground state and fix potential:
calc = GPAW('Si_gs.gpw',
            nbands=16,
            fixdensity=True,
            symmetry='off',
            kpts={'path': 'GXWLGK', 'npoints': 60},
            convergence={'bands': 8}, txt='Si2_gs.txt')

calc.get_potential_energy()
e_f = calc.get_fermi_level()
#e1, dos1 = calc.get_dos(spin=1, npts=2001, width=0.1) #What is spin?
e0, dos0 = calc.get_dos(spin=0, npts=2001, width=0.1)

plt.figure(0)
plt.plot(dos0, [i-e_f for i in e0],'b')
plt.plot([0,4], [0,0],'r--')
plt.ylim(-10, 10)
plt.xlim(0,4)
plt.legend(['DOS', 'Fermi level'],fancybox=True, framealpha=1,shadow=True,prop={'size': 10})
plt.xlabel('Density of states [1/eV]')
plt.ylabel('Energy [eV]')
#plt.show()
#
# print(e_f)
# P3
bs = calc.band_structure()
bs.write('my_js.js')


for i in range(0,len(bs.energies)):
    for k in range(0, len(bs.energies[i])):
        for j in range(0, len(bs.energies[i][k])):
            bs.energies[i][k][j] = bs.energies[i][k][j] - e_f
bs.reference = 0
ax = bs.plot(filename='bandstructure2.pdf',ylabel = 'Energies [eV]', show=True, emin=-10, emax=10)
#bs.finish_plot('bandstructure2.pdf', True, ['Fermi level','Spin up', 'Spin down'])
