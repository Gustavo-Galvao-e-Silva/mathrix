# Installation

## From PyPI

```bash
pip install panchi
```

Requires Python 3.10 or higher.

## Optional: Manim backend

The core library only depends on Matplotlib. If you want Manim-powered animated visualizations, install the optional extra:

```bash
pip install panchi[manim]
```

Note that Manim requires system-level dependencies (Cairo, FFmpeg, LaTeX). See the [Manim installation guide](https://docs.manim.community/en/stable/installation.html) if you run into issues.

## From source

```bash
git clone https://github.com/Gustavo-Galvao-e-Silva/panchi.git
cd panchi
pip install -e ".[dev]"
```

This installs panchi in editable mode along with development tools (pytest, mypy, black, ruff).

## Verifying the installation

```python
import panchi as pan
print(pan.__version__)
print(pan.identity(3))
```
