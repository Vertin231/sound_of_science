"""Reusable discrete-time signal models."""
from dataclasses import dataclass
import numpy as np

@dataclass
class Signal:
    samples: np.ndarray
    sample_rate: int
    label: str = "signal"

    def __post_init__(self):
        self.samples = np.asarray(self.samples, dtype=float)
        if self.samples.ndim != 1:
            raise ValueError("Signal samples must be one-dimensional.")
        if self.sample_rate <= 0:
            raise ValueError("sample_rate must be positive.")

    @property
    def time(self):
        return np.arange(self.samples.size) / self.sample_rate

    @property
    def duration(self):
        return self.samples.size / self.sample_rate

    def normalized(self):
        peak = np.max(np.abs(self.samples)) if self.samples.size else 0.0
        return Signal(self.samples / peak if peak else self.samples.copy(),
                      self.sample_rate, self.label)

    def __add__(self, other):
        if not isinstance(other, Signal):
            return NotImplemented
        if self.sample_rate != other.sample_rate or self.samples.size != other.samples.size:
            raise ValueError("Signals must have the same sample rate and length.")
        return Signal(self.samples + other.samples, self.sample_rate,
                      f"{self.label} + {other.label}")

    def __call__(self, time):
        indices = np.rint(np.asarray(time) * self.sample_rate).astype(int)
        indices = np.clip(indices, 0, max(0, self.samples.size - 1))
        return self.samples[indices]

def harmonic_signal(frequency=440.0, duration=0.02, sample_rate=44100,
                    amplitudes=(1.0,), phases=None):
    """Build a harmonic sum: sum A_n sin(2 pi n f0 t + phase_n)."""
    if frequency <= 0 or duration <= 0 or sample_rate <= 0:
        raise ValueError("frequency, duration and sample_rate must be positive.")
    amplitudes = np.asarray(amplitudes, dtype=float)
    if phases is None:
        phases = np.zeros(amplitudes.size)
    phases = np.asarray(phases, dtype=float)
    if phases.size != amplitudes.size:
        raise ValueError("amplitudes and phases must have equal lengths.")
    t = np.arange(int(duration * sample_rate)) / sample_rate
    y = np.zeros_like(t)
    for n, (amp, phase) in enumerate(zip(amplitudes, phases), start=1):
        y += amp * np.sin(2 * np.pi * n * frequency * t + phase)
    return Signal(y, sample_rate, f"{frequency:g} Hz harmonic sum")

def make_waveform(kind="sine", frequency=440.0, duration=0.02,
                  sample_rate=44100, harmonics=12):
    """Generate standard periodic waveforms using Fourier-series approximations."""
    if kind == "sine":
        amps = [1.0]
    elif kind == "square":
        amps = [1/n if n % 2 else 0 for n in range(1, harmonics + 1)]
    elif kind == "sawtooth":
        amps = [((-1)**(n+1))/n for n in range(1, harmonics + 1)]
    elif kind == "triangle":
        amps = [((-1)**((n-1)//2))/(n*n) if n % 2 else 0 for n in range(1, harmonics + 1)]
    else:
        raise ValueError("kind must be sine, square, sawtooth, or triangle")
    return harmonic_signal(frequency, duration, sample_rate, amps)
