# complex_function.py

class ComplexFunction:
    # Specifically, here we're talking about a complex valued function of a complex variable.
    def __init__( self ):
        pass

    def __call__( self, input ):
        return self.Evaluate( input )
    
    def Evaluate( self, input ):
        output = input
        return output
    
class ReimannZetaFunction( ComplexFunction ):
    # Can we give here the analytical continuation of the function?
    # I have no idea how to do that, but we can give part of the function.
    def __init__( self ):
        super().__init__()
    
    def Evaluate( self, input ):
        pass