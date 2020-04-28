This project attempts to address whether the neural code in the auditory thalamus in songbirds can be interpreted in terms of a hierarchical model of sensory processing. The neural recording data is shown by accessing the "all_stims" directory, which can be interpreted in python through the os.chdir() method. The project will answer which class of stimuli (songrip, conspecific, flatrip) produces the most amount of spikes. The id input/UoI is the the name of the bird sample used and the stimulus presented for that trial. The subsequent return will be the number of spikes that occurred in response to the stimulus.

The data can be retrieved by downloading the files "cell_regions.csv" and "all_cells" from the aa2 dataset. (https://crcns.org/data-sets/aa/aa-2/about)

"Cell_regions.csv" will allow us to find which birds were tested in respsect to OV (as opposed to other brain regions involved in the experiment). This can be used to make a list to isolate all birds tested in the specific region to be analyzed (in this case, the OV region) and integrate those specific birds when running the analysis.

The "all_cells" file gives us access to the main data that records the spike times per song type for every bird tested, in accordance with the song type.

In each stimulus class subdirectory, there is a file "Spike files" that are prefixed with "spike" and contains a list of spike times for each stimulus presentation. These spike times are the ones accounted for when calculating average spike times.

Each cell is presented with stimuli from 2-3 classes:

1) flatrip: modulation-limited noise with a (somewhat) flat modulation spectrum (ML-Noise)
2) songrip: ripple stimuli with the same modulation spectrum as song (not included for OV birds)
3) conspecific: natural birdsong from zebra finch

Important Notes:
*In order to run this project, insert an individualized directory for "addr" to allow code to access individual computers after downloading aa2 dataset directories and files.

*Conspecific sounds were tested by offering 20 stimuli, while flatrip sounds were tested with only 10 stimuli.

*Bird sample “pupi0414_2” did not have data for flatrip stimulation trials and was excluded in making the list for OV birds tested for flatrip songs
    - as a result, there are 57 averages instead of 58
    - "None" was used to replace "pupi0414_2" when graphing the flatrip song results in order to show a gap to indicate the absence of data for bird subject "pupi0414_2" (and also line up the results when comparing with conspecific song results)

 Files not used for this project include: "all_stims", "cell_stim_classes.csv", "stim_data.csv"

 All data attributed to:
 Sarah M.N. Woolley sw2277@columbia.edu and Thane Fremouw Thane_Fremouw@umit.maine.edu
