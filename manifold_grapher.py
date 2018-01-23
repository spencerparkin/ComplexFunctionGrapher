# manifold_grapher.py

from complex_function_grapher import ComplexFunctionGrapher

class LineSegment(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Length(self):
        return abs(self.a - self.b)

    def Lerp(self, t):
        return self.a + t * (self.b - self.a)

class ManifoldGrapher(ComplexFunctionGrapher):
    # Here we graph the given function by manipulating a manifold.
    
    def __init__(self, window_min=None, window_max=None, density=0.5, max_segment_length=2.0):
        super().__init__(window_min, window_max)
        self.density = density
        self.max_segment_length = max_segment_length
        self.segment_list = []
    
    def GraphFunction(self, function, image):
        self.segment_list = []
        # Make a grid or lattice of longitudinal and latitudinal lines.
        queue = []
        for real in range(self.window_min.real, self.window_max.real, self.density):
            for imag in range(self.window_min.imag, self.window_max.image, self.density):
                queue.append(LineSegment(complex(real, imag), complex(real + self.density, imag)))
                queue.append(LineSegment(complex(real, imag), complex(real, imag + self.density)))
        # We are evaluating some points more than once with this, but the code is very simple for now.
        while len(queue) > 0:
            input_segment = queue.pop(0)
            output_segment = LineSegment(function(input_segment.a), function(input_segment.b))
            if output_segment.Length() > self.max_segment_length:
                c = input_segment.Lerp(0.5)
                queue.append(LineSegment(input_segment.a, c))
                queue.append(LineSegment(c, input_segment.b))
            else:
                self.segment_list.append(output_segment)
        # TODO: Use the ImageDraw stuff in the PIL module to draw line segments.