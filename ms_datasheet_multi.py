import ms_datasheet
import glob
from matplotlib import cm
import argparse


if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Plot a single datasheet for a each raw file in a given directory. Requires "ms_datasheet", "pyextractMS", "MSFileReader", numpy, matplotlib')
    parser.add_argument('directory', type=str,
                       help='path to the directory to analyze')
    parser.add_argument('--display', default=True, action='store_false',
                        help='just display the plots, but do not save them')
    parser.add_argument('--extension', default='.pdf', type=str,
                        help='string for figure filetype (e.g. .pdf, .png)')
    parser.add_argument('--spectra_rt_range', default='1,120', type=str,
                       help='RT range over which to calculate spectra histograms; format is start,end. e.g. --spectra_rt_range 1,120')
    parser.add_argument('--tic_rt_range', default='1,120', type=str,
                       help='RT range over which to plot tics; format is start,end. e.g. --tic_rt_range 1,120')
    args = parser.parse_args()

    directory= vars(args)['directory']
    savefig= vars(args)['display']
    fig_extension = vars(args)['extension']
    spectra_rt_range = vars(args)['spectra_rt_range']
    tic_rt_range = vars(args)['tic_rt_range']

    all_files = glob.glob(directory+'*.raw')
    print('analyzing the following files:')
    print(all_files)
    for file_name in all_files:
        print('analyzing: '+file_name+'...')
        ms_datasheet.plot_datapage(file_name, savefig=savefig, fig_extension=fig_extension, colors=cm.get_cmap(name='plasma'))
        print('completed: '+file_name)