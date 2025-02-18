```bash
IMG=picasso
DEF=$IMG.def
SIF=$IMG.sif

sudo singularity build --force --notest $SIF $DEF
singularity test      $SIF
singularity test --nv $SIF

```
