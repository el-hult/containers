#!/usr/bin/env bash
set -xe

sudo singularity build --force --notest pip.sif pip.def
singularity test      pip.sif
singularity test --nv pip.sif
