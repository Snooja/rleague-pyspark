# rleague-pyspark
Analysing Rocket League TPS competition data using PySpark, Docker, and PyTest.

# Getting Started
At the moment I'm using dev containers in VSCode to develop. But the Makefile can be used to build images from the Dokcerifle and spin up containers as well.

# Project
## Status
In Development

Completed:
* Multi-stage Dockerfile with seperate prod and dev targets created and run using Makefile and pipenv piping to pip install.
* Common logger set up in src\shared\utils.py using config\logging.json.
* Migrated from Make commands to .devcontainer for development including mounting api key directories. 
* Relative imports in src folder working from script directly, main.py, and pytest.
* Jupyter notebooks now work using /opt/venv/bin/python as the interpreter

## TODO
* Finish extract and transform steps in notebook then migrate to etl.py
* Load data ?somewhere? ready for analysis stage

## Structure
* .devcontainer for containerised development
* config folder for general config and logger configs
* data folder for raw and processed data
* notebooks folder for jupyter notebooks used for initial EDA and development
src
* src folder contains jobs and shared folder, and main.py for majority of Python code
* tests folder for pytests
* Dockerfile contains multi-stage image builds using Pipenv just during build to pipe into requirements.txt for pip install
* Pipfile and Pipfile.lock for package control
* Makefile as alternative way to build and run dev and prod containers


# Datasets
I'm using the Kaggle TPS rocket league data from here:
https://www.kaggle.com/datasets/alvinleenh/tps-rocket-league-data-float16-parquet-format



