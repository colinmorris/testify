#!/bin/bash

OUTDIR="generated"

for problem in anagram wordcount leap hamming
do
  python unittests.py $problem.json py > $OUTDIR/test_$problem.py
  python unittests.py $problem.json js > $OUTDIR/test_$problem.js
  python unittests.py $problem.json objc > $OUTDIR/test_$problem.m
done
