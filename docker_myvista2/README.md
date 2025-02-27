A docker image for headless VTK with open GL support

```bash
IMG=mytorchvista
docker build -t $IMG .

# to run the tests onthe docker image
docker run --interactive --tty --gpus all --ipc host --ulimit memlock=-1 --ulimit stack=67108864 --volume .:/work $IMG
# then copy paste the below rows into the terminal inside the docker container
python /work/test_pyvista.py
python /work/test_xgb.py
python /work/test_transformers.py

# Convert docker image to singularity, and try it out
# this took ca 8 hours to run...
SIF=$IMG.sif
singularity build $SIF docker-daemon:$IMG

# to run a certain test file in the singularity container, run like this
singularity exec --nv $SIF python test_pyvista.py

# if you have iTerm2 and want to look at images, run imgcat (must be in path)
imgcat foo.png

# push to bianca
rsync --progress --human-readable mytorchvista.sif elhult@transit.uppmax.uu.se:sens2020598
```
