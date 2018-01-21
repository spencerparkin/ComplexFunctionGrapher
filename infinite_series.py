# infinite_series.py

import cmath
import math

# TODO: Test our algorithm here with {1, -1, 1, -1, 1, -1, 1, -1, ...}.  Should get 1/2, approximately.

class InfiniteSeries(object):
    def __init__(self):
        self.partial_sums = []

    def Term(self, i):
        return 0.0

    def PartialSum(self, i):
        if i >= len(self.partial_sums):
            j = len(self.partial_sums) - 1
            while j < i:
                self.partial_sums.append(self.partial_sum[j] + self.Term(j + 1))
                j += 1
        return self.partial_sums[i]

    def ComputeSum(self, epsilon=1e-9, term_count=100, max_depth=10, depth=1):
        # There is no proof of convergence here.  This is very approximate.
        # Much of this is quite naive, I'm sure.
        i = 1
        for k in range(term_count):
            j = i + 1
            a = self.PartialSum(i)
            b = self.PartialSum(j)
            if math.fabs(a - b) < epsilon:
                return b
            i = j
        if depth < max_depth:
            cesaro_series = CesaroSeries(self)
            return cesaro_series.ComputeSum(epsilon, term_count, max_depth, depth + 1)
        return None

class CesaroSeries(InfiniteSeries):
    def __init__(self, series):
        super().__init__()
        self.series = series

    def Term(self, i):
        return self.series.PartialSum(i) / float(i)