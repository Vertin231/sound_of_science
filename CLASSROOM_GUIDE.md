# Classroom deployment (Windows + USB)

## What to copy to the USB drive

Copy the entire `sound_of_science` project folder to the USB drive. Keep the folder structure intact. Do not copy your development computer's `.venv` folder; the launcher creates a fresh environment on the classroom computer.

The USB copy should contain at least:

- `main.ipynb`
- `requirements.txt`
- `start_demo.bat`
- `core/`
- `modules/`
- `visualization/`

## First run on the classroom computer

Requirements:

- Windows 10/11
- Python 3.10 or newer (Python 3.11 recommended)
- Internet access for the first setup

Steps:

1. Insert the USB drive.
2. Open the `sound_of_science` folder.
3. Double-click `start_demo.bat`.
4. On first run, the script creates `.venv` on the USB/project folder and installs dependencies from `requirements.txt`.
5. JupyterLab opens `main.ipynb` in the browser.
6. In JupyterLab, select the kernel from the project's `.venv` if prompted, then run the notebook cells from top to bottom.

The first run can take several minutes depending on network speed. Later launches reuse the environment and are faster.

## Before the talk

- Test the USB on the actual classroom computer at least one day beforehand.
- Keep the laptop connected to power and disable sleep.
- Connect the projector and set a suitable resolution.
- Open `main.ipynb`, run all cells, and test every slider/dropdown.
- Close unrelated browser tabs and notifications.
- Keep the PowerShell/terminal window opened by the launcher running throughout the talk.

## Important portability notes

- The `.venv` folder is created on the classroom computer and is specific to that computer and its Python installation. Do not prepare it on one computer and assume it will work on another.
- The first setup requires internet access. If the classroom network is unreliable, run the launcher once on the classroom computer in advance while connected to a reliable network.
- If the classroom computer has no Python installed, install Python 3.11 first from https://www.python.org/downloads/ and enable **Add Python to PATH**. The launcher does not install Python itself.
- Do not unplug the USB drive while JupyterLab is running.
- To stop JupyterLab, return to the terminal window and press Ctrl+C.

## Troubleshooting

- **Python not found:** install Python 3.11 and enable Add Python to PATH.
- **Dependency installation fails:** check internet access, then run `start_demo.bat` again.
- **Plots/widgets do not render:** restart the notebook kernel and rerun cells from the top. Confirm that `ipympl` and `ipywidgets` were installed in the project's environment.
- **Drive letter changes:** no change is needed; the launcher uses its own folder location rather than a fixed drive letter.
