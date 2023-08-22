# Based on the principle that everything in Prod is also in Dev
# Dev just has additional stuff
# Therefore we can build on top of prod image to make dev
FROM jupyter/pyspark-notebook as prod
WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY config/ config/
COPY src/ src/

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv requirements > /tmp/requirements.txt  && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Dev includes tests and notebooks and additinoal dev packages
FROM prod as dev

COPY tests/ tests/
COPY notebooks/ notebooks/

RUN pipenv requirements --dev-only > /tmp/dev_requirements.txt && \
    pip install -r /tmp/dev_requirements.txt && \
    rm /tmp/dev_requirements.txt

