# complex_grapher.py

from complex_number import ComplexNumber

class ComplexGraphWindow:
    def __init__( self, r_min, r_max, i_min, i_max ):
        self.r_min = r_min
        self.r_max = r_max
        self.i_min = i_min
        self.i_max = i_max
    
    def ContainsPoint( self, point ):
        if self.r_min <= point.real and point.real <= self.r_max:
            if self.i_min <= point.imag and point.imag <= self.i_max:
                return True
        return False

class ComplexGrapher:
    def __init__( self, window = ComplexGraphWindow( -10.0, 10.0, -10.0, 10.0 ) ):
        self.window = window
        self.max_segment_length = 0.1
        self.line_segment_list = None
        self.r_res = 0.1
        self.i_res = 0.1
    
    def GenerateGraph( self, function ):
        self.line_segment_list = []
        delta = ( self.window.r_max - self.window.r_min ) * self.r_res
        for real in range( self.window.r_min, self.window.r_max, delta ):
            self.GeneratePolyline( function, ComplexNumber( real, self.window.i_min ), ComplexNumber( real, self.window.i_max ) )
        delta = ( self.window.i_max - self.window.i_min ) * self.i_res
        for imag in range( self.window.i_min, self.window.i_max, delta ):
            self.GeneratePolyline( function, ComplexNumber( self.window.r_min, imag ), ComplexNumber( self.window.r_max, imag ) )
    
    def GeneratePolyline( self, function, pointA, pointB ):
        segment_queue = [ ( pointA, pointB ) ]
        while len( segment_queue ) > 0:
            point_pair = segment_queue.pop(0)
            pointA = point_pair[0]
            pointB = point_pair[1]
            if self.DoesLineSegmentImageOverlapWindow( function, pointA, pointB ):
                pointA_image = function( pointA )
                pointB_image = function( pointB )
                if ( pointA_image - pointB_image ).Magnitude() <= self.max_segment_length:
                    self.line_segment_list.append( ( pointA_image, pointB_image ) )
                else:
                    midPoint = pointA + ( pointB - pointA ) * 0.5
                    segment_queue.append( ( pointA, midPoint ) )
                    segment_queue.append( ( midPoint, pointB ) )
    
    def DoesLineSegmentImageOverlapWindow( self, function, pointA, pointB, depth = 1, max_depth = 4 ):
        # Of course, we only answer this question in the approximate.
        midPoint = pointA + ( pointB - pointA ) * 0.5
        midPoint_image = function( midPoint )
        if self.window.ContainsPoint( midPoint_image ):
            return True
        if depth >= max_depth:
            return False
        if self.DoesLineSegmentImageOverlapWindow( function, pointA, midPoint, depth + 1, max_depth ):
            return True
        if self.DoesLineSegmentImageOverlapWindow( function, midPoint, pointB, depth + 1, max_depth ):
            return True
        return False