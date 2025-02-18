#!/usr/bin/env bash
set -xe

sudo singularity build --force --notest base.sif base.def
singularity test      base.sif
singularity test --nv base.sif
