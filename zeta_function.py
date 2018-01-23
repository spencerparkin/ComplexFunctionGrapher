# zeta_function.py

import cmath

from infinite_series import InfiniteSeries

class EtaFunctionSeries(InfiniteSeries):
    def __init__(self, z):
        self.z = z

    def Term(self, i):
        numer = 1.0
        if i % 2 == 0:
            numer = -1.0
        denom = complex(real=float(i)) ** self.z
        result = numer / denom
        return result

def EtaFunction(z):
    return EtaFunctionSeries(z).ComputeSum()

def ZetaFunction(z):
    return EtaFunction(z) / (1.0 - 2.0 ** (1.0 - z))