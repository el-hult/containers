Like the docker_myvista2 but I opted to go for the precompiled VTK wheels with osmesa, since I did not get EGL to work anyways.

I started an attempt to build this on my macbook with cross compilation. The idea was to:


```bash
docker build --platform=linux/amd64 --tag osmesa .

docker save osmesa --output osmesa.tar

rsync --progress --human-readable --compress osmesa.tar \
  elhult@transit.uppmax.uu.se:sens2020598

ssh bianca
cd wharf
singularity build osmesa.sif docker-archive://osmesa.tar
singularity exec --nv osmesa.sif python # test stuffs
```

