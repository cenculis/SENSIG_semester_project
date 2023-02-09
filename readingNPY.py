import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

data = np.load("invGoodGlass0.npy")
plt.plot(data, color="blue")
plt.show()