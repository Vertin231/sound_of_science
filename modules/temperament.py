"""Demo 4: twelve-tone equal temperament."""
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as w
from IPython.display import display
from core.music_theory import NOTE_NAMES

def create_demo():
    ref = w.IntSlider(value=440,min=400,max=480,step=1,description="A4 (Hz)")
    out = w.Output()
    figures = []  # Keep active ipympl figures alive until the next redraw.
    def update(*_):
        with out:
            out.clear_output(wait=True)
            for old_fig in figures:
                plt.close(old_fig)
            figures.clear()
            semis=np.arange(-9,4)
            freqs=ref.value*2**(semis/12)
            labels=[NOTE_NAMES[(n+9)%12] + str(4+(n+9)//12) for n in semis]
            fig,ax=plt.subplots(figsize=(9,3.8))
            ax.stem(freqs,np.ones_like(freqs),basefmt=" ")
            ax.set_xticks(freqs,labels,rotation=35)
            ax.set(title="Equal-tempered notes around A4",xlabel="Frequency (Hz)",ylabel="Note markers")
            ax.grid(axis="x",alpha=.2);fig.tight_layout();figures.append(fig);plt.show()
            fifth_equal=2**(7/12); fifth_just=3/2
            cents=1200*np.log2(fifth_equal/fifth_just)
            print(f"Semitone ratio: 2^(1/12) = {2**(1/12):.8f}")
            print(f"Equal-tempered fifth: {fifth_equal:.8f}")
            print(f"Just fifth (3:2):      {fifth_just:.8f}")
            print(f"Difference: {cents:.3f} cents")
    ref.observe(update,names="value")
    display(w.VBox([w.HTML("<h3>4 · Twelve-tone Equal Temperament</h3><p>Move the A4 reference and compare the equal-tempered fifth with the pure 3:2 fifth.</p>"),ref,out]))
    update()
