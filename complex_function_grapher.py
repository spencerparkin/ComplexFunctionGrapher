# complex_function_grapher.py

class ComplexFunctionGrapher(object):
    # Derivatives of this class can graph complex-valued functions
    # of a complex variable in a variety of ways.
    
    def __init__(self, window_min=None, window_max=None):
        self.window_min = complex(real=-10.0, imag=-10.0) if window_min is None else window_min
        self.window_max = complex(real=10.0, image=10.0) if window_max is None else window_max
    
    def GraphFunction(self, function, image):
        pass
        # TODO: Here we could draw the real and imaginary axes with text on tick marks.