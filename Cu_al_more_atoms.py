"""Bulk Cu(fcc) test"""
from __future__ import print_function
from ase import Atoms, Atom
from ase.visualize import view
from gpaw import GPAW, PW, FermiDirac
import matplotlib.pyplot as plt
import numpy as np

def the_parameter_changer(start_iteration, end_iteration, increment, is_ec, is_kpts, is_smear, is_lat_const):

    #example 2, 10, 1, False, True, False

    changing_parameter = []
    energies = []

    for k in range(start_iteration, end_iteration, increment):

        name = 'Cu-fcc'
        a = 3.62  # fcc lattice parameter Cu [Å]
        b = a / 2

        if is_lat_const:
            b = k/200 # divide by 2 and by 100


        bulk = Atoms([Atom('Cu', (0, 0, 0))],
                      cell=np.array([[b, b, 0.0],
                                               [0.0, b, b],
                                               [b, 0.0, b]]), pbc = True).repeat((1, 2, 1))

        #view(bulk)
        if is_ec:
            calc = GPAW(mode=PW(k), nbands = -2, xc='PBE', kpts=(8, 8, 8), occupations=FermiDirac(0.1),
                        txt=name + '.txt')
        if is_kpts:
            calc = GPAW(mode=PW(340), nbands = -2, xc='PBE', kpts=(k, k, k), occupations=FermiDirac(0.1),
                        txt=name + '.txt')
        if is_smear:
            k = k/100
            calc = GPAW(mode=PW(340), nbands = -2, xc='PBE', kpts=(8, 8, 8), occupations=FermiDirac(k),
                        txt=name + '.txt')
        if is_lat_const:
            calc = GPAW(mode=PW(340), nbands = -2, xc='PBE', kpts=(8, 8, 8), occupations=FermiDirac(0.1),
                        txt=name + '.txt')

        bulk.set_calculator(calc)

        energy = bulk.get_potential_energy()
        calc.write(name + '.gpw')
        print('Energy:', energy, 'eV')
        if is_lat_const:
            changing_parameter.append(b*2)
        else:
            changing_parameter.append(k)
        energies.append(energy)

    #view(bulk)
    return changing_parameter, energies

def plot_changing_param_vs_energy(start_iteration, end_iteration, increment, is_ec, is_kpts, is_smear, is_lat_const):

    changing_parameter, energies = the_parameter_changer(start_iteration, end_iteration, increment, is_ec, is_kpts, is_smear, is_lat_const)

    if is_kpts:
        changing_parameter = [i**3 for i in changing_parameter]
        x_label = "Number of k-points"
    if is_ec:
        x_label = "E_cutoff"
    if is_smear:
        x_label = "K_BT"
    if is_lat_const:
        x_label = "Lattice constant"

    my_fig = plt.figure(0)

    if not is_lat_const:
        plt.semilogx(changing_parameter, energies)
        plt.semilogx(changing_parameter, energies,'*')
    else:
        plt.plot(changing_parameter, energies)
        plt.plot(changing_parameter, energies,'*')

    plt.xlabel(x_label)
    plt.ylabel('Energy, eV')
    #my_fig.savefig(x_label, bbox_inches='tight')
    plt.show()

#plot_changing_param_vs_energy(350,380,5,False,False,False,True)
#plot_changing_param_vs_energy(2,12,1,False,True,False,False)


plot_changing_param_vs_energy(300,1000,150,True,False,False,False)
