
import numpy as np

short_description = "Build a 3 layer slab model"
def add_arguments(parser):


    parser.add_argument('interface_depth', default=100,
                        type=int, help="The time in ms above and below the wedge")
    parser.add_argument('x_samples', default=300, type=int,
                        help="Number of samples (traces) in the x-direction")
    parser.add_argument("margin", default=15, type=int,
                        help="Zero thickness x location")
    parser.add_argument("left", default='40,40', type=int,
                         action='list',
                         help="Thickness on the left-hand side")
    parser.add_argument("right", default='30,130', type=int,
                        action='list',
                        help="Thickness on the right-hand side")
    parser.add_argument("layers", default=3, type=int,
                        help="The number of layers in the model")

    

def run_script(args):
    from modelr.modelbuilder import body_svg, svg2png
    
    l1 = (150,110,110)
    l2 = (110,150,110)
    l3 = (110,110,150)
    
    layers = [l1,l2]
    
    if args.layers == 3:
        layers.append(l3)
        
    body = body_svg(args.interface_depth, args.margin,
                    args.left, args.right, args.x_samples,
                    layers)

    tmpfile = svg2png(body, layers)
    with open(tmpfile.name, 'rb') as f:
        data = f.read()
    

    return data



                        
                        
