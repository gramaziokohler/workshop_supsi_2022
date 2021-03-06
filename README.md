# SUPSI SUPERFAB Summer School

[🎦 Slides](https://docs.google.com/presentation/d/1YkNU2KeMX9iotR79TOqGxQhPTd6fq15RnppwAX3oJYk/edit) | [📃 COMPAS docs](https://compas.dev)

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Rhino 6/7 & Grasshopper](https://www.rhino3d.com/download)

Optional:

* [Docker Desktop](https://www.docker.com/products/docker-desktop) After installation on Windows, it is required to enable "Virtualization" on the BIOS of the computer.
* [Visual Studio Code](https://code.visualstudio.com/): Any python editor works, but we recommend VS Code + extensions [as mentioned in our docs](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html#working-in-visual-studio-code-1)

## Installation

We use `conda` to make sure we have clean, isolated environment for dependencies.

<details><summary>First time using <code>conda</code>?</summary>
<p>

Make sure you run this at least once:

    (base) conda config --add channels conda-forge

</p>
</details>

    (base) conda env create -f https://dfab.link/supsi22.yml

### Add to Rhino

    (base)  conda activate fab22
    (fab22) python -m compas_rhino.install -v 7.0

### Get the workshop files

Download the [zip file from Github](https://github.com/gramaziokohler/workshop_supsi_2022/archive/refs/heads/main.zip).

Or optionally, clone the repository instead:

    (fab22) cd Documents
    (fab22) git clone https://github.com/gramaziokohler/workshop_supsi_2022.git

### Verify installation

    (fab22) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 1.16.0
    Python: 3.8.13 (CPython)
    Extensions: ['compas-fab', 'compas-cgal', 'compas-rrc']

### Update installation

To update your environment:

    (fab22) conda env update -f https://dfab.link/supsi22.yml
