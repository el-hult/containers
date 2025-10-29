FROM nvcr.io/nvidia/pytorch:25.10-py3 

ARG PYTHON=python

# install python dependencies
# N.B. check https://docs.docker.com/build/building/best-practices/#add-or-copy
# it suggests bind mounts instead o add/copy for a requirements file
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
  $PYTHON -m pip install --no-cache-dir --requirement /tmp/requirements.txt 

# setting variables for the user later on
ENV PYVISTA_OFF_SCREEN=true


