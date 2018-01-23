# infinite_series.py

import cmath
import math

class InfiniteSeries(object):
    def __init__(self):
        self.epsilon = 1e-9
        self.limit_count = 10
        self.sum_count = 100
    
    def Term(self, i):
        raise Exception('Pure virtual call.')
    
    def ComputeSum(self):
        # Note that not all sums are Cesaro summable.  In the case that this sum is
        # not Cesaro summable, here we will loop indefinitely.  I'm okay with that,
        # because I am only interested in the sums that are Cesaro summable.
        sequence = []
        sum = 0.0
        for i in range(self.sum_count):
            sum += self.Term(i)
            sequence.append(sum)
        while not self.ConvergentSequence(sequence):
            new_sequence = []
            sum = 0.0
            for i in range(len(sequence)):
                sum += sequence[i]
                average = sum / float(i + 1)
                new_sequence.append(average)
            sequence = new_sequence
        return sequence[len(sequence) - 1]

    def ConvergentSequence(self, sequence):
        # We will approximate the given sequence to be convergent if the
        # the last self.limit_count elements are within self.epsilon.
        # There might be a proof in real analysis of the legitimacy of this
        # approach, or it may as yet still be too naive.
        approx_limit = sequence[len(sequence) - 1]
        for i in range(len(sequence) - self.limit_count, len(sequence)):
            if abs(sequence[i] - approx_limit) >= self.epsilon:
                return False
        return True