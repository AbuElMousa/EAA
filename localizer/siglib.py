import random
import numpy as np
from scipy.spatial import distance


DEFAULT_MIC_POSITIONS = [[1, 1], [1, -1], [-1, 1], [-1, -1]]


def get_signals(mic_positions = DEFAULT_MIC_POSITIONS, source_position=[6, 10], frequencies=[440], samples=1024, c=330, start=0, end=1, noise=10):
    """
    """
    num_mics = len(mic_positions)
    signals = []#np.empty((num_mics, samples)) 
    decays = generate_decay(mic_positions, source_position)
    delays = generate_delay(mic_positions, source_position, c)
    phase = 0
    for i in range(num_mics):
        signal = np.zeros(samples)
        noise = generate_noise(samples)
        delay = delays[i]
        for freq in frequencies:
            signal += sine(freq, phase, samples, start, end, noise)
            noise = noise + generate_noise(samples)
            signal = decays[i] * signal
        signals.append(signal)
    return signals


def sine(frequency, phase, samples, start, end, noise):
    time = np.linspace(start, end, samples)
    signal = np.sin(2 * np.pi * frequency * time + phase)
    noise = generate_noise(samples)
    return signal + noise
    

def calculate_mic_source_radii(mic_positions, source_position):
    """Calculates the radius between each pair of microphones
    """
    radii = []
    for current_mic_position in mic_positions:
        radius = distance.euclidean(source_position, current_mic_position)
        radii.append(radius)
    return radii


def generate_noise(samples):
    """
    """
    noise_level = 1
    return noise_level * 0.0008 * np.asarray(random.sample(range(0, samples), samples))


def generate_decay(mic_positions, source_position):
    """
    """
    radii = calculate_mic_source_radii(mic_positions, source_position)
    min_radius = min(radii)
    pressure_deviations = np.divide(min_radius, radii)
    pressure_deviations = np.multiply(pressure_deviations, pressure_deviations)
    return pressure_deviations


def generate_delay(mic_positions, source_position, c):
    """Calculates the delay time between each microphone
    """
    radii = calculate_mic_source_radii(mic_positions, source_position)
    min_radius = min(radii)
    r_adj = np.subtract(radii, min_radius)
    time_deltas = np.divide(r_adj, c) 
    return time_deltas
