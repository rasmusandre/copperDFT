import numpy as np
from ase import Atoms
from ase.lattice import bulk
from ase.io.trajectory import PickleTrajectory
from ase.optimize.bfgs import BFGS
from gpaw import GPAW
from gpaw import PW
from gpaw import FermiDirac

silicon = bulk('Si', 'diamond', a=5.459)

calc=GPAW(mode=PW(400),                # Energycutoff for planewaves [eV]
          h=0.2,                       # The distance between gridpoints AA^-1
          xc='PBE',                    # xc-functional
          nbands=20,                   # number of bands
          kpts=(20,20,20),             # number of k-points
          occupations=FermiDirac(0.1), # Fermi temperature [eV]
          txt='sibulk_dos.txt')

silicon.set_calculator(calc)
silicon.get_potential_energy()
calc.write('silicon.gpw', mode='all')


from ase import *
from ase.dft.dos import DOS
from gpaw import GPAW , restart
import pylab as p

slab , calc = restart('silicon.gpw')
e, dos = calc.get_dos(spin=0, npts=2001, width=0.1)
e_f = calc.get_fermi_level()

p.subplot(211)
p.plot(e-e_f, dos)
p.grid(True)
p.axis([-15, 10, None , None])
p.ylabel('DOS')

p.subplot(212)
p.plot(e-e_f, dos)
p.grid(True)
p.axis([-1, 1, None , None])
p.ylabel('DOS')
p.show()
