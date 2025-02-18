A docker image for headless VTK with open GL support

```bash
IMG=myvistatorch
docker build -t $IMG .

# to run the tests onthe docker image
docker run --iinteractive --tty --gpus all --ipc host --ulimit memlock=-1 --ulimit stack=67108864 -v .:/work $IMG
# then copy paste the below rows...
python /work/test_pyvista.py
python /work/test_xgb.py
python /work/test_transformers.py

# Convert docker image to singularity, and try it out
SIF=$IMG.sif
singularity build $SIF docker-daemon:$IMG
singularity exec --nv $SIF python test_pyvista.py
imgcat foo.png
```
