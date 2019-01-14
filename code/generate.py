from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
#import matplotlib
#from matplotlib import pyplot as plt
#%matplotlib inline
import sys 
from madminer.core import MadMiner
from madminer.plotting import plot_2d_morphing_basis
from madminer.delphes import DelphesProcessor
from madminer.sampling import combine_and_shuffle
from madminer.sampling import SampleAugmenter
from madminer.sampling import constant_benchmark_theta, multiple_benchmark_thetas
from madminer.sampling import constant_morphing_theta, multiple_morphing_thetas, random_morphing_thetas
from madminer.ml import MLForge


njobs = int(sys.argv[1])
h5_file = sys.argv[2]

mg_dir = '/home/software/MG5_aMC_v2_6_2'

miner = MadMiner(debug=False)

miner.load(h5_file)

##################################################################################
#signal
miner.run_multiple(
    only_prepare_script=True,
    sample_benchmarks=['sm' for i in range(njobs)],
    mg_directory=mg_dir,
    mg_process_directory='/home/code/mg_processes/signal',
    proc_card_file='/home/code/cards/proc_card_signal.dat',
    param_card_template_file='/home/code/cards/param_card_template.dat',
    run_card_files=['/home/code/cards/run_card_signal.dat'],
    pythia8_card_file='/home/code/cards/pythia8_card.dat',
    log_directory='/home/code/logs/signal')
    #initial_command='source activate python2'

#background
miner.run_multiple(
    is_background=True,
    only_prepare_script=True,
    sample_benchmarks=['sm' for i in range(njobs)],
    mg_directory=mg_dir,
    mg_process_directory='/home/code/mg_processes/background',
    proc_card_file='/home/code/cards/proc_card_background.dat',
    param_card_template_file='/home/code/cards/param_card_template.dat',
    run_card_files=['/home/code/cards/run_card_background.dat'],
    pythia8_card_file='/home/code/cards/pythia8_card.dat',
    log_directory='/home/code/logs/background')