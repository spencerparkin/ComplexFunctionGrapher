# Test.py

from infinite_series import InfiniteSeries
from zeta_function import ZetaFunction

class SimpleSeries(InfiniteSeries):
    def __init__(self):
        super().__init__()
    
    def Term(self, i):
        if i % 2 == 0:
            return 1.0
        else:
            return -1.0

if __name__ == '__main__':
    series = SimpleSeries()
    sum = series.ComputeSum()
    print('Sum = %f' % sum)