from ase.build import bulk
from ase import Atoms, Atom
from ase.db import connect
from ase.optimize import BFGS
from ase.visualize import view
import numpy as np
from gpaw import GPAW, PW, FermiDirac
import sys
from ase.calculators.emt import EMT

a = 5
e_cut = 600
nbands = -2
xc = 'PBE'
k_pts = 8
smear = 0.1
#
#
# atoms = 1
# bulk_mat = bulk('Cu','fcc',a)*(1,atoms,atoms)
# print(bulk_mat.cell)
#
#
# calc = GPAW(mode=PW(e_cut), nbands = nbands,
#             xc='PBE', kpts=(k_pts,k_pts,k_pts),
#             occupations=FermiDirac(smear), txt='Cu.out')
#
# bulk_mat.set_calculator(calc)
# print(bulk_mat.get_potential_energy())
# dyn = LBFGS(bulk_mat)
# dyn.run(fmax=0.05)
# #bulk_mat.get_potential_energy()
# calc.write('Cu.gpw')
# print(bulk_mat.get_potential_energy())
# print(bulk_mat.cell)
# view(bulk_mat)

# d = 5
#
# copper = Atoms('Cu',
#               cell=[[d/2, d/2, 0],
#                          (d/2, 0, d/2),
#                          (0, d/2, d/2)],pbc=True)*(1,1,1)
# # calc = GPAW(mode=PW(e_cut), nbands = nbands,
# #             xc='PBE', kpts=(k_pts,k_pts,k_pts),
# #             occupations=FermiDirac(smear), txt='Cu.out')
#
# calc = GPAW()
# copper.set_calculator(calc)
# print(copper.cell)
# print(copper.positions)
# dyn = BFGS(copper)
# dyn.run(fmax=0.05)
# print(copper.positions)
# print(copper.cell)

system = Atoms('Cu2', positions=[[0.0, 0.0, 0.0],
                                [0.0, 0.0, 3.62/2]])
calc = EMT()
print(system.positions)
system.set_calculator(calc)

opt = BFGS(system, trajectory='h2.emt.traj')

opt.run(fmax=0.05)
print(system.positions)
