from ase.build import bulk
from gpaw import GPAW, PW, FermiDirac
import matplotlib.pyplot as plt
import numpy as np


my_sum = {}

for i in range(0,200):
    my_sum[str(i/10)] = 0
print(my_sum)
