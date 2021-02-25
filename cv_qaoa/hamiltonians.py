# construct mixer and cost hamiltonians here:
import pennylane as qml
from pennylane import numpy as np
import strawberryfields as sf
from strawberryfields.ops import *

def H_cost1(q, params):
    pass

def H_number_mixer(q, params):

    pass

def H_kinetic_mixer(q, param):
    # Fdagger p^2 F
    Rgate(-np.pi/2) | q[0] # Fourier gate is just special case of Rotation, this is inverse
    Rgate(-np.pi/2) | q[1]
    Pgate(param) | q[0] # docs on this give me an error, but its the quadratic phase gate
    Pgate(param) | q[1]
    Fouriergate() | q[0]
    Fouriergate() | q[1]
    pass