#!/usr/bin/env bash

mkdir -p results

for seed in $(seq $1 $2); do
    for version in {1,2}; do
        ocamlbuild progs/map-$version-$seed.native
    done
done

hyperfine -P seed $1 $2 ./map-1-{seed}.native ./map-2-{seed}.native --runs 10 --warmup 3 --export-csv results/results.csv

