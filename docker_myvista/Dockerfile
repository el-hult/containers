FROM ubuntu:latest

# dependencies for VTK installation
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y ninja-build cmake libegl1-mesa-dev python3-dev git g++

# build VTK using EGL
RUN git clone https://github.com/Kitware/VTK
RUN mkdir VTK/build
WORKDIR /VTK/build
RUN git checkout v9.3.0
RUN cmake -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DVTK_BUILD_TESTING=OFF \
  -DVTK_BUILD_DOCUMENTATION=OFF \
  -DVTK_BUILD_EXAMPLES=OFF \
  -DVTK_MODULE_ENABLE_VTK_PythonInterpreter:STRING=NO \
  -DVTK_MODULE_ENABLE_VTK_WebCore:STRING=YES \
  -DVTK_MODULE_ENABLE_VTK_WebGLExporter:STRING=YES \
  -DVTK_MODULE_ENABLE_VTK_WebPython:STRING=YES \
  -DVTK_WHEEL_BUILD=ON \
  -DVTK_PYTHON_VERSION=3 \
  -DVTK_WRAP_PYTHON=ON \
  -DVTK_OPENGL_HAS_EGL:BOOL=ON \
  -DVTK_USE_X:BOOL=OFF \
  -DVTK_USE_COCOA:BOOL=OFF \
  -DVTK_DEFAULT_RENDER_WINDOW_HEADLESS:BOOL=ON \
  -DPython3_EXECUTABLE=/usr/bin/python3 ../
RUN ninja

# build the python wheel from the VTK we just built, and install it
RUN apt-get install -y python3-pip python3-venv
RUN python3 -m venv /myenv
ARG PYTHON=/myenv/bin/python
RUN $PYTHON -m pip install wheel setuptools
RUN $PYTHON setup.py bdist_wheel
RUN $PYTHON -m pip install dist/vtk-*.whl

# install pyvista
RUN $PYTHON -m pip install pyvista

# setting variables for the user later on
ENV PYVISTA_OFF_SCREEN=true


