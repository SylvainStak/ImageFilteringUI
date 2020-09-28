# ImageFilteringUI

ImageFilteringUI is a little piece of software that lets you select images and apply different filters on them.

This tool is completely open source, so you can watch closely how each algorithm for every filter works.

NVIDIA GPU proccessing has been added so in order to be able to run functions that loads really big data sets using GPU you need to install cudatoolkit from NVIDIA and Anaconda for python, then run

```sh
$ conda install numba
```

```sh
$ conda install cudatoolkit
```