from ase.db import connect
from ase import Atoms
from ase.build import bulk
from ase.visualize import view
import matplotlib.pyplot as plt
import numpy as np


def save_atoms(my_atoms, E_c, Nbands, Kpts, Fermi_dirac, Lattice_constant, Is_varying):

    db = connect('single_cu_xc_PBE2.db')
    db.write(my_atoms, energy_cutoff = E_c, nbands = Nbands, k_points = Kpts, smearing_factor = Fermi_dirac, lattice_constant = Lattice_constant, is_varying = Is_varying)

def print_energies(Is_varying):

    db = connect('single_cu_xc_PBE.db')
    print('The changing parameter is ' + Is_varying)
    for obj in db.select(is_varying = Is_varying):

        print(Is_varying + ' is ' + str(obj[Is_varying]))

        print('The energy is ' + str(obj['energy']))




def db_deleter():

    param = 'lattice_constant'
    db = connect('single_cu_bcc.db')
    for obj in db.select(is_varying = param):

        del db[obj.id]

def plot_from_db(Is_varying, database_name):

    db = connect(database_name)
    energies = []
    changing_parameter = []
    for obj in db.select(is_varying = Is_varying):

        energies.append(obj['energy'])
        changing_parameter.append(obj[Is_varying])

    plt.figure(0)
    if Is_varying == 'lattice_constant':
        plt.plot(changing_parameter, energies)
        plt.plot(changing_parameter, energies, '*')
    else:
        plt.semilogx(changing_parameter, energies)
        plt.semilogx(changing_parameter, energies, '*')
    plt.ylabel('Potential energy [eV/atom]')
    plt.xlabel('Lattice constant [Å]')
    #plt.show()
    return energies, changing_parameter

def plot_from_db_two_db(Is_varying, database_name1, database_name2):

    db1 = connect(database_name1)
    db2 = connect(database_name2)
    energies1 = []
    energies2 = []
    changing_parameter1 = []
    changing_parameter2 = []
    amt1 = db1.get_atoms(id = 1)
    amt2 = db2.get_atoms(id = 1)

    for obj in db1.select(is_varying = Is_varying):

        energies1.append(obj['energy']/amt1.get_number_of_atoms())
        changing_parameter1.append((obj[Is_varying])**3)

    plt.figure(0)


    plt.semilogx(changing_parameter1, energies1,'b')
    plt.semilogx(changing_parameter1, energies1, 'bo',label='_nolegend_')

    for obj in db2.select(is_varying = Is_varying):

        energies2.append(obj['energy']/amt2.get_number_of_atoms())

        changing_parameter2.append((obj[Is_varying])**3)



    plt.semilogx(changing_parameter2, energies2,'r')
    plt.semilogx(changing_parameter2, energies2, 'ro',label='_nolegend_')

    plt.ylabel('Potential energy [eV/atom]')
    plt.xlabel('number of k-points')
    plt.legend(['1 atom', '64 atoms'],fancybox=True, framealpha=1,shadow=True,prop={'size': 10})
    plt.grid(True)
    #plt.show()
    #return energies, changing_parameter


def show_min_lc():
    en_lda, cp_lda = plot_from_db('lattice_constant', 'single_cu_xc_LDA2.db')
    en_pbe, cp_pbe = plot_from_db('lattice_constant', 'single_cu_xc_PBE.db')
    print(cp_lda[en_lda.index(min(en_lda))])
    print(cp_pbe[en_pbe.index(min(en_pbe))])

#plot_from_db_two_db('k_points','single_cu.db','cu_kpts.db')
#plot_from_db('k_points', 'cu_kpts.db')
#plt.savefig('my_fig.png')
#plot_from_db('lattice_constant', 'single_cu_xc_LDA2.db')
#plt.show()

#bulk_mat = bulk('Cu','fcc',3.62)*(4,4,4)


#del bulk_mat[[atom.index for atom in bulk_mat if atom.index != 45]]
#view(bulk_mat)






#
