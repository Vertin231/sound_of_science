"""Demo 2: periodic sounds, mixtures and noise."""
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as w
from IPython.display import display
from core.signal import Signal
from core.fourier import single_sided_spectrum

def create_demo():
    mode = w.Dropdown(options=["Pure tone", "Two-tone mixture", "White noise", "Harmonic tone"], description="Signal")
    freq = w.IntSlider(value=440, min=100, max=1000, step=10, description="f₀ (Hz)")
    out = w.Output()
    rng = np.random.default_rng(7)
    def update(*_):
        with out:
            out.clear_output(wait=True)
            sr, duration = 8000, .25
            t = np.arange(int(sr*duration))/sr
            if mode.value == "Pure tone": y = np.sin(2*np.pi*freq.value*t)
            elif mode.value == "Two-tone mixture": y = .6*np.sin(2*np.pi*freq.value*t)+.4*np.sin(2*np.pi*1.5*freq.value*t)
            elif mode.value == "White noise": y = rng.normal(0, .35, t.size)
            else: y = sum(np.sin(2*np.pi*n*freq.value*t)/n for n in range(1,9))
            sig = Signal(y, sr, mode.value)
            f, a = single_sided_spectrum(y, sr)
            fig, (ax1, ax2) = plt.subplots(2,1,figsize=(9,5.5))
            ax1.plot(t[:1200], y[:1200], lw=.8); ax1.set(xlabel="Time (s)", ylabel="Amplitude", title="Time domain")
            ax2.plot(f, a, lw=1); ax2.set(xlim=(0, min(2500,sr/2)), xlabel="Frequency (Hz)", ylabel="Amplitude", title="Fourier spectrum")
            for ax in (ax1,ax2): ax.grid(alpha=.2)
            fig.tight_layout(); plt.show(); plt.close(fig)
    mode.observe(update,names="value"); freq.observe(update,names="value")
    display(w.VBox([w.HTML("<h3>2 · Noise & Music</h3><p>Compare temporal structure with frequency content. Noise and music are not defined by a simple periodic/non-periodic split.</p>"),
                    w.HBox([mode,freq]),out]))
    update()
