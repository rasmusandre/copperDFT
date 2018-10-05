from ase.db import connect
from ase import Atoms
from ase.build import bulk
from ase.visualize import view
import matplotlib.pyplot as plt


def save_atoms(my_atoms, E_c, Nbands, Kpts, Fermi_dirac, Lattice_constant, Is_varying):

    db = connect('single_cu_xc_LDA2.db')
    db.write(my_atoms, energy_cutoff = E_c, nbands = Nbands, k_points = Kpts, smearing_factor = Fermi_dirac, lattice_constant = Lattice_constant, is_varying = Is_varying)

def print_energies(Is_varying):

    db = connect('single_cu.db')
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
    plt.ylabel('Potential Energy, eV')
    plt.xlabel(Is_varying)
    #plt.show()
    return energies, changing_parameter


def show_min_lc():
    en_lda, cp_lda = plot_from_db('lattice_constant', 'single_cu_xc_LDA2.db')
    en_pbe, cp_pbe = plot_from_db('lattice_constant', 'single_cu_xc_PBE.db')
    print(cp_lda[en_lda.index(min(en_lda))])
    print(cp_pbe[en_pbe.index(min(en_pbe))])


#db_deleter()
#plot_from_db('energy_cutoff', 'single_cu.db')
#plt.show()
#plot_from_db('lattice_constant', 'single_cu_xc_PBE.db')
#plt.show()
#plt.show()
#bulk = bulk('Cu', 'fcc', a=3.6)*(4,4,4)
#view(bulk)
