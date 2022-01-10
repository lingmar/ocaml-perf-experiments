# OCaml performance experiments

How to run the experiments for 100 programs:
1. `./generate.sh 1 100`
2. `./benchmark.sh 1 100`
3. The resulting CSV file can be found in `results/results.csv`

The Jupyter notebook `plot.ipynb` can be used to plot the results.

Requirements: 
* Python 3 (along with libraries such as `numpy`, `pandas` and `scipy`)
* `hyperfine` tool
