# complex_number.py

import math

class ComplexNumber:
    def __init__( self, real = 0.0, imag = 0.0 ):
        self.real = real
        self.imag = imag
    
    def __add__( self, other ):
        return ComplexNumber( self.real + other.real, self.imag + other.imag )
    
    def __sub__( self, other ):
        return ComplexNumber( self.real - other.real, self.imag - other.imag )
    
    def __mul__( self, other ):
        if type( other ) == float or type( other ) == int:
            return ComplexNumber( self.real * float( other ), self.imag * float( other ) )
        else:
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber( real, imag )
    
    def Conjugate( self ):
        return ComplexNumber( self.real, -self.imag )
    
    def SquareMagnitude( self ):
        return self.real * self.real + self.imag * self.imag
    
    def Magnitude( self ):
        return math.sqrt( self.SquareMagnitude() )
    
    def Inverse( self ):
        return self.Conjugate() * ( 1.0 / self.SquareMagnitude() )