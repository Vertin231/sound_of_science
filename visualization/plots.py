import matplotlib.pyplot as plt
from core.fourier import single_sided_spectrum

def plot_signal_and_spectrum(signal, max_frequency=5000):
    fig, (ax_time, ax_freq) = plt.subplots(2, 1, figsize=(9, 6))
    ax_time.plot(signal.time, signal.samples, lw=1.3)
    ax_time.set(xlabel="Time (s)", ylabel="Amplitude", title="Time domain")
    f, a = single_sided_spectrum(signal.samples, signal.sample_rate)
    mask = f <= max_frequency
    ax_freq.plot(f[mask], a[mask], lw=1.2)
    ax_freq.set(xlabel="Frequency (Hz)", ylabel="Amplitude", title="Single-sided amplitude spectrum")
    fig.tight_layout()
    return fig, (ax_time, ax_freq)
