"""Bulk Al(fcc) test"""
from __future__ import print_function
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW, FermiDirac

import matplotlib.pyplot as plt

k_vec = []
e_c = []

for k in range(2,10):

    name = 'Cu-fcc'
    a = 3.62  # fcc lattice parameter
    b = a / 2

    bulk = Atoms('Cu',
                 cell=[[0, b, b],
                       [b, 0, b],
                       [b, b, 0]],
                 pbc=True)

    #view(bulk)


    calc = GPAW(mode=PW(340), nbands = -2, xc='PBE', kpts=(k, k, k), occupations=FermiDirac(0.1),
                txt=name + '.txt')

    bulk.set_calculator(calc)

    energy = bulk.get_potential_energy()
    calc.write(name + '.gpw')
    print('Energy:', energy, 'eV')
    k_vec.append(k)
    e_c.append(energy)

plt.figure(0)
plt.semilogx([i**3 for i in k_vec], e_c)
plt.xlabel('Number of k-points')
plt.ylabel('Ev/atom')
plt.show()
