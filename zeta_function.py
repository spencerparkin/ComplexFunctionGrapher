# zeta_function.py

import cmath

from infinite_series import InfiniteSeries

class EtaFunctionSeries(InfiniteSeries):
    def __init__(self, z):
        super().__init__()
        self.z = z

    def Term(self, i):
        numer = 1.0
        if i % 2 == 1:
            numer = -1.0

        #x^y = exp(log(x^y)) = exp(y log(x))

        try:
            denom = complex(real=float(i)) ** self.z
        except ZeroDivisionError:
            denom = 1.0
        except Exception as ex:
            error = str(ex)
            error = None

        result = numer / denom
        return result

def EtaFunction(z):
    return EtaFunctionSeries(z).ComputeSum()

def ZetaFunction(z):
    numer = EtaFunction(z)
    denom = 1.0 - 2.0 / (2.0 ** z)
    result = numer / denom
    return result