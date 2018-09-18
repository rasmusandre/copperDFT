"""Bulk Cu(fcc) test"""
from __future__ import print_function
from ase import Atoms, Atom
from ase.build import bulk
from ase.visualize import view
from gpaw import GPAW, PW, FermiDirac
from ase_db import save_atoms, print_energies
import matplotlib.pyplot as plt
import numpy as np

def create_calculator(ec, nb, x_c, k_pts, FD, name):
    calc = GPAW(mode=PW(ec), nbands = nb, xc=x_c, kpts=(k_pts, k_pts, k_pts), occupations=FermiDirac(FD), txt=name + '.txt')
    return calc

def run_parameter_iterator():

    start_iteration = 3.2
    end_iteration = 4.01
    increment = 0.1

    st_lattice_cnst = 3.62
    st_ec = 340
    st_nb = -2
    st_xc = 'PBE'
    st_kpts = 8
    st_FD = 0.1
    is_varying = 'lattice_constant'

    changing_parameter, energies =  parameter_iterator(start_iteration, end_iteration, increment, st_lattice_cnst, st_ec, st_nb, st_xc, st_kpts, st_FD, is_varying)

    print_energies(is_varying)

def parameter_iterator(start_iteration, end_iteration, increment, st_lattice_cnst, st_ec, st_nb, st_xc, st_kpts, st_FD, is_varying):

    changing_parameter = []
    energies = []
    name = 'Cu-fcc'
    k = start_iteration

    while k <= end_iteration:

        b = st_lattice_cnst/2

        if is_varying == 'lattice_constant':
            b = k/2 #DIVIDE BY TO FOR FCC!?


        #bulk = Atoms('Cu',cell=[[0, b, b],[b, 0, b],[b, b, 0]], pbc=True)
        bulk_mat = bulk('Cu', 'bcc', b*2)

        if is_varying == 'energy_cutoff':
            calc = create_calculator(k, st_nb, st_xc, st_kpts, st_FD, name)
        if is_varying == 'k_points':
            calc = create_calculator(st_ec, st_nb, st_xc, k, st_FD, name)
        if is_varying == 'smearing_factor':
            calc = create_calculator(st_ec, st_nb, st_xc, st_kpts, k, name)
        if is_varying == 'lattice_constant':
            calc = create_calculator(st_ec, st_nb, st_xc, st_kpts, st_FD, name)

        bulk_mat.set_calculator(calc)
        energy = bulk_mat.get_potential_energy()
        calc.write(name + '.gpw')

        if is_varying == 'energy_cutoff':
            save_atoms(bulk_mat, k, st_nb, st_kpts, st_FD, st_lattice_cnst, is_varying)
        if is_varying == 'k_points':
            save_atoms(bulk_mat, st_ec, st_nb, k, st_FD, st_lattice_cnst, is_varying)
        if is_varying == 'smearing_factor':
            save_atoms(bulk_mat, st_ec, st_nb, st_kpts, k, st_lattice_cnst, is_varying)
        if is_varying == 'lattice_constant':
            save_atoms(bulk_mat, k, st_nb, st_kpts, st_FD, b*2, is_varying)

        print('Energy:', energy, 'eV')
        if is_varying == 'lattice_constant':
            changing_parameter.append(b*2)
        else:
            changing_parameter.append(k)
        energies.append(energy)

        k += increment

    return changing_parameter, energies

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
#plot_changing_param_vs_energy(1,100,15,False,False,True)

run_parameter_iterator()
