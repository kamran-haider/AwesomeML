# AwesomeML
Building and Distributing Packages in Python using Conda Framework

In this workshop, we will go through the basics of building and distributing python packages.
We will focus on machine learning codes, e.g., a new classifier and we will take it all the way
from a just a python script to a maintainable and installable package.

# Set up
In order to set up for the first time, clone this repository:
```commandline

conda env create -f environment.yml
source activate qaanalyzer-env
make test
```
If there have been changes in the setup
```commandline
source deactivate qaanalyzer-env
conda env update -f environment.yml
source activate qaanalyzer-env
```