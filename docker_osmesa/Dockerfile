FROM nvcr.io/nvidia/pytorch:25.01-py3 

ARG PYTHON=python
RUN $PYTHON -m pip install pyvista

# install all other python dependencies
# N.B. check https://docs.docker.com/build/building/best-practices/#add-or-copy
# it suggests bind mounts instead o add/copy for a requirements file
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
  $PYTHON -m pip install --no-cache-dir --requirement /tmp/requirements.txt 

# replace VTK with VTK-osmesa instead
# as they do in https://github.com/pyvista/pyvista/blob/main/docker/jupyter.Dockerfile
RUN $PYTHON -m pip uninstall vtk -y
RUN $PYTHON -m pip install --no-cache-dir --extra-index-url https://wheels.vtk.org vtk-osmesa

# setting variables for the user later on
ENV PYVISTA_OFF_SCREEN=true


