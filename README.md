# Sound of Science

**Explore the physics of sound and the mathematics of music.**

Sound of Science is an interactive Python project designed for a science outreach talk. It connects simple physical models with audible signals, time-domain waveforms, and frequency-domain spectra.

## Four interactive demonstrations

1. **Waveform & Timbre** — compare sine, square, sawtooth, and triangle waves; explore harmonic synthesis.
2. **Noise & Music** — compare periodic tones, mixtures, and noise in the time and frequency domains.
3. **Intervals & Chords** — investigate frequency ratios, superposition, and beating.
4. **Equal Temperament** — build the twelve-tone equal-tempered scale and compare it with just intervals.

## Quick start

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS / Linux:
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Open `main.ipynb` and run the cells from top to bottom.

For interactive Matplotlib figures, the notebook uses the `ipympl` widget backend. If the plots do not respond, restart the kernel after installing the requirements.

## Project structure

```text
sound_of_science/
├── core/              # Signal models and numerical operations
├── modules/           # Four independent interactive demonstrations
├── visualization/     # Shared plotting helpers
├── tests/             # Core unit tests
├── main.ipynb         # Talk/demo entry point
└── requirements.txt
```

## Scientific notes

- A musical sound is not simply "periodic", and noise is not simply "non-periodic". The demonstrations use these as useful examples, not as a strict definition of music.
- A Fourier spectrum describes frequency content; it does not by itself explain musical meaning or emotional response.
- The equal-tempered semitone ratio is \(2^{1/12}\). A justly tuned perfect fifth has ratio \(3/2\), while the equal-tempered fifth is \(2^{7/12}\).

## Development

Run the tests with:

```bash
python -m pytest
```

The project separates signal calculations from plotting and widgets so the numerical core can also be reused in scripts or other interfaces.

## License

MIT
