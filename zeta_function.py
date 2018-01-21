# zeta_function.py

from infinite_series import InfiniteSeries

class EtaFunctionSeries(InfiniteSeries):
    def __init__(self, z):
        self.z = z

    def Term(self, i):
        sign = 1.0
        if i % 2 == 0:
            sign = -1.0
        return sign / (float(i) ^ self.z)

def EtaFunction(z):
    return EtaFunctionSeries(z).ComputeSum()

def ZetaFunction(z):
    return EtaFunction(z) / (1.0 - 2.0 ^ (1.0 - z))