# color_wheel_grapher.py

from complex_function_grapher import ComplexFunctionGrapher

class ColorWheelGrapher(ComplexFunctionGrapher):
    def __init__(self, window_min=None, window_max=None):
        super().__init__(window_min, window_max)
    
    def GraphFunction(self, function, image):
        pass # TODO: Render into PNG image using pillow module.
        # See: https://en.wikipedia.org/wiki/Domain_coloring