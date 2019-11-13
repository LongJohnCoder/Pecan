# Pecan

[![Build Status](https://travis-ci.org/ReedOei/Pecan.svg?branch=master)](https://travis-ci.org/ReedOei/Pecan)

## Installation

You will need Python 3.3 or higher.

Then, install [spot](https://spot.lrde.epita.fr/install.html), if you are on a Linux system, the `install-spot.sh` script may work for you:

```bash
bash install-spot.sh
```

Otherwise, follow the instructions on the spot website.

You will also need to install the libraries in `requirements.txt`:

```bash
# Use the appropriate line for your pip installation (if pip --version says 3.x, then you should be good; otherwise use/install pip3)
pip install -r requirements.txt
pip3 install -r requirements.txt
```

## Examples

```

```

## Configuration

The `PECAN_PATH` environment variable controls which paths are searched for files when importing/loading automata.
It should be a colon-separated or semicolon-separated list of paths, depending on your operating system (Linux/MacOs uses `:`, Windows uses `;`).

## Todo

- Plotting?
- Debug mode
- Verbose output (timing/state/transition counts on intermediate steps à la Walnut)
- Documentation

