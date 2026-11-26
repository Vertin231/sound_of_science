"""Fourier-domain helpers."""
import numpy as np

def single_sided_spectrum(samples, sample_rate, window=True):
    x = np.asarray(samples, dtype=float)
    if x.ndim != 1 or x.size < 2:
        raise ValueError("Provide at least two one-dimensional samples.")
    x = x - np.mean(x)
    if window:
        x = x * np.hanning(x.size)
        scale = np.sum(np.hanning(x.size)) / 2
    else:
        scale = x.size / 2
    spectrum = np.fft.rfft(x)
    frequencies = np.fft.rfftfreq(x.size, 1 / sample_rate)
    amplitude = np.abs(spectrum) / max(scale, np.finfo(float).eps)
    if amplitude.size > 2:
        amplitude[1:-1] *= 2
    return frequencies, amplitude
