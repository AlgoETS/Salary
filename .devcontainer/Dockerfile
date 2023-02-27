ARG VARIANT=3.10-buster

# First stage: create a non-root user and install Python dependencies
FROM python:${VARIANT} AS base
ARG USERNAME=vscode

# Add non-root user
RUN groupadd --gid 1000 $USERNAME && \
    useradd --uid 1000 --gid 1000 -m $USERNAME

# add sudo
RUN apt-get update -q && apt-get install -y sudo
# add sudo privileges to user
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN echo "#!/bin/bash\n\$@" > /usr/bin/sudo
RUN chmod +x /usr/bin/sudo

# Make sure to reflect new user in PATH
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

# Update system and install dependencies
RUN apt-get update -q && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y -q install --no-install-recommends wget curl vim python3-pip \
    # Remove imagemagick due to https://security-tracker.debian.org/tracker/CVE-2019-10131
    && apt-get purge -y imagemagick imagemagick-6-common -q

USER $USERNAME

## Pip dependencies
# Upgrade pip
RUN pip install --upgrade pip

# Install poetry
RUN pip install --user poetry

# Copy dependency files and install dependencies
COPY --chown=$USERNAME:$USERNAME pyproject.toml /tmp/
RUN cd /tmp && \
    poetry install --no-root

COPY --chown=$USERNAME:$USERNAME requirements.txt /tmp/
RUN cd /tmp && pip install --user -r requirements.txt
COPY --chown=$USERNAME:$USERNAME requirements-dev.txt /tmp/
RUN cd /tmp && pip install --user -r requirements-dev.txt

# Second stage: setup Jupyter Lab
FROM base AS jupyter
# Install jupyter
RUN pip install --user jupyter jupyterlab jupyterlab-requirements
# Put jupyterlab in .bashrc
RUN echo 'alias jupyterlab="jupyter-lab --no-browser --ip=127.0.0.0 --port=8888"' >> ~/.bashrc

# Third stage: install zsh and oh-my-zsh
FROM jupyter AS zsh
# Install zsh
USER root
RUN apt-get update -q && apt-get install -y zsh
USER $USERNAME
# Install oh-my-zsh
RUN sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"


# Set default shell to zsh for non-root user
ENV SHELL="/bin/zsh"
RUN echo 'alias jupyterlab="jupyter-lab --no-browser --ip=127.0.0.0 --port=8888"' >> ~/.zshrc
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/g' ~/.zshrc