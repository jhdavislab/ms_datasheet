###################################
#Tool to plot thermo raw files
#to QC proteomics injections
#Joey Davis
#jhdavislab.com
#jhdavis@mit.edu
###################################
from matplotlib import cm
from gooey import GooeyParser
from gooey import Gooey
from ms_datasheet import plot_datapage

__VERSION__="0.1.1"

@Gooey(default_size=(600, 650), program_name='Davis Lab mass spec datasheet')
def main():
    parser = GooeyParser(description='Plot a single datasheet for a given therom RAW file.\nRequires "pyextractMS", "MSFileReader", numpy, matplotlib, gooey')
    parser.add_argument('file', type=str,
                       help='path to the file to analyze', widget='FileChooser')
    parser.add_argument('--display', default=True, action='store_false',
                        help='just display the plot, but do not save it')
    parser.add_argument('--extension', default='.pdf', type=str,
                        help='string for figure filetype (e.g. .pdf, .png)')
    parser.add_argument('--spectra_rt_range', default='1,120', type=str,
                       help='RT range over which to calculate spectra histograms; format is start,end. e.g. --spectra_rt_range 1,120')
    parser.add_argument('--tic_rt_range', default='1,120', type=str,
                       help='RT range over which to plot tics; format is start,end. e.g. --tic_rt_range 1,120')
    parser.add_argument('--include_irts', default=False, action='store_true',
                       help='include XICs, MS1, MS2 spectra for standard iRT peptides at expected retention times. Default is to exclude this information.\
do not sure this option unless you have included pierce iRT peptides in your sample')
    args = parser.parse_args()

    file_name= vars(args)['file']
    savefig= vars(args)['display']
    fig_extension = vars(args)['extension']
    spectra_rt_range = vars(args)['spectra_rt_range']
    tic_rt_range = vars(args)['tic_rt_range']
    include_iRTs = vars(args)['include_irts']
    
    print('****generating datasheet for file: ' +file_name+'....****\n')
    print('****to do the same from the commandline, run the following:')
    command = 'python ms_datasheet.py '+file_name+' --spectra_rt_range ' + spectra_rt_range + ' --tic_rt_range ' + tic_rt_range + ' --extension ' + fig_extension
    if not savefig:
        command+=' --display'
    if include_iRTs:
        command+=' --include_irts'
    print(command)
    plot_datapage(file_name, savefig=savefig, fig_extension=fig_extension, colors=cm.get_cmap(name='plasma'),
                  spectra_rt_range=spectra_rt_range, tic_rt_range=tic_rt_range, include_iRTs=include_iRTs)
    print('****plotting complete')
if __name__ =='__main__':
    main()
    