"""Bulk Cu(fcc) test"""
from __future__ import print_function
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW, FermiDirac
import matplotlib.pyplot as plt

def the_parameter_changer(start_iteration, end_iteration, increment, is_ec, is_kpts, is_smear):

    #example 2, 10, 1, False, True, False

    changing_parameter = []
    energies = []

    for k in range(start_iteration, end_iteration, increment):

        name = 'Cu-fcc'
        a = 3.62  # fcc lattice parameter Cu [Å]
        b = a / 2

        bulk = Atoms('Cu',cell=[[0, b, b],[b, 0, b],[b, b, 0]], pbc=True)

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

        bulk.set_calculator(calc)

        energy = bulk.get_potential_energy()
        calc.write(name + '.gpw')
        print('Energy:', energy, 'eV')
        changing_parameter.append(k)
        energies.append(energy)
    view(bulk)
    return changing_parameter, energies

def plot_changing_param_vs_energy(start_iteration, end_iteration, increment, is_ec, is_kpts, is_smear):

    changing_parameter, energies = the_parameter_changer(start_iteration, end_iteration, increment, is_ec, is_kpts, is_smear)

    if is_kpts:
        changing_parameter = [i**3 for i in changing_parameter]
        x_label = "Number of k-points"
    if is_ec:
        x_label = "E_cutoff"
    if is_smear:
        x_label = "K_BT"


    my_fig = plt.figure(0)
    plt.semilogx(changing_parameter, energies)
    plt.semilogx(changing_parameter, energies,'*')
    plt.xlabel(x_label)
    plt.ylabel('Energy, eV')
    my_fig.savefig(x_label, bbox_inches='tight')
    #plt.show()

plot_changing_param_vs_energy(200,1200,100,True,False,False)
#plot_changing_param_vs_energy(2,12,1,False,True,False)
#plot_changing_param_vs_energy(1,100,15,False,False,True)
