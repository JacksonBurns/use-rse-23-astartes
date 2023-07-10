# Extrapolation and Interpolation in Machine Learning Modeling with Fast Food and `astartes`

## Abstract
Machine learning is a groundbreaking tool for tackling high-dimensional datasets with complex correlations that humans struggle to comprehend.
An important nuance of ML is the difference between using a model for interpolation or extrapolation, meaning either inference or prediction.
This work will demonstrate visually what interpolation and extrapolation mean in the context of machine learning using `astartes`, a Python package that makes it easy to tackle in ML modeling.
Many different sampling approaches are made available with `astartes`, so using a very tangible dataset - a fast food menu - we can visualize how different approaches differ and then train and compare ML models.

## Usage
This repository contains the `split_comparisons.ipynb` file and associated environment files for submission to the United States Research Software Engineer Association 2023 Conference.
The notebook walks the user through the software tool `astartes` and its application to machine learning validation and testing.
You may view the notebook in a number of different ways:
 1. \[__Recommended__\] Visit the GitHub pages site [at this link](https://jacksonburns.github.io/use-rse-23-astartes/split_comparisons.html) to view the notebook rendered as an interactive webpage with Quarto.
 2. Run this notebook live and in your browser _without installation_ using Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JacksonBurns/use-rse-23-astartes/main?labpath=split_comparisons.ipynb)
 3. To execute locally:
    1. clone this repository
    2. build the environment with `pip install -r requirements.txt` using any version of Python from 3.7 to 3.11
    3. open `split_comparisons.ipynb` in your preferred notebook IDE, i.e. `jupyter` or VSCode

### Reproducibilty of USRSE23 Submission
The `conda-environment.yml` file provides the exact package versions and builds used to run the notebook for submission to the USRSE2023 conference, and `requirements.txt` specifies a set of 'loose' requirements as well as more 'strict' requirements that match the `conda` file but are cross platform.
`astartes` has been designed to be strictly backwards compatible and reproducible, so this notebook should be identical with all minor releases of `astartes` v1.

_Note: this repository is based on [`astartes`](https://github.com/JacksonBurns/astartes)'s main repository, with changes to conform to the submission criteria for RSE23. Visit the `astartes` repository for other examples and additional detail about `astartes`._