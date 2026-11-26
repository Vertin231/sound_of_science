import numpy as np
from core.signal import harmonic_signal, make_waveform
from core.fourier import single_sided_spectrum
from core.music_theory import note_frequency

def test_signal_time_and_length():
    s=harmonic_signal(100, .1, 1000, [1])
    assert len(s.samples)==100
    assert np.isclose(s.time[-1], .099)

def test_sine_peak():
    s=make_waveform("sine",100,.1,1000)
    assert np.isclose(np.max(s.samples),1,atol=.02)

def test_fft_peak():
    sr=8000
    t=np.arange(sr)/sr
    f,a=single_sided_spectrum(np.sin(2*np.pi*440*t),sr,window=False)
    assert f[np.argmax(a)]==440

def test_octave():
    assert np.isclose(note_frequency(12),880)
