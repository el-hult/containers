A docker image for headless VTK with open GL support

```bash
IMG=myvistatorch
TAR=IMG.tar
SIF=IMG.sif
date ; docker build -t $IMG . ; date
# when running in WSL2 on my windows machine with docker Desktop, for some reason, I must call it like below  
# see discussion on https://stackoverflow.com/questions/66146088/docker-gets-error-failed-to-compute-cache-key-not-found-runs-fine-in-visual
date ; docker build -t $IMG -f Dockerfile . ; date

# to run the tests onthe docker image
docker run --interactive --tty --gpus all --ipc host --ulimit memlock=-1 --ulimit stack=67108864 -v .:/work $IMG
# then copy paste the below rows into the terminal inside the docker container
python /work/test_pyvista.py
python /work/test_xgb.py
python /work/test_transformers.py


#
# ALT 1 convert on host
#

# Convert docker image to singularity, and try it out
# this took ca 8 hours to run...
singularity build $SIF docker-daemon:$IMG

# to run a certain test file in the singularity container, run like this
singularity exec --nv $SIF python test_pyvista.py

# if you have iTerm2 and want to look at images, run imgcat (must be in path)
imgcat foo.png

# push to bianca
rsync --progress --human-readable mytorchvista.sif elhult@transit.uppmax.uu.se:sens2020598

# 
# Alt 2 convert on bianca
#
date ; docker save --output $TAR $IMG ; date
```
