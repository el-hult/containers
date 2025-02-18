A docker image for headless VTK with open GL support

This is a quite minimal ubuntu setup, but with VTK 9.3 compiled from source, with EGL support.

When converting to  singularity, some stuff breaks due to something I don't understand, but the code seem to  WORK at least. noice.

```bash
# build the environment with docker
docker build -t myvista .
docker run -v .:/work myvista /myenv/bin/python /work/sphere.py /work/bar.png
docker save myvista --output myvista.tar

# Convert docker image to singularity, and try it out
SIF=./myvista.sif
singularity build $SIF docker-archive:myvista.tar
singularity exec --nv $SIF /myenv/bin/python sphere.py foo.png
imgcat foo.png
```
