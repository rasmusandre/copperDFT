import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.io.trajectory import PickleTrajectory
from ase.optimize.bfgs import BFGS
from ase.db import connect
import matplotlib.pyplot as plt
from gpaw import GPAW
from gpaw import PW
from gpaw import FermiDirac

copper = bulk('Cu', 'fcc', a=3.62)

calc=GPAW(mode=PW(340),
          h=0.2,
          xc='PBE',
          nbands=-2,
          kpts=(8,8,8),
          occupations=FermiDirac(0.1),
          txt='cubulk_dos.txt')

copper.set_calculator(calc)
copper.get_potential_energy()
calc.write('cu.gpw', mode='all')


from ase import *
from ase.dft.dos import DOS
from gpaw import GPAW , restart
import pylab as p

slab , calc = restart('cu.gpw')
e, dos = calc.get_dos(spin=0, npts=2001, width=0.1)
e_f = calc.get_fermi_level()

#db = connect('cu_dos.db')
#db.write(slab, number_of_atoms = 1)
#
#for obj in db.select(number_of_atoms = 1):
#    print(obj)

bs = calc.band_structure()
bs.plot(filename='bandstructure.png', show=True, emax=10.0)

plt.figure(0)
plt.plot(dos, e)
plt.plot([0,5], e_f*np.ones(2))
plt.xlim(0,5)
plt.ylim(0, 10)
plt.xlabel('DOS')
plt.ylabel('Energy')
plt.savefigure('cu_dos.txt')
#my_fig.savefig('cu_dos', bbox_inches='tight')
plt.show()

#p.subplot(211)
#p.plot(e, dos)
#p.plot(e_f, dos)
#p.grid(True)
#p.axis([-15, 10, None , None])
#p.ylabel('DOS')
