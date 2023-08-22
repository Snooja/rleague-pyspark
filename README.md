# rleague-pyspark
Analysing Rocket League TPS competition data using PySpark, Docker, and PyTest.

# Project Status
Currently working on streamlining downloading the kaggle dataset using kaggle.json key and Docker. Using dev dockerfile target for development

Completed:
*  Multi-stage Dockerfile with seperate prod and dev targets created and run using Makefile and pipenv piping to pip install.
*  Common logger set up in src\shared\utils.py using config\logging.json. 

# Data
I'm using the Kaggle TPS rocket league data from here:
https://www.kaggle.com/datasets/alvinleenh/tps-rocket-league-data-float16-parquet-format

# Getting Started
At the moment I'm using dev containers in VSCode to develop. But the Makefile can be used to build images from the Dokcerifle and spin up containers as well.


