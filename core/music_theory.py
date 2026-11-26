"""Small, explicit music-theory calculations."""
import numpy as np

NOTE_NAMES = ["C", "C♯", "D", "D♯", "E", "F",
              "F♯", "G", "G♯", "A", "A♯", "B"]

def note_frequency(semitones_from_a4, reference=440.0):
    return reference * 2 ** (np.asarray(semitones_from_a4) / 12)

def equal_tempered_scale(root_frequency=440.0, semitones=range(13)):
    return [(int(n), float(root_frequency * 2 ** (n / 12))) for n in semitones]

def interval_frequency(root, semitones):
    return root * 2 ** (semitones / 12)
