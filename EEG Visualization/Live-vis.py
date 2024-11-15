import time

import matplotlib.patches as mpatches
import numpy as np
from matplotlib import pyplot as plt
from mne import Annotations, create_info
from mne.io import RawArray
from mne.viz import set_browser_backend

from mne import Epochs, EpochsArray, annotations_from_events, find_events
from mne.io import read_raw_fif

from mne_lsl.stream import EpochsStream, StreamLSL
from mne_lsl.lsl import StreamInfo, StreamInlet, resolve_streams


# same as source_id defined in the PsychoPy script
source_id = 'Cyton_Stream'

streams = resolve_streams()
streams

eeg_stream = StreamLSL(bufsize=5, name=streams[0].name).connect(acquisition_delay=0.001) # if acquisition_delay is 0, must use .acquire() 

# eeg_stream = StreamInlet(streams[0])
# eeg_stream.open_stream()

# Only the initial .time_correction() call takes a few ms to complete so we do it here (future calls are 'instantaneous')
eeg_stream.time_correction()

srate = eeg_stream.info["sfreq"]

eeg_stream.pick('eeg')

eeg_stream.filter(None, 40, picks="grad")  # filter signal

eeg_stream.set_eeg_reference("average")


data = eeg_stream.get_data()

print(data.shape)


##################
# Epoch Streaming
##################

# epochs = EpochsStream(
#     eeg_stream,
#     bufsize=20,  # number of epoch held in the buffer
#     event_id=2,
#     event_channels="STI 014",
#     tmin=-0.2,
#     tmax=0.5,
#     baseline=(None, 0),
#     picks="grad",
# ).connect(acquisition_delay=0.1)
# epochs.info


# for i in range(15):
#     sample, timestamp = eeg_stream.pull_sample(timeout=0)
#     timestamp = timestamp - eeg_stream.time_correction()
    
#     print((sample, timestamp))
#     time.sleep(0.150)


##########################
# Example Visualization
##########################
# picks = ("Fz", "Cz", "Oz")  # channel selection
# f, ax = plt.subplots(3, 1, sharex=True, constrained_layout=True)
# for _ in range(3):  # acquire 3 separate window
#     # figure how many new samples are available, in seconds
#     winsize = stream.n_new_samples / stream.info["sfreq"]
#     # retrieve and plot data
#     data, ts = stream.get_data(winsize, picks=picks)
#     for k, data_channel in enumerate(data):
#         ax[k].plot(ts, data_channel)
#     time.sleep(0.5)
# for k, ch in enumerate(picks):
#     ax[k].set_title(f"EEG {ch}")
# ax[-1].set_xlabel("Timestamp (LSL time)")
# plt.show()