"""Demo 1: waveform and timbre."""
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as w
from IPython.display import display
from core.signal import make_waveform, harmonic_signal

def create_demo():
    kind = w.Dropdown(options=["sine", "square", "sawtooth", "triangle"], value="sine", description="Wave")
    freq = w.FloatSlider(value=220, min=55, max=880, step=5, description="f₀ (Hz)")
    count = w.IntSlider(value=12, min=1, max=40, description="Harmonics")
    out = w.Output()
    def update(*_):
        with out:
            out.clear_output(wait=True)
            sig = make_waveform(kind.value, freq.value, 0.025, 44100, count.value)
            t = sig.time
            fig, ax = plt.subplots(figsize=(9, 3.4))
            ax.plot(t, sig.samples, lw=1.4)
            ax.set(title=f"{kind.value.title()} wave · fundamental {freq.value:.0f} Hz",
                   xlabel="Time (s)", ylabel="Amplitude")
            ax.grid(alpha=.2); fig.tight_layout(); plt.show()
            plt.close(fig)
            amps = {"sine":[1.0], "square":[1/n if n%2 else 0 for n in range(1,count.value+1)],
                    "sawtooth":[(-1)**(n+1)/n for n in range(1,count.value+1)],
                    "triangle":[(-1)**((n-1)//2)/(n*n) if n%2 else 0 for n in range(1,count.value+1)]}[kind.value]
            fig, ax = plt.subplots(figsize=(9, 2.4))
            ax.stem(np.arange(1,len(amps)+1), np.abs(amps), basefmt=" ")
            ax.set(title="Harmonic amplitudes", xlabel="Harmonic number n", ylabel="|Aₙ|")
            ax.grid(alpha=.2); fig.tight_layout(); plt.show(); plt.close(fig)
    for control in (kind, freq, count): control.observe(update, names="value")
    display(w.VBox([w.HTML("<h3>1 · Waveform & Timbre</h3><p>Change the waveform and harmonic content. The spectrum of a waveform shapes its timbre.</p>"),
                    w.HBox([kind, freq]), count, out]))
    update()
