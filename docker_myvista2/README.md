A docker image for headless VTK with open GL support


# Build and test docker file

```bash
IMG=mytorchvista
TAR=$IMG.tar
SIF=$IMG.sif
date ; docker build -t $IMG . ; date
# when running in WSL2 on my windows machine with docker Desktop, for some reason, I must call it like below  
# see discussion on https://stackoverflow.com/questions/66146088/docker-gets-error-failed-to-compute-cache-key-not-found-runs-fine-in-visual
date ; docker build -t $IMG -f Dockerfile . ; date

# to run the tests onthe docker image
docker run --interactive --tty --gpus all --ipc host --ulimit memlock=-1 --ulimit stack=67108864 --volume .:/work $IMG
# then copy paste the below rows into the terminal inside the docker container
python /work/test_pyvista.py
python /work/test_xgb.py
python /work/test_transformers.py
```

# Building and testing singularity

## ALT 1 convert on host/build server

this took ca 8 hours to run...

```bash
singularity build $SIF docker-daemon:$IMG
singularity exec --nv $SIF python test_pyvista.py  # or whatever test files you like
imgcat foo.png                                     # if you have iTerm2 and want to look at images, run imgcat (must be in path)
rsync --progress --human-readable $SIF elhult@transit.uppmax.uu.se:sens2020598
```

## Alt 2 convert on bianca
(on the build host)
```
date ; docker save --output $TAR $IMG ; date
rsync --progress --human-readable --compress $SIF            elhult@transit.uppmax.uu.se:sens2020598
rsync --progress --human-readable --compress test_pyvista.py elhult@transit.uppmax.uu.se:sens2020598
```
(ssh into to bianca)
```bash
cd /proj/nobackup/sens2020598/wharf/elhult/elhult-sens2020598/
singularity build $SIF docker-archive:$TAR
singularity exec --nv $SIF python test_pyvista.py
```
