"""Demo 3: intervals, chord superposition and beating."""
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as w
from IPython.display import display

INTERVALS = {"Unison":0, "Minor third":3, "Major third":4, "Perfect fourth":5,
             "Perfect fifth":7, "Octave":12}

def create_demo():
    root = w.IntSlider(value=220,min=110,max=440,step=5,description="Root (Hz)")
    interval = w.Dropdown(options=list(INTERVALS),value="Perfect fifth",description="Interval")
    chord = w.Dropdown(options=["Two notes","Major triad (4:5:6)","Minor triad (10:12:15)"],description="Chord")
    out = w.Output()
    def update(*_):
        with out:
            out.clear_output(wait=True)
            f0 = root.value
            if chord.value == "Major triad (4:5:6)": freqs=[f0, f0*5/4, f0*3/2]
            elif chord.value == "Minor triad (10:12:15)": freqs=[f0, f0*6/5, f0*3/2]
            else: freqs=[f0, f0*2**(INTERVALS[interval.value]/12)]
            sr=12000; t=np.arange(int(.06*sr))/sr
            waves=[np.sin(2*np.pi*f*t) for f in freqs]
            total=np.sum(waves,axis=0)/len(waves)
            fig,(a,b)=plt.subplots(2,1,figsize=(9,5.5))
            for i,y in enumerate(waves): a.plot(t,y+i*1.3,label=f"{freqs[i]:.1f} Hz")
            b.plot(t,total,color="black")
            a.set(title="Individual tones (vertically offset)",xlabel="Time (s)",ylabel="Amplitude"); a.legend()
            b.set(title="Superposition",xlabel="Time (s)",ylabel="Amplitude")
            for ax in (a,b): ax.grid(alpha=.2)
            fig.tight_layout();plt.show();plt.close(fig)
            if len(freqs)==2: print(f"Frequency difference: {abs(freqs[1]-freqs[0]):.2f} Hz (beat rate when tones are close).")
            print("Frequency ratios:", " : ".join(f"{f/freqs[0]:.4g}" for f in freqs))
    for c in (root,interval,chord): c.observe(update,names="value")
    display(w.VBox([w.HTML("<h3>3 · Intervals & Chords</h3><p>Hear and see how adding tones produces a composite waveform. Close frequencies produce beats.</p>"),
                    w.HBox([root,interval]),chord,out]))
    update()
