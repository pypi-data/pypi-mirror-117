# grgr
`grgr` is a library for using `ggplot2` from `python`.  

`grgr` can create figures in `python` using grammar similar to `ggplot2`. `python` does not create the figure itself, but generates a code that can be executed in `R`, and executes it in R to create the figure. In other words, `grgr` is an interface from `python` to `R`'s `ggplot2`. Therefore, this library directly depends on `R` and `ggplot2`.

# Quickstart
You can install `grgr` through `pip` by running `pip install grgr`. In order to use `grgr`, you need to have `R` and `ggplot2` installed. Please make sure that these are installed beforehand. Once the installation is complete, you can draw a figure in `python` with the grammer same as `ggplot2`. A basic usage example can be found in `example/basic.py`.
