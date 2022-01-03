#!/usr/bin/env bash

mkdir -p progs

for seed in $(seq $1 $2); do
    for version in {1,2}; do
        ./generate.py \
            --seed $seed \
            --version $version \
            --workload 30 \
            -n 1000 \
            --workload 30 \
            --length 100 \
            > progs/map-$version-$seed.ml
    done
done
