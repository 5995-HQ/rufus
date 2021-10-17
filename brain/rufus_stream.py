import numpy as np
import sounddevice as sd

fs = 48000
data = np.random.uniform(-1, 1, fs)
sd.play(10, 20, fs)
