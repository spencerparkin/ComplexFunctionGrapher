# infinite_series.py

class InfiniteSeries(object):
    def __init__(self):
        self.epsilon = 1e-3
        self.limit_count = 5
        self.sum_count = 20000
        self.max_cesaro = 10
    
    def Term(self, i):
        # Terms will be 1-based (e.g., a_1, a_2, a_3, etc.)
        raise Exception('Pure virtual call.')
    
    def ComputeSum(self):
        # Note that not all sums are Cesaro summable.
        sequence = []
        sum = 0.0
        for i in range(1, self.sum_count + 1):
            sum += self.Term(i)
            sequence.append(sum)
        j = 0
        while not self.ConvergentSequence(sequence):
            j += 1
            if j > self.max_cesaro:
                raise Exception('Max cesaro (%d) reached.' % self.max_cesaro)
            new_sequence = []
            sum = 0.0
            for i in range(len(sequence)):
                sum += sequence[i]
                average = sum / float(i + 1)
                new_sequence.append(average)
            sequence = new_sequence
        return sequence[-1]

    def ConvergentSequence(self, sequence):
        # We will approximate the given sequence to be convergent if the
        # the last self.limit_count elements are within self.epsilon.
        # There might be a proof in real analysis of the legitimacy of this
        # approach, or it may as yet still be too naive.
        approx_limit = sequence[-1]
        for i in range(len(sequence) - self.limit_count, len(sequence)):
            if abs(sequence[i] - approx_limit) >= self.epsilon:
                return False
        return True