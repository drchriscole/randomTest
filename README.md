# randomTest

Quick script to test whether setting a fixed random seed works
across platforms for a minimal machine-learning exercise.

By "works" I mean that regardless of the platform using a fixed
seed gives exactly the same results. My expectation is that yes
it would which is the point of deterministic random seeds.

## Quick Start

Simply run the script in the terminal:

    python3 randomTest.py

It should give the following outputs:

    Test set labels:
    [0 0 0 1 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 0 1 1 1 0
     1 1 1 1 1 1 1 0 1 0 0 1 1 1 1 1 1 0 1 1]
    5-fold cross-validation scores:
    [0.97087379 0.96116505 0.95098039 0.99019608 0.91176471]