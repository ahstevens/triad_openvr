# Triad OpenVR Python Wrapper

This is an enhanced wrapper for the already excellent [pyopenvr library](https://github.com/cmbruns/pyopenvr) by [cmbruns](https://github.com/cmbruns).  The goal of this library is to create easy to use python functions for any SteamVR tracked system.

# Setup

- [Steamvr](https://www.steamvr.com/)
- Python >=3.6 (best to use a python environment via something like Anaconda or [Miniconda](https://conda.io/projects/conda/en/latest/index.html))
  - Example conda env setup: `conda create -n vivetracker pip matplotlib`
  - Activate the python env: `conda activate vivetracker`
- Install the OpenVR Python library in your python env: `pip install openvr`

- Open C:\Program Files (x86)\Steam\config\steamvr.vrsettings
- Add an entry nested under the "steamvr" object: `"requireHmd" : false,`

- Download this repo and navigate to it in your conda console
- `python tracker_test_vislab.py` 

# Changelog

1/18/2024  
(ahs) Updated wrapper and some examples updated to work with newer version of OpenVR python library
