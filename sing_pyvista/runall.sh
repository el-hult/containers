#!/usr/bin/env bash
set -xe

sudo singularity build --force --notest base.sif base.def
singularity test      base.sif
singularity test --nv base.sif

sudo singularity build --force --notest pip.sif pip.def
singularity test      pip.sif
singularity test --nv pip.sif

sudo singularity build --force --notest pyvista.sif pyvista.def
singularity test      pyvista.sif
singularity test --nv pyvista.sif