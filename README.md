# rleague-pyspark
Analysing Rocket League TPS competition data using PySpark, Docker, and PyTest.

# Project Status
Currently working on streamlining downloading the kaggle dataset using kaggle.json key and Docker. Using dev dockerfile target for development

Completed:

*  Multi-stage Dockerfile with seperate prod and dev targets created and run using Makefile
*  Common logger set up in src\shared\utils.py using config\logging.json. 

# Data
I'm using the Kaggle TPS rocket league data from here:
https://www.kaggle.com/datasets/alvinleenh/tps-rocket-league-data-float16-parquet-format

# Getting Started
TBC
# Components
## Docker
I've used a multi-stage Dockerfile allowing clear seperation between prod and dev files, folders, and Python pacakges.

## Makefile
I'm using a Makefile to handle building the Docker images and spinning them up. Once semi-completed I'll look at having a make run command which runs the end-to-end process from within the container.


