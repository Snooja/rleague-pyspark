# Based on the principle that everything in Prod is also in Dev
# Dev just has additional stuff
# Therefore we can build on top of prod image to make dev
# +-----------------------------+
# | BASE IMAGE             ~32MB|        See https://hub.docker.com/_/debian
# +-----------------------------+

FROM debian:bookworm-slim as prod

# +-----------------------------+
# | METADATA                    |
# +-----------------------------+

LABEL org.opencontainers.image.vendor = "Jens A. Koch"
LABEL org.opencontainers.image.source = "https://github.com/jakoch/jupyter-devbox"

# +-----------------------------+
# | ARGS                        |
# +-----------------------------+

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# +-----------------------------+
# | ENV                         |
# +-----------------------------+

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

# +-----------------------------+
# | PRE-REQUISITES/INIT PACKAGES |
# +-----------------------------+

# avoid debconf delaying package configuration, since apt-utils is not installed
RUN apt-get update && \
    apt-get -y install --no-install-recommends apt-utils dialog sudo 2>&1

# Setup User and enable sudo
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        git zsh curl wget nano openssh-client \
        gcc g++ build-essential cmake build-essential \
        unzip libjpeg-dev libpng-dev libpq-dev \
        imagemagick gnuplot gnuplot-x11 libssl-dev libzmq3-dev graphviz \
        # py3
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        python3-wheel \
        python3-setuptools \
        python3-opencv \
        libopencv-dev

# Cleanup
RUN apt-get autoremove -fy && \
    apt-get clean && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/*

# Use a virtual environment for Python (to avoid PEP668 "externally managed environment" error).
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Update python packge installers
#ARG PIP_BREAK_SYSTEM_PACKAGES=1
RUN pip3 config --user set global.disable-pip-version-check true && \
    pip3 config --user set global.progress_bar off && \
    pip3 config --user set global.no-cache-dir true && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    pip3 install --upgrade wheel && \ 
    pip3 install --upgrade pipenv


# Install Python Packages
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv requirements > /tmp/requirements.txt && \
    pip3 install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Copy Project Code
COPY config/ config/
COPY src/ src/

# re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog

# Dev includes tests and notebooks and additinoal dev packages
FROM prod as dev


COPY ../tests/ tests/
COPY ../notebooks/ notebooks/

# Use a virtual environment for Python (to avoid PEP668 "externally managed environment" error).
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pipenv requirements --dev-only > /tmp/dev_requirements.txt && \
    pip3 install -r /tmp/dev_requirements.txt && \
    rm /tmp/dev_requirements.txt

