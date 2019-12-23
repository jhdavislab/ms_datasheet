###################################
#Tool to plot thermo raw files
#to QC proteomics injections
#Joey Davis
#jhdavislab.com
#jhdavis@mit.edu
###################################
import ms_datasheet
import glob
from matplotlib import cm
from gooey import GooeyParser
from gooey import Gooey

__VERSION__="0.1.0"

@Gooey(default_size=(610, 610))
def main():
    parser = GooeyParser(description='Plot a single datasheet for a each raw file in a given directory. Requires "ms_datasheet", "pyextractMS", "MSFileReader", numpy, matplotlib')
    parser.add_argument('directory', type=str,
                       help='path to the directory to analyze', widget='DirChooser')
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

    all_files = glob.glob(directory+'/*.raw')
    
    print('****to do the same from the commandline, run the following:')
    command = 'python ms_datasheet_multi.py '+directory+'/ --spectra_rt_range ' + spectra_rt_range + ' --tic_rt_range ' + tic_rt_range + ' --extension ' + fig_extension
    if not savefig:
        command+=' --display'
    print(command)
    
    print('/n*****analyzing the following files:')
    print(all_files)
    for file_name in all_files:
        print('****analyzing: '+file_name+'...')
        ms_datasheet.plot_datapage(file_name, savefig=savefig, fig_extension=fig_extension, colors=cm.get_cmap(name='plasma'),
                      spectra_rt_range=spectra_rt_range, tic_rt_range=tic_rt_range)
        print('****completed: '+file_name)

if __name__ =='__main__':
    main()