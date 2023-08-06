# Meteopy

Meteopy is a phony package created to illustrate the organization of a python project (from environment and package management to distribution).

Meteopy allows you to watch netcdf files content :

```python
>>> import meteopy
>>> meteopy.view("my_file.nc")
```

## Installation

### Quick installation

To install Meteopy, simply : 
```bash
$ pip install meteopy
```
**Dependencies :** Meteopy depends on `xarray` and `matplotlib`.

### Dev installation

To use Meteopy in dev-mode :
```bash
$ git clone https://git.meteo.fr/deep_learning/demo-projet-python.git
$ cd demo-projet-python
$ make install
```
**Dependencies :** Dev-mode relies on conda for package and environment management.
