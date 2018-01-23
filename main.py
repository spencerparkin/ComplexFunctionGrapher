# main.py

import types
import argparse
from PIL import Image

if __name__ == '__main__':
    
    arg_parser = argparse.ArgumentParser(description='Graph complex-valued functions of a complex variable.')
    arg_parser.add_argument('--r_min', help='', type=str)
    arg_parser.add_argument('--r_max', help='', type=str)
    arg_parser.add_argument('--i_min', help='', type=str)
    arg_parser.add_argument('--i_max', help='', type=str)
    arg_parser.add_argument('--density', help='', type=str)
    arg_parser.add_argument('--max_seg_len', help='', type=str)
    arg_parser.add_argument('--function_file', help='', type=str)
    arg_parser.add_argument('--function_code', help='', type=str)
    arg_parser.add_argument('--function_name', help='', type=str)
    arg_parser.add_argument('type', help='', type=str)
    arg_parser.add_argument('image_file', help='', type=str)
    arg_parser.add_argument('width', help='', type=str)
    arg_parser.add_argument('height', help='', type=str)
    
    args = arg_parser.parse_args()
    
    window_min = complex(real=float(args.r_min if args.r_min else -10.0), imag=float(args.i_min if args.i_min else -10.0))
    window_max = complex(real=float(args.r_max if args.r_max else 10.0), imag=float(args.r_max if args.r_max else 10.0))
    
    print('Graphed region of the complex plane...')
    print('r-min: %f' % window_min.real)
    print('r-max: %f' % window_max.real)
    print('i-min: %f' % window_min.imag)
    print('i-max: %f' % window_max.imag)
    
    grapher = None
    if args.type == 'color_wheel':
        from color_wheel_grapher import ColorWheelGrapher
        grapher = ColorWheelGrapher(window_min, window_max)
        print('Color-wheel grapher created.')
    elif args.type == 'manifold':
        density = float(args.density) if args.density else 0.5
        max_segment_length = float(args.max_seg_len) if args.max_seg_len else 2.0
        from manifold_grapher import ManifoldGrapher
        grapher = ManifoldGrapher(window_min, window_max, density, max_segment_length)
        print('Manifold grapher created.')
    
    size = (int(args.width), int(args.height))
    mode = 'RGB'
    image = Image.new(mode, size)
    print('Image size: %d x %d' % size)
    
    print('Compiling function code...')
    function_code = None
    function_file = ''
    if args.function_file:
        function_file = args.function_file
        with open(function_file, 'r') as file:
            function_code = file.read()
    elif args.function_code:
        function_code = args.function_code
    compiled_code = compile(function_code, function_file, 'exec')
    module = types.ModuleType('script_module')
    exec(compiled_code, module.__dict__)
    function_name = args.function_name if args.function_name else 'complex_function'
    function = getattr(module, function_name)
    
    print('Graphing...')
    grapher.GraphFunction(function, image)
    
    print('Saving image...')
    print('File: ' + args.image_file)
    image.save(args.image_file)
    
    print('Process complete!')