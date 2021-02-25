import pennylane as qml
from pennylane import numpy as np
import strawberryfields as sf
from strawberryfields.ops import *

# main file
def main():







    return 


def circuit():
    num_modes = 2
    prog = sf.Program(num_modes) # number of modes will be dependent on cost and mixer hams

    r_sqz = 1.0 # from the paper
    phi_sqz = 0 # 

    num_blocks = 3

    gamma = np.random.uniform(0.0, np.pi*2, size=(3, 3))
    eta = np.random.uniform(0.0, np.pi*2, size=(3, 3))

    with prog.context as q:
        # Generate two mode squeezed vacuum state as input
        S2gate(r_sqz, phi_sqz)

        # single mode squeezing:
        # Squeezed(r_sqz, phi_sqz) | q[0]
        # Squeezed(r_sqz, phi_sqz) | q[1]

        # 


if __name__ == "__main__":
    main

