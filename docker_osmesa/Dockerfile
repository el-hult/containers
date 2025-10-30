FROM nvcr.io/nvidia/pytorch:25.10-py3 

ARG PYTHON=python

# these libs are needed for the EGL layer to work
# without it, VTK crashes
# This seemes to work for VTK 9.5
RUN apt update && apt install --assume-yes --no-install-recommends libx11-dev libxrender-dev libegl1-mesa-dev 

# install python dependencies
# N.B. check https://docs.docker.com/build/building/best-practices/#add-or-copy
# it suggests bind mounts instead o add/copy for a requirements file
RUN \
  --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
  --mount=type=cache,id=pip-cache,target=/root/.cache/pip
  $PYTHON -m pip install --requirement /tmp/requirements.txt 

# setting variables for the user later on
ENV PYVISTA_OFF_SCREEN=true
