from ase.build import bulk
from ase.db import connect
from ase.visualize import view
from gpaw import GPAW, PW, FermiDirac
import sys


def save_atoms(my_atoms, E_c, Nbands, Kpts, Fermi_dirac, Lattice_constant, Is_varying):

    db = connect('cu_test.db')
    db.write(my_atoms, energy_cutoff = E_c,
             nbands = Nbands, k_points = Kpts,
             smearing_factor = Fermi_dirac,
             lattice_constant = Lattice_constant,
             is_varying = Is_varying)

if __name__ == "__main__":

    a = 3.62
    e_cut = 340
    nbands = -2
    xc = 'PBE'
    k_pts = 8
    smear = 0.1

    atoms = sys.argv[1]
    atoms = int(atoms)
    bulk_mat = bulk('Cu','fcc',a)*(atoms,atoms,atoms)

    calc = GPAW(mode=PW(e_cut), nbands = nbands,
                xc='PBE', kpts=(k_pts,k_pts,k_pts),
                occupations=FermiDirac(smear), txt='Cu.out')

    bulk_mat.set_calculator(calc)
    bulk_mat.get_potential_energy()
    calc.write('Cu.gpw')
    save_atoms(bulk_mat, e_cut, nbands, k_pts, smear, a, 'energy_cutoff')
