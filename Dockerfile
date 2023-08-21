# Base image
FROM jupyter/pyspark-notebook as base
WORKDIR /app
RUN pip install pipenv
COPY config/kaggle.json /home/jovyan/.kaggle/kaggle.json
#RUN chmod 600 /home/jovyan/.kaggle/kaggle.json
COPY Pipfile Pipfile
COPY config/ config/
COPY src/ src/

# Dev includes tests and notebooks and uses the dev pipenv install
FROM base as dev
COPY tests/ tests/
COPY notebooks/ notebooks/
RUN pipenv install --dev

# Prod
FROM base as prod
RUN pipenv install 

