'''
Created on Apr 30, 2012

@author: Sean Ross-Ross, Matt Hall, Evan Bianco
'''
from argparse import ArgumentParser
from modelr.reflectivity import create_wedge
import matplotlib
import matplotlib.pyplot as plt
from modelr.web.urlargparse import rock_properties_type, reflectivity_type
from modelr.rock_properties import MODELS
from modelr.web.util import return_current_figure

short_description = 'Create a simple wedge model.'

def add_arguments(parser):
    
    parser.add_argument('title', default='Plot', type=str, help='The title of the plot')
    parser.add_argument('pad', default=50, type=int, help='The time in milliseconds aboe and below the wedge')
    parser.add_argument('max_thickness', default=50, type=int, help='The maximum thickness of the wedge')
    parser.add_argument('ntraces', default=300, type=int, help='Number of traces')
    
    parser.add_argument('Rpp0', type=rock_properties_type, 
                        help='rock properties of upper rock', required=True)
    parser.add_argument('Rpp1', type=rock_properties_type, 
                        help='rock properties of lower rock', required=True)
    
    parser.add_argument('reflectivity_method', type=reflectivity_type, help='Algorithm for calculating reflectivity', default='zoeppritz', choices=MODELS.keys())    
    parser.add_argument('theta', type=float, help='Angle of incidence', default='0')
    parser.add_argument('f', type=float, help='Frequency of wavelet', default=25)
    parser.add_argument('colour', type=str, help='Matplotlib colourmap', default='Greys')

    return parser

def run_script(args):
    
    matplotlib.interactive(False)
    
    Rprop0 = args.Rpp0 
    Rprop1 = args.Rpp1
    
    warray_amp = create_wedge(args.ntraces, args.pad, args.max_thickness,
                              Rprop0, Rprop1, args.theta, args.f, args.reflectivity_method)
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    aspect = float(warray_amp.shape[1]) / warray_amp.shape[0]
    ax1.imshow( warray_amp, aspect=aspect, cmap=args.colour)
    
    plt.title(args.title % locals())
    plt.ylabel('time (ms)')
    plt.xlabel('trace')
    
    return return_current_figure()
    
    
def main():
    parser = ArgumentParser(usage=short_description, description=__doc__)
    parser.add_argument('time', default=150, type=int, 
                        help='The size in milliseconds of the plot')
    args = parser.parse_args()
    run_script(args)
    
if __name__ == '__main__':
    main()
