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

## Alt 1 convert on host/build server

This took ca 8 hours to run in one run. In another run it just crashed out-of-memory.

```bash
singularity build $SIF docker-daemon:$IMG
singularity exec --nv $SIF python test_pyvista.py  # or whatever test files you like
imgcat foo.png                                     # if you have iTerm2 and want to look at images, run imgcat (must be in path)
rsync --progress --human-readable $SIF elhult@transit.uppmax.uu.se:sens2020598
```

## Alt 2 convert on bianca
On the build host, if sending from mitevs build server
```
date ; docker save --output $TAR $IMG ; date
rsync --progress --human-readable --compress $SIF            elhult@transit.uppmax.uu.se:sens2020598
rsync --progress --human-readable --compress test_pyvista.py elhult@transit.uppmax.uu.se:sens2020598
```
It took very long time (many hours? i didnt record the time) if doing it on the build server.

The `docker save` took 8 minutes if I built the docker image on my old windows laptop. That is very much better, but on the other hand I don't have a GPU there to test the image on.
I could not also not use rsync from wsl2, since cisco has messed up the VPN See more on https://gist.github.com/pyther/b7c03579a5ea55fe431561b502ec1ba8 So I used replaced the rsync call in WSL with sftp from powershell instead. cd into the correct folder and run
 ```powershell
 echo "put mytorchvista.tar" | sftp elhult-sens2020598@bianca-sftp.uppmax.uu.se:/elhult-sens2020598
 ```
this transfer took an hour or so.

Finally, we want to do the conversion to singularity on bianca. ssh into to bianca and continue there.
```bash
salloc --qos interact -n 16 -t 12:00:00 -A sens2020598 --no-shell
# get some allocation, on e.g. bianca-b4
ssh b4 # shortcut that expands and sends me right
cd /proj/nobackup/sens2020598/wharf/elhult/elhult-sens2020598/ # landing site in wharf for the transfer
singularity build $SIF docker-archive://$TAR
singularity exec --nv $SIF python test_pyvista.py
```
building takes an hour or so when using 16 cores
